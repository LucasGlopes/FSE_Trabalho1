import socket
import json

def socketCliente(host, port, tipoCruzamento):
    global conexao

    conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.bind(("", 10284))
    conexao.connect((host, port))

    dadosCruzamento = {
        "numeroCruzamento": tipoCruzamento,
        "velocidadesViaPrincipal": [],
        "qtdCarrosViaAuxiliar_S1": 0,
        "qtdCarrosViaAuxiliar_S2": 0,
        "qtdInfracoesSinal": 0,
        "qtdInfracoesVelocidade": 0,
        "tempoInicial": 0
    }
    while True:

        conexao.send(json.dumps(dadosCruzamento).encode('utf-8'))

        data = conexao.recv(1024)

        # print('received from the server :', str(data.decode('ascii')))

        # ans = input('\ncontinue?\n')
        # if ans == 'y':
        #     continue
        # else:
        #     break
    conexao.close()

def envia_mensagem(dadosCruzamento):
    global conexao

    conexao.send(json.dumps(dadosCruzamento).encode('utf-8'))