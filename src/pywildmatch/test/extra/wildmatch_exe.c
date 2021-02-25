
#include "common.h"

int wildmatch(const char *pattern, const char *text, unsigned int flags);

int main(int argc, char *argv[]) {
    if (argc != 4) {
        fprintf(stderr, "BAD ARGUMENTS.\n");
        return 1;
    }

    const char *pattern = (const char*) argv[1];
    const char *text = (const char*) argv[2];
    unsigned int flags = strtoul(argv[3], 0, 10);

    return wildmatch(pattern, text, flags);
}

