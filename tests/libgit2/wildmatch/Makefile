
CWD := $(shell pwd)
LIBGIT2_DIR := $(shell dirname ${CWD})
LIBGIT2_SRC := ${LIBGIT2_DIR}/src/libgit2
LIBGIT2_BLD := ${LIBGIT2_DIR}/build
LIBGIT2_SO  := ${LIBGIT2_DIR}/lib/libgit2.so
LIBGIT2_EXE := ${LIBGIT2_DIR}/bin/wildmatch.bin
LIBGIT2_GIT := "https://github.com/libgit2/libgit2.git"


all: mkdirs ${LIBGIT2_SRC}/src/libgit2 ${LIBGIT2_SO} ${LIBGIT2_EXE}


.PHONY: mkdirs
mkdirs:
	mkdir --verbose --parents \
	${LIBGIT2_BLD} \
	${LIBGIT2_DIR}/lib \
	${LIBGIT2_DIR}/src


${LIBGIT2_SRC}/src/libgit2:
	git -C ${LIBGIT2_DIR}/src clone ${LIBGIT2_GIT}


${LIBGIT2_SO}:
	cd ${LIBGIT2_BLD}; \
	cmake \
	-DBUILD_CLI=OFF \
	-DBUILD_TESTS=OFF \
	-DREGEX_BACKEND=builtin \
	-DUSE_BUNDLED_ZLIB=ON \
	../src/libgit2; \
	cmake --build .
	cp -av ${LIBGIT2_BLD}/libgit2.so* ${LIBGIT2_DIR}/lib


${LIBGIT2_EXE}:
	gcc \
	-Wall \
	-I ${LIBGIT2_SRC}/include \
	-I ${LIBGIT2_SRC}/src/libgit2 \
	-I ${LIBGIT2_SRC}/src/util \
	-I ${LIBGIT2_BLD}/src/util \
	-o ${LIBGIT2_EXE} \
	${LIBGIT2_SRC}/src/util/wildmatch.c \
	${CWD}/libgit2_wildmatch.c \
	-L ${LIBGIT2_DIR}/lib \
	-l git2

