import RPi.GPIO as GPIO
from cruzamento import inicializaCruzamento
from valores import CRUZAMENTO_1, CRUZAMENTO_2
from multiprocessing import Process
import sys

if __name__ == "__main__":
    host = sys.argv[1]
    port = int(sys.argv[2])

    GPIO.setmode(GPIO.BCM)

    cruz1 = Process(target=inicializaCruzamento,args=(CRUZAMENTO_1,host,port), daemon=True)
    cruz2 = Process(target=inicializaCruzamento,args=(CRUZAMENTO_2,host,port), daemon=True)


    cruz1.start()
    cruz2.start()

    name = input('Press enter to exit')
