#AUTHOR : ROHIT ATHAVALE
#EMAIL  : rohit.athavale89@gmail.com
#Basic Script to display Battery Stats
#To make this script visible in your sl4a app
#send this script to the sl4a/scripts/ folder in your sdcard
#For example : $ adb push battery_stats.py /mnt/sdcard/sl4a/scripts/
#Visit http://www.mithril.com.au/android/doc/BatteryManagerFacade.html for more details
import android,time
droid = android.Android()

#Start Monitoring Battery Events,Wait for few events
droid.batteryStartMonitoring()
time.sleep(2)

#Battery Technology
batteryTech = droid.batteryGetTechnology().result
print 'Battery Technology',batteryTech
droid.makeToast('Battery Technology %s'%batteryTech)
time.sleep(3)

#Battery Level
batteryLevel = droid.batteryGetLevel().result
print 'Battery Level is %d percent'%batteryLevel
droid.makeToast('Battery Level is %d percent'%batteryLevel)
time.sleep(3)

#Battery Temperature
batteryTemp = droid.batteryGetTemperature().result
print 'Battery Temperature: %d Kelvin(K)'%batteryTemp
droid.makeToast('Battery Temperature %d Kelvin(K)'%batteryTemp)
time.sleep(3)

#All battery data
batteryData=droid.readBatteryData().result
print "All battery Data \n ",batteryData
time.sleep(3)

#Stop monitoring
droid.batteryStopMonitoring()
