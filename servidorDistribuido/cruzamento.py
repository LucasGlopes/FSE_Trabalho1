import RPi.GPIO as GPIO
from time import sleep
import time
from semaforo import estados
from valores import TEMPO


QTD_ESTADOS = 6

botaoPedestrePrincipal = False
botaoPedestreAuxiliar = False

sensorPassagem_1 = False
sensorPassagem_2 = False

tempoInicialSensor_1 = 0
tempoFinalSensor_1 = 0

tempoInicialSensor_2 = 0
tempoFinalSensor_2 = 0

def trataTempoInicial(channel, CRUZAMENTO):
        global tempoInicialSensor_1
        global tempoInicialSensor_2

        if channel == CRUZAMENTO['SENSOR_VELOCIDADE_1_B']:
                tempoInicialSensor_1 = time.time()
        else:
                tempoInicialSensor_2 = time.time()

def trataTempoFinal(channel, CRUZAMENTO):
        global tempoInicialSensor_1
        global tempoInicialSensor_2
        global tempoFinalSensor_1
        global tempoFinalSensor_2

        if channel == CRUZAMENTO['SENSOR_VELOCIDADE_1_A']:
                tempoFinalSensor_1 = time.time()
                print(round(((1/ (tempoFinalSensor_1 - tempoInicialSensor_1)) * 3.6), 2),'km/h')
        else:
                tempoFinalSensor_2 = time.time()
                print(round(((1/ (tempoFinalSensor_2 - tempoInicialSensor_2)) * 3.6), 2),'km/h')


def trataBotao(channel, CRUZAMENTO):
        global botaoPedestrePrincipal
        global botaoPedestreAuxiliar

        if channel == CRUZAMENTO['BOTAO_PEDESTRE_2']:
                botaoPedestrePrincipal = not botaoPedestrePrincipal
        else:
                botaoPedestreAuxiliar = not botaoPedestreAuxiliar

def trataSensorPassagem(channel, CRUZAMENTO):
        global sensorPassagem_1
        global sensorPassagem_2

        if channel == CRUZAMENTO['SENSOR_PASSAGEM_1']:
                sensorPassagem_1 = not sensorPassagem_1
        else:
                sensorPassagem_2 = not sensorPassagem_2

def atualizaEstado(estadoAtual):
        global botaoPedestrePrincipal
        global botaoPedestreAuxiliar
        global sensorPassagem_1
        global sensorPassagem_2

        if estadoAtual == 1:
                tempo_max = TEMPO['PRINCIPAL_VERDE_MAXIMO']
                tempo_atual = TEMPO['PRINCIPAL_VERDE_MINIMO']
                while tempo_atual < tempo_max and (not botaoPedestrePrincipal) and (not sensorPassagem_1) and (not sensorPassagem_2):
                        sleep(0.1)
                        tempo_atual = tempo_atual + 0.1
                
                if botaoPedestrePrincipal or sensorPassagem_1 or sensorPassagem_2:
                        botaoPedestrePrincipal = False
                        return 3
                else:
                        (estadoAtual + 1) % QTD_ESTADOS

        elif estadoAtual == 4:
                tempo_max = TEMPO['AUXILIAR_VERDE_MAXIMO']
                tempo_atual = TEMPO['AUXILIAR_VERDE_MINIMO']
                while tempo_atual < tempo_max and botaoPedestreAuxiliar == False:
                        sleep(0.1)
                        tempo_atual = tempo_atual + 0.1
        
                if botaoPedestreAuxiliar:
                        botaoPedestreAuxiliar = False
                        return 0
                else:
                        (estadoAtual + 1) % QTD_ESTADOS

        return (estadoAtual + 1) % QTD_ESTADOS

def inicializaCruzamento(CRUZAMENTO):
        semaforoPrincipal = [CRUZAMENTO['SEMAFORO_2_VERDE'], CRUZAMENTO['SEMAFORO_2_AMARELO'], CRUZAMENTO['SEMAFORO_2_VERMELHO']]
        semaforoAuxiliar = [CRUZAMENTO['SEMAFORO_1_VERDE'], CRUZAMENTO['SEMAFORO_1_AMARELO'], CRUZAMENTO['SEMAFORO_1_VERMELHO']]

        estadoAtual = 0

        GPIO.setup(semaforoPrincipal, GPIO.OUT)
        GPIO.setup(semaforoAuxiliar, GPIO.OUT)

        GPIO.setup(CRUZAMENTO['BOTAO_PEDESTRE_2'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(CRUZAMENTO['BOTAO_PEDESTRE_1'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.setup(CRUZAMENTO['SENSOR_PASSAGEM_1'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(CRUZAMENTO['SENSOR_PASSAGEM_2'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.setup(CRUZAMENTO['SENSOR_VELOCIDADE_1_A'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(CRUZAMENTO['SENSOR_VELOCIDADE_1_B'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(CRUZAMENTO['SENSOR_VELOCIDADE_2_A'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(CRUZAMENTO['SENSOR_VELOCIDADE_2_B'], GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(CRUZAMENTO['BOTAO_PEDESTRE_2'],GPIO.RISING,callback=lambda x: trataBotao(CRUZAMENTO['BOTAO_PEDESTRE_2'],CRUZAMENTO), bouncetime=300)
        GPIO.add_event_detect(CRUZAMENTO['BOTAO_PEDESTRE_1'],GPIO.RISING,callback=lambda x: trataBotao(CRUZAMENTO['BOTAO_PEDESTRE_1'],CRUZAMENTO), bouncetime=300)

        GPIO.add_event_detect(CRUZAMENTO['SENSOR_PASSAGEM_1'],GPIO.BOTH,callback=lambda x: trataSensorPassagem(CRUZAMENTO['SENSOR_PASSAGEM_1'],CRUZAMENTO))
        GPIO.add_event_detect(CRUZAMENTO['SENSOR_PASSAGEM_2'],GPIO.BOTH,callback=lambda x: trataSensorPassagem(CRUZAMENTO['SENSOR_PASSAGEM_2'],CRUZAMENTO))

        GPIO.add_event_detect(CRUZAMENTO['SENSOR_VELOCIDADE_1_B'],GPIO.FALLING,callback=lambda x: trataTempoInicial(CRUZAMENTO['SENSOR_VELOCIDADE_1_B'],CRUZAMENTO))
        GPIO.add_event_detect(CRUZAMENTO['SENSOR_VELOCIDADE_1_A'],GPIO.FALLING,callback=lambda x: trataTempoFinal(CRUZAMENTO['SENSOR_VELOCIDADE_1_A'],CRUZAMENTO))
        GPIO.add_event_detect(CRUZAMENTO['SENSOR_VELOCIDADE_2_A'],GPIO.FALLING,callback=lambda x: trataTempoInicial(CRUZAMENTO['SENSOR_VELOCIDADE_2_A'],CRUZAMENTO))
        GPIO.add_event_detect(CRUZAMENTO['SENSOR_VELOCIDADE_2_B'],GPIO.FALLING,callback=lambda x: trataTempoFinal(CRUZAMENTO['SENSOR_VELOCIDADE_2_B'],CRUZAMENTO))

        while True:
                estados[estadoAtual](semaforoPrincipal, semaforoAuxiliar)
                estadoAtual = atualizaEstado(estadoAtual)

        

