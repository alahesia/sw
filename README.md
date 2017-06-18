# sw
Smart Home on Raspberry Pi 3


Convert py to pyc
=====================
```python
nano pyc.py

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


Git about README
=====================
> h1 =====================
***
> h2 -----------------------------------


Link: <http://webdesign.ru.net/article/pravila-oformleniya-fayla-readmemd-na-github.html>