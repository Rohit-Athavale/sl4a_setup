SL4A setup

#This setup will guide you to setting up Scripting Layer for Android on your device. 
#You can execute python scripts and access the python #interpreter with this app.
#You can visit http://code.google.com/p/android-scripting/wiki/Tutorials for more info
#Steps 1-8 are the steps for installing the Android SDK.Skip these if you already have it or don't need it
#Steps 9-12 are to install the SL4A setup


1.Download the Android SDK from here : http://developer.android.com/sdk/index.html

2.Go to the Tools folder in the android sdk folder (android-sdk-linux/tools/)

3.Execute the executable named android(./android)

4.It will setup an installation.Install the android-sdk tools and the android-sdk platform tools(API's are not required for SL4A)

5.After the installation,open the platform-tools directory.You will find the adb executable.
  (Optional)Add the path of this directory to your bashrc
    Example:echo "export PATH=$PATH:/home/user/android-sdk-linux/platform-tools/" >> /home/user/.bashrc

6.To check if adb is successfully installed :
    $./adb should give you a long menu (if you are in the platform-tools-directory and you haven't done step 5)
    $adb should give the long menu

7.To get access to you android device you must first modify the udev rules
    Please visit http://developer.android.com/tools/device.html#VendorIds first and read steps 2-3
    Say your phone is LG and your look up the list you see its vendor id as 1004.
    Then ,
	A)Login as root(su) and create the file : /etc/udev/rules.d/51-android.rulesand add the following to its contents : 
	
	"SUBSYSTEM=="usb", ATTR{idVendor}=="0bb4", MODE="0666", GROUP="plugdev". Then,
	
	$chmod +x /etc/udev/rules.d/51-android.rules
	
	B)Since the vendor id is 1004(for LG)
	$echo "0x1004" >> ~/.android/adb_usb.ini
Also visit http://blog.apkudo.com/2012/08/21/one-true-adb_usb-ini-to-rule-them-all/ for all devices

8.After this,when you perform an adb command you will be able to see your device
	To test this you can try :
	user@ubuntu:$ adb devices
	List of devices attached 
	D025A0A023970L5C	device
If you see no device id ,it means your device is not successfully connected.Check 51-android.rules .

9.Install the Python For Android apk and the SL4A(Scripting Layer For Android) apk as follows:
	user@ubuntu:folder-containing-these-apk$adb install PythonForAndroid_r5.apk
	user@ubuntu:folder-containing-these-apk$adb install sl4a_r6.apk
Or download the latest apk from http://code.google.com/p/android-scripting/downloads/list and install it or install it from the android store

10.After that to install some sample scripts,open to the Python For Android App in your installed apps on your phone/tablet
 and press the 'Install' button upon opening the Python For Android app.
11.Then open your SL4A app you should see a list of python files on your screen. Click on the say_time.py and then press on the 
  small shell terminal(black) icon on the extreme left of the menu that pops up.If you hear the time correctly,your Sl4A setup is complete.

12.You can try my sample Battery statistics script in this repository.
