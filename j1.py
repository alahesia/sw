import json
#import subprocess
from subprocess import Popen, PIPE

file = open('json.txt', 'r') 
f = file.read()

temp = json.loads(f)

temp2 = temp['pins']

for pin in temp2['i']:
    print pin

#for (id, pin) in temp['i'].items():
#    print id, pin


file = open('cmd.txt', 'r') 
f = file.read()

temp = json.loads(f)


#PIPE = subprocess.PIPE
for (id, cmd) in temp.items():
    #print id, cmd
    out, p = Popen(cmd, shell=True, stdout=PIPE).communicate()
    print out


p1 = Popen(['ifconfig', '-a'], stdout=PIPE)
p2 = Popen(["grep", "HWaddr"], stdin=p1.stdout, stdout=PIPE)
output = p2.communicate()[0]
mac = output.split()[-1]

print mac