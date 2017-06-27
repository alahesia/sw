# sw
Smart Home on Raspberry Pi 3


Convert py to pyc
=====================
```python
nano pyc.py

#!/usr/bin/python
import py_compile 
py_compile.compile('abc.py')

python pyc.py
```
or

```python
python -m compileall Read.py
python -m compileall Read.py Read2.py
```
Link: <https://stackoverflow.com/posts/38426786/revisions>


GPIO on console
=====================
```bash
gpio readall
gpio mode <pin> in/out

gpio write <pin> 0/1
gpio read <pin>
```

Link: <http://wiringpi.com/the-gpio-utility/>


Avtoload script on load Raspberry
=====================
```bash
$ cd ~
$ sudo nano c
```

Create bash file
```bash
#!/bin/bash
python c2.py
```

```bash
$ sudo nano .bashrc
./c
```



KILL PID
=====================
```bash
top
ps -la  #pid only 1 users
kill PID[ PID2 PID3]
killall PIDNAME


pstree #tree pid

```


Git about README
=====================
> h1 =====================
>***
> h2 -----------------------------------


Link: <http://webdesign.ru.net/article/pravila-oformleniya-fayla-readmemd-na-github.html>
