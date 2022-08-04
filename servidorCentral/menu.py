from os import system, name
import time
from time import sleep
from threading import Thread, Event
import signal

cruzamentos = {}

evento_saida = Event()

def signal_handler(signum, frame):
    evento_saida.set()

signal.signal(signal.SIGINT, signal_handler)
 
def limpaTela():
  
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def atualizaInfo(mensagem):
    global cruzamentos
    cruzamentos[mensagem['numeroCruzamento']] = mensagem

def calculaMedia(lista):
    total = 0

    if len(lista) == 0:
        return 0

    for i in lista:
        total += i

    return total/len(lista)

def calculaFluxo(qtdCarros, tempoInicial):
    tempoFinal = time.time()

    return (qtdCarros/(tempoFinal - tempoInicial))/60


def print_menu_info():
    global cruzamentos
    limpaTela()

    while True:

        for cruz in cruzamentos:
            print('CRUZAMENTO',cruzamentos[cruz]["numeroCruzamento"],'\n')
            print('Velocidade Média na Via Principal:',round(calculaMedia(cruzamentos[cruz]["velocidadesViaPrincipal"]), 2),'km/h\n')
            print('Fluxo de carros na Via Auxiliar - Sentido 1:',round(calculaFluxo(cruzamentos[cruz]["qtdCarrosViaAuxiliar_S1"],cruzamentos[cruz]["tempoInicial"]), 2),'carros/min\n')
            print('Fluxo de carros na Via Auxiliar - Sentido 2:',round(calculaFluxo(cruzamentos[cruz]["qtdCarrosViaAuxiliar_S2"],cruzamentos[cruz]["tempoInicial"]), 2),'carros/min\n')
            print('Quantidade de carros acima da velocidade permitida na Via Principal:',cruzamentos[cruz]["qtdInfracoesVelocidade"],'\n')
            print('Quantidade de carros que ultrapassaram o sinal vermelho na Via Auxiliar:',cruzamentos[cruz]["qtdInfracoesSinal"],'\n')
            
        print('\nDigite CTRL + C para voltar ao menu:')

        if evento_saida.is_set():
            limpaTela()
            evento_saida.clear()
            break

        sleep(1)
        limpaTela()



def print_menu():
    while True:
        print('\nSERVIDOR CENTRAL\n')
        print('Selecione uma opção e aperte ENTER\n')
        print('1 - Verificar informações dos cruzamentos\n')
        print('2 - Comando para cruzamentos\n')
        print('3 - Sair\n')

        opcao = int(input())

        while opcao != 1 and opcao != 2 and opcao != 3:
            print('INVÁLIDO! Digite 1 ou 2 ou 3!')
            opcao = int(input())


        if opcao == 1:
            threadMenu = Thread(target=print_menu_info, daemon=True)
            threadMenu.start()
            threadMenu.join()
        else:
            break
