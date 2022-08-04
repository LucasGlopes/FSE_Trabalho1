import socket
import json
import pickle

def socketCliente(host, port, CRUZAMENTO):
    global conexao

    conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conexao.connect((host, port))

    dadosCruzamento = {
        "numeroCruzamento": CRUZAMENTO['TIPO'],
        "velocidadesViaPrincipal": [],
        "qtdCarrosViaAuxiliar_S1": 0,
        "qtdCarrosViaAuxiliar_S2": 0,
        "qtdInfracoesSinal": 0,
        "qtdInfracoesVelocidade": 0,
        "tempoInicial": 0
    }
    try:
        while True:
            envia_mensagem(dadosCruzamento)
            data = conexao.recv(1024)
            
    except:
        print('Ocorreu um erro')
        conexao.close()

def envia_mensagem(dadosCruzamento):
    global conexao

    conexao.send(pickle.dumps(dadosCruzamento))