from os import path, remove
from urllib2 import urlopen
from json import loads, dumps
from subprocess import Popen, PIPE
from RPi.GPIO import setmode, BOARD, setwarnings, setup, output as o, input as i, OUT, IN
from time import sleep

import dht11


#import math
import MFRC522

baseurl = 'http://test.q1q2.net/1/?action='


start = True
config = 'config.txt'
while start:
	if path.exists(config):
		print 'config ok'

		file = open(config, 'r') 
		result = file.read()
		file.close()

		result = loads(result)

	else:
		print 'config error'

		p1 = Popen(['ifconfig', '-a'], stdout=PIPE)
		p2 = Popen(["grep", "HWaddr"], stdin=p1.stdout, stdout=PIPE)
		output = p2.communicate()[0]
		mac = output.split()[-1]

		url = baseurl+'start&mac='+mac

		f = urlopen(url)
		result = f.read()  
		f.close()

		print result
		result = loads(result)

	if (result['token']!='NULL'):
		token = result['token']

		file = '{"token":"'+token+'"}'
		f = open(config, 'w')
		f.write(file)
		f.close()

		start = False

print token



pin_T = True
patch = 'pins.txt'
while pin_T:
	if path.exists(patch):
		print 'pins ok'

		file = open(patch, 'r') 
		result = file.read()
		file.close()

		pins = loads(result)

		if pins['i'] is None and pins['o'] is None and pins['t'] is None:
			remove(patch)

	else:
		print 'pins error'

		url = baseurl+'get_pins&token='+token

		f = urlopen(url)
		result = f.read()  
		f.close()

		print result
		result = loads(result)
		pins = result['pins']

	if pins['i'] is not None or pins['o'] is not None or pins['t'] is not None :
		
		file = dumps(pins)

		f = open(patch, 'w')
		f.write(file)
		f.close()

		pin_T = False



patch = 'rfids.txt'

url = baseurl+'get_rfids&token='+token

f = urlopen(url)
result = f.read()  
f.close()

print result
result = loads(result)
		
rfids = result['rfids']
if rfids is not None:
	file = dumps(rfids)

	f = open(patch, 'w')
	f.write(file)
	f.close()

#print rfids


setmode(BOARD)
setwarnings(False)

for pin in pins['i']:
	setup(pin,IN)

for pin in pins['o']:
	setup(pin,OUT)


#For RFIDS
MIFAREReader = MFRC522.MFRC522()


q = True
while q:
	pp = ''
	for pin in pins['i']:
		#print i(pin)
		pp = pp+'"'+str(pin)+'":'+str(i(pin))+','

	for pin in pins['t']:
		#humidity, temperature = Adafruit_DHT.read_retry(11, 22)
		#t=temperature
		#h=humidity

		instance = dht11.DHT11(pin)
		result = instance.read()

		if result.is_valid():
		    t = result.temperature
		    h = result.humidity
		else:
		    t = '-'
		    h = '-'

		pp = pp+'"'+str(pin)+'":'+str(t)+','




	pp = '{'+pp[0:-1]+'}'
	print pp
	#http://91.202.240.29/?action=set_pins&token=abc123&pins={"37":1,"12":1}
	url = baseurl+'set_pins&token='+token+'&pins='+pp

	f = urlopen(url)
	result = f.read()  
	f.close()

	print result

	result = loads(result)
	
	status = result['status']
	if result['guard']==0:
		for (pin, s) in status.items():
			o(int(pin),s)
			#print pin + ' ' + str(s)
	else:
		for pin in pins['o']:
			o(pin,0)

	cmds = result['cmd']

	if cmds is not None:
		oo = ''
		for cmd in cmds:
			out = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE).stdout.read().split("\n")[0:-1]

			l = ''
			for line in out:
				l = l + line + "%0A"	# %0D%0A

			oo = oo + '"'+cmd+'":"'+l+'",'
			print out

		oo = '{'+oo[0:-1]+'}'

		#print oo

		url = baseurl + 'cmd_result&token='+token+'&cmd_id='+str(result['cmd_id'])+'&result='+oo
		print url

		f = urlopen(url)
		result = f.read()  
		f.close()
		
		print result


	sleep(0.5)

	
	#start RFID
	(status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

	# Read UID
	(status,uid) = MIFAREReader.MFRC522_Anticoll()
	if status == MIFAREReader.MI_OK:
		UIDcode = str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])

		print UIDcode
		print rfids

		#for f in frids:
		#	print r

		if int(UIDcode) in rfids:
			print "rfid ok"

			url = baseurl + 'upd_guard&token='+token

			f = urlopen(url)
			result = f.read()  
			f.close()

			#for pin in pins['o']:
			#	o(pin,1)
		else:
			print "rfid error"
			for pin in pins['o']:
				o(pin,0)


			url = baseurl + 'add_new_rfid&token='+token+'&cid='+UIDcode
			print url

			f = urlopen(url)
			result = f.read()  
			f.close()
			
			print result
	# end RFID


GPIO.cleanup()
