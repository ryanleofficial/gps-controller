# USB-Port-GPS Module
LINK: http://wiki.52pi.com/index.php/USB-Port-GPS_Module_SKU:EZ-0048

NOTE: If you have a Pi3 please go with UART styles
## Wiring
	FTDI ---->GPS(L80-M39)
	VCC 		VCC
	GND		GND
	TXD 		RXD
	RXD		TXD

## Setup 
Install minicom
```
$ sudo apt-get install minicom
```
Check data read from usb port 
```
$ sudo cat /dev/ttyUSB0

	You should see this :

			$GPZDA,182728.000,23,07,2017,,*52
			$GPRMC,182728.000,A,4729.9516,N,12209.9076,W,1.73,175.32,230717,,,A*7E
			$GPGGA,182728.000,4729.9516,N,12209.9076,W,1,3,9.32,149.7,M,-17.3,M,,*63
			$GPGSA,A,2,19,17,12,,,,,,,,,,9.37,9.32,1.00*0A
			$GPTXT,01,01,02,ANTSTATUS=
			$GPZDA,182729.000,23,07,2017,,*53
```

Check reading data using minicom
```
$ minicom -b 9600 -o -D /dev/ttyUSB0
```

Open terminal
```
$ sudo apt-get update && sudo apt-get -y install gpsd gpsd-clients python-gps 
```

Reboot and reconfigure 
```
$ sudo nano /etc/default/gpsd
	Change to:
		# Default settings for the gpsd init script and the hotplug wrapper.
		# Start the gpsd daemon automatically at boot time
		START_DAEMON="true"

		# Use USB hotplugging to add new USB devices automatically to the daemon
		USBAUTO="true"

		# Devices gpsd should collect to at boot time.
		# They need to be read/writeable, either by user gpsd or the group dialout.
		DEVICES="/dev/ttyUSB0"

		# Other options you want to pass to gpsd
		GPSD_OPTIONS="-n"
		GPSD_SOCKET="/var/run/gpsd.sock"
    
Save, Exit and Reboot 
```
Start the gps service
```
$ sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock
```
Run 
```
$ sudo cgps -s
```

# Using UART instead of USB (Adafruit Ultimate GPS on the Raspberry Pi)
## Wiring:
```
	Pi ----- Adafruit Ultimate GPS
	TxD  -	RxD
	RxD  -	TxD
	5v   -  5v
	GND  -  GND
```

Edit /boot/cmdline.txt
```
$ sudo nano /boot/cmdline.txt
```
```
And change:

dwc_otg.lpm_enable=0 console=ttyAMA0,115200 kgdboc=ttyAMA0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait

to:
dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait
(eg, remove console=ttyAMA0,115200 and if there, kgdboc=ttyAMA0,115200)

Note: you might see console=serial0,115200 or console=ttyS0,115200 and should remove those parts of the line if present.
```
## Raspbian Jessie
To stop and disable the tty service:
```
sudo systemctl stop serial-getty@ttyAMA0.service
sudo systemctl disable serial-getty@ttyAMA0.service 
```

Edit the /boot/config.txt file:
```
sudo nano /boot/config.txt
```

At the very bottom of the file add this on a new line:
```
enable_uart=1
```
Reboot your Pi

Run these commands:
```
$ sudo killall gpsd
$ sudo gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock
```

Test Output:
```
$ cgps -s
```
