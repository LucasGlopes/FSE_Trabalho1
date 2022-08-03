from os import system, name
import time

cruzamentos = []
 
def limpaTela():
  
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def atualizaInfo(mensagem):
    global cruzamentos

    cruzamentos.append(mensagem)

def calculaMedia(lista):
    total = 0
    for i in lista:
        total += i

    return total/len(lista)

def calculaFluxo(qtdCarros, tempoInicial):
    tempoFinal = time.time()

    return (qtdCarros/(tempoFinal - tempoInicial))/60


def print_menu_info():
    global cruzamentos
    limpaTela()

    for cruz in cruzamentos:
        print('INFORMAÇÕES CRUZAMENTO',cruz["numeroCruzamento"],'\n')
        print('Velocidade Média na Via Principal:', calculaMedia(cruz["velocidadesViaPrincipal"]),'\n')
        print('Fluxo de carros na Via Auxiliar - Sentido 1:',calculaFluxo(cruz["qtdCarrosViaAuxiliar_S1"],cruz["tempoInicial"]),'\n')
        print('Fluxo de carros na Via Auxiliar - Sentido 2:',calculaFluxo(cruz["qtdCarrosViaAuxiliar_S2"],cruz["tempoInicial"]),'\n')


    saida = input('Pressione ENTER para voltar ao menu')
    limpaTela()


def print_menu():
    while True:
        print('\nSERVIDOR CENTRAL\n')
        print('Selecione uma opção\n')
        print('1 - Verificar informações dos cruzamentos\n')
        print('2 - Comando para cruzamentos\n')

        opcao = int(input())

        while opcao != 1 and opcao != 2:
            print('INVÁLIDO! Digite 1 ou 2!')
            opcao = int(input())


        if opcao == 1:
            print_menu_info()
