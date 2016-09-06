# Firstly we should write these codes to terminal
# sudo apt-get install git
# git clone git://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code.git
# cd Adafruit-Raspberry-Pi-Python-Code
# cd Adafruit_CharLCD
# nano ilk_yazi.py

from Adafruit_CharLCD import Adafruit_CharLCD
import time
import imaplib
import RPi.gpio as GPIO
msrvr = imaplib.IMAP4_SSL\
        ('imap.gmail.com',993)


unm = '***Mail Adress***'
pwd = '***Password***'
msrvr.login(unm,pwd)


stat,cnt = msrvr.select('Inbox')


stat, dta = msrvr.fetch\
            (cnt[0],\
             '(UID BODY[TEXT])')




dp = Adafruit_CharLCD()

dp.message(data[0][1])

#for x in range(0,16):
#	dp.scrollDisplayRight()
#	sleep(.2)
#dp.clear()	
#dp.begin(16,2)
#dp.setCursor(8,0)
#dp.message('ilk yazi\n hello world')
#for x in range(0,16):
#	dp.DisplayLeft()
#	sleep(.2)


	
msrvr.close()
msrvr.logout()
dp.clear()
GPIO.cleanup()

# After writing the codes save the file
# sudo python ilk_yazi.py




