# USB-Port-GPS Module
LINK: http://wiki.52pi.com/index.php/USB-Port-GPS_Module_SKU:EZ-0048

NOTE: If you have a Pi3 please go with UART styles
## Wiring
	FTDI ---->GPS(L80-M39)
	VCC 		VCC
	GND			GND
	TXD 		RXD
	RXD			TXD

## Setup 
Install minicom
```
$ sudo apt-get install minicom
```

After power on and login to system. Open terminal
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
