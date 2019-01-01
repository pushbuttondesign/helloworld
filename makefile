#
# makefile usage: make --file=name
#

all:
	gcc -g -Wall -O0 \
	-o ./hello.out \
	./hello.c \
	~/librarys/source/LIBRARYlib.c \
	-I ~/librarys/include \
	-L ~/librarys/lib
