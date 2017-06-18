import RPi.GPIO as GPIO
import time
import urllib2
import json
import math
import MFRC522

card_01 = '1364147152'


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

MIFAREReader = MFRC522.MFRC522()
 
while True:
 
  #start RFID
  (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

  # Read UID
  (status,uid) = MIFAREReader.MFRC522_Anticoll()
  if status == MIFAREReader.MI_OK:
    UIDcode = str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])

    print UIDcode
    
    if UIDcode == card_01:
    	print "ok"
    else:
    	print "error"
  # end RFID

  time.sleep(1) 

GPIO.cleanup()