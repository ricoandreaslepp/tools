1) Keyboard streams data to /dev/input/eventN
2) Where N is found from the file /proc/bus/input/devices (AT Translated Set 2 keyboard)
3) Keyboard mapping in /usr/include/linux/input-event-codes.h

* needs root permissions to get access to /dev/input/ folder

* missing Windows version
* finding the event file of the keyboard isn't automatic yet
