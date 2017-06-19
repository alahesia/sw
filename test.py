from RPi.GPIO import setmode, BOARD, setwarnings, setup, output, input as i, OUT, IN

setmode(BOARD)
setwarnings(False)

setup(37,IN)


print i(37)