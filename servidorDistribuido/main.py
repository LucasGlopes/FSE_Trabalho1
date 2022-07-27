import RPi.GPIO as GPIO
from cruzamento import inicializaCruzamento
from valores import CRUZAMENTO_1, CRUZAMENTO_2
from threading import Thread

GPIO.setmode(GPIO.BCM)

cruz1 = Thread(target=inicializaCruzamento, args=(CRUZAMENTO_1,), daemon=True)
cruz2 = Thread(target=inicializaCruzamento, args=(CRUZAMENTO_2,), daemon=True)

cruz1.start()
cruz2.start()

name = input('Press enter to exit')

# inicializaCruzamento(CRUZAMENTO_1)

