#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#include <sys/types.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h> 

#define BLOCK_SIZE 512

int main() {
	char * addr;
	int fd;

	fd = open("./test.txt", O_RDWR | O_CREAT, S_IRUSR | S_IWUSR);
	if (fd == -1) {
		return -1;
	}

	if ((addr = mmap(NULL, BLOCK_SIZE, PROT_READ | PROT_WRITE, MAP_PRIVATE, fd, 0)) == MAP_FAILED) {
		return -1;
	}
	
	printf("%s\n", addr);

	munmap(addr, BLOCK_SIZE);
	close(fd);
	return 0;
}
