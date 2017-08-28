import GPSController
import time
gps = GPSController.GpsController()


try:
    # start controller
    gps.start()
    while True:
        print "latitude ", gps.fix.latitude
        print "longitude ", gps.fix.longitude
        print "time utc ", gps.utc, " + ", gps.fix.time
        print "altitude (m)", gps.fix.altitude
        print "speed (m/s) ", gps.fix.speed
        time.sleep(0.5)

#Ctrl C
except KeyboardInterrupt:
    print "User cancelled"

finally:
    print "Stopping gps controller"
    gps.stopController()
    #wait for the tread to finish
    gps.join()
    exit()