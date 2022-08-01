import RPi.GPIO as GPIO
from time import sleep
from semaforo import estados
from valores import TEMPO


QTD_ESTADOS = 6

botoesPedestrePrincipal = dict (
        C1=False,
        C2=False,
)

botoesPedestreAuxiliar = dict (
        C1=False,
        C2=False,
)

sensoresPassagem_1 = dict (
        C1=False,
        C2=False,  
)

sensoresPassagem_2 = dict (
        C1=False,
        C2=False,  
)

def trataBotao(channel, CRUZAMENTO):
        global botoesPedestrePrincipal
        global botoesPedestreAuxiliar

        if channel == CRUZAMENTO['BOTAO_PEDESTRE_2']:
                botoesPedestrePrincipal[CRUZAMENTO['TIPO']] = not botoesPedestrePrincipal[CRUZAMENTO['TIPO']]
        else:
                botoesPedestreAuxiliar[CRUZAMENTO['TIPO']] = not botoesPedestreAuxiliar[CRUZAMENTO['TIPO']]

def trataSensorPassagem(channel, CRUZAMENTO):
        global sensoresPassagem_1
        global sensoresPassagem_2

        if channel == CRUZAMENTO['SENSOR_PASSAGEM_1']:
                sensoresPassagem_1[CRUZAMENTO['TIPO']] = not sensoresPassagem_1[CRUZAMENTO['TIPO']]
        else:
                sensoresPassagem_2[CRUZAMENTO['TIPO']] = not sensoresPassagem_2[CRUZAMENTO['TIPO']]

def atualizaEstado(estadoAtual, CRUZAMENTO):
        global botoesPedestrePrincipal
        global botoesPedestreAuxiliar
        global sensoresPassagem_1
        global sensoresPassagem_2

        if estadoAtual == 1:
                tempo_max = TEMPO['PRINCIPAL_VERDE_MAXIMO']
                tempo_atual = TEMPO['PRINCIPAL_VERDE_MINIMO']
                while tempo_atual < tempo_max and (not botoesPedestrePrincipal[CRUZAMENTO['TIPO']]) and (not sensoresPassagem_1[CRUZAMENTO['TIPO']]) and (not sensoresPassagem_2[CRUZAMENTO['TIPO']]):
                        sleep(0.1)
                        tempo_atual = tempo_atual + 0.1
                
                if botoesPedestrePrincipal[CRUZAMENTO['TIPO']] or sensoresPassagem_1[CRUZAMENTO['TIPO']] or sensoresPassagem_2[CRUZAMENTO['TIPO']]:
                        botoesPedestrePrincipal[CRUZAMENTO['TIPO']] = False
                        # sensoresPassagem_1[CRUZAMENTO['TIPO']] = False
                        # sensoresPassagem_2[CRUZAMENTO['TIPO']]  = False
                        return 3
                else:
                        (estadoAtual + 1) % QTD_ESTADOS

        elif estadoAtual == 4:
                tempo_max = TEMPO['AUXILIAR_VERDE_MAXIMO']
                tempo_atual = TEMPO['AUXILIAR_VERDE_MINIMO']
                while tempo_atual < tempo_max and botoesPedestreAuxiliar[CRUZAMENTO['TIPO']] == False:
                        sleep(0.1)
                        tempo_atual = tempo_atual + 0.1
        
                if botoesPedestreAuxiliar[CRUZAMENTO['TIPO']]:
                        botoesPedestreAuxiliar[CRUZAMENTO['TIPO']] = False
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

        GPIO.add_event_detect(CRUZAMENTO['BOTAO_PEDESTRE_2'],GPIO.RISING,callback=lambda x: trataBotao(CRUZAMENTO['BOTAO_PEDESTRE_2'],CRUZAMENTO), bouncetime=300)
        GPIO.add_event_detect(CRUZAMENTO['BOTAO_PEDESTRE_1'],GPIO.RISING,callback=lambda x: trataBotao(CRUZAMENTO['BOTAO_PEDESTRE_1'],CRUZAMENTO), bouncetime=300)


        GPIO.setup(CRUZAMENTO['SENSOR_PASSAGEM_1'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(CRUZAMENTO['SENSOR_PASSAGEM_2'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.add_event_detect(CRUZAMENTO['SENSOR_PASSAGEM_1'],GPIO.BOTH,callback=lambda x: trataSensorPassagem(CRUZAMENTO['SENSOR_PASSAGEM_1'],CRUZAMENTO))
        GPIO.add_event_detect(CRUZAMENTO['SENSOR_PASSAGEM_2'],GPIO.BOTH,callback=lambda x: trataSensorPassagem(CRUZAMENTO['SENSOR_PASSAGEM_2'],CRUZAMENTO))

        while True:
                estados[estadoAtual](semaforoPrincipal, semaforoAuxiliar)
                estadoAtual = atualizaEstado(estadoAtual, CRUZAMENTO)


        

