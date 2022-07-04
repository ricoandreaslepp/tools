1) Keyboard streams data to /dev/input/eventN
2) Where N is found from the file /proc/bus/input/devices (AT Translated Set 2 keyboard)
3) Keyboard mapping in /usr/include/linux/input-event-codes.h

* needs root permissions to get access to /dev/input/ folder

# TO-DO
1) missing Windows version
2) finding the event file of the keyboard isn't scripted
3) keyboard mapping isn't complete in keylog_linux.h (m variable)

Used for inspiration and help: https://github.com/nayan4755/linux_keylogger
