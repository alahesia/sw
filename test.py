from RPi.GPIO import setmode, BOARD, setwarnings, setup, output as o, input as i, OUT, IN

setmode(BOARD)
setwarnings(False)

setup(31,OUT)

o(31 ,1)