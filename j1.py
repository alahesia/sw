import json

file = open('json.txt', 'r') 
f = file.read()

temp = json.loads(f)


for (id, pin) in temp['i'].items():
    print id, pin

#for temp['i'] in list:
#print temp['i']['1']