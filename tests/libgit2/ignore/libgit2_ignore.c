#include <dirent.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <unistd.h>
#include "git2.h"


static git_repository *repo = NULL;


void mk_tmpdir(char *tmpdir)
{
    char template[] = "/tmp/tmpdir.XXXXXX";
    strcpy(tmpdir, template);
    mkdtemp(tmpdir);
    if (tmpdir == NULL) {
        fprintf(stderr, "ERROR: MAKE TEMP FAILED.\n");
        exit(1);
    }
}


void write_ignoref(char *tmpdir, const char *pattern)
{
    char ignoref[32];
    sprintf(ignoref, "%s%s", tmpdir, "/.gitignore");
    FILE *fd = fopen(ignoref, "w");
    if (fd == NULL) {
        fprintf(stderr, "ERROR: WRITE gitignore FAILED.\n");
        exit(1);
    }
    int len = strlen(pattern);
    for (int i=0; i < len; i++) {
        if (pattern[i] == '\\' && i+1 < len && pattern[i+1] == 'n') {
            putc('\n', fd);
            i++;
        } else {
            putc(pattern[i], fd);
        }
    }
    putc('\n', fd);
    fclose(fd);
}


void remove_dir(char *dir)
{
    struct dirent *ent;
    DIR *fd = opendir(dir);
    while ((ent = readdir(fd)) != NULL) {
        if (!strcmp(".", ent->d_name) || !strcmp("..", ent->d_name)) {
            continue;
        }
        char path[strlen(dir) + strlen(ent->d_name) + 2];
        sprintf(path, "%s/%s", dir, ent->d_name);
        struct stat pathstat;
        stat(path, &pathstat);
        if (S_ISDIR(pathstat.st_mode)) {
            remove_dir(path);
        } else {
            if (unlink(path) == -1) {
                fprintf(stderr, "ERROR: REMOVE %s FAILED.\n", path);
            }
        }
    }
    closedir(fd);
    if (rmdir(dir) == -1) {
        fprintf(stderr, "ERROR: REMOVE %s FAILED.\n", dir);
    }
}


void init_repo(char *dir)
{
    git_libgit2_init();
    int err = git_repository_init(&repo, dir, 0);
    if (err < 0) {
        const git_error *e = git_error_last();
        fprintf(stderr, "ERROR: REPO INIT FAILED %s — %s\n", dir, e->message);
        exit(err);
    }
}


void handle_icase(const int flag)
{
    if (flag != 1) {
        return;
    }
    git_config *cfg;
    git_repository_config(&cfg, repo);
    int err = git_config_set_bool(cfg, "core.ignorecase", 1);
    if (err < 0) {
        const git_error *e = git_error_last();
        fprintf(stderr, "ERROR: REPO CONFIG FAILED — %s\n", e->message);
        exit(err);
    }
    git_config_free(cfg);
}


int get_ignore_status(const char *text)
{
    int is_ignored = 0;
    git_ignore_path_is_ignored(&is_ignored, repo, text);
    return is_ignored;
}


int main(int argc, char *argv[])
{
    if (argc != 4) {
        fprintf(stderr, "BAD ARGUMENTS.\n");
        return 1;
    }
    const char *pattern = (const char*) argv[1];
    const char *text = (const char*) argv[2];
    const unsigned int flag = strtoul(argv[3], 0, 10);

    // TMP
    char tmpdir[20];
    mk_tmpdir(tmpdir);

    // gitignore
    write_ignoref(tmpdir, pattern);

    // INIT REPO
    init_repo(tmpdir);

    // CASE INSENSITIVE FLAG
    handle_icase(flag);

    // IGNORE STATUS
    int ignore_status = get_ignore_status(text);

    // CLEANUP
    remove_dir(tmpdir);
    git_repository_free(repo);

    return (ignore_status == 1) ? 0 : 1;
}

