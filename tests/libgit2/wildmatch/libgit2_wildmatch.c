#include <stdio.h>
#include "wildmatch.h"


int main(int argc, char *argv[])
{
    if (argc != 4) {
        fprintf(stderr, "BAD ARGUMENTS.\n");
        return 1;
    }
    const char *pattern = (const char*) argv[1];
    const char *text = (const char*) argv[2];
    const unsigned int flag = strtoul(argv[3], 0, 10);
    return wildmatch(pattern, text, flag);
}

