# Fundamentos de Sistemas Embarcados - Trabalho 1 (2022/1)

Este trabalho consiste em um sistema distribuído para o controle e monitoramento de um grupo de sinais de trânsito.
A descrição completa da atividade pode ser vista [aqui](https://gitlab.com/fse_fga/trabalhos-2022_1/trabalho-1-2022-1).

## Execução do Projeto

### Servidor Central
* Acesse o diretório do servidor central:
```
cd FSE_Trabalho1/servidorCentral
```
* Execute o seguinte comando (As portas disponíveis vão de 10281 a 10290):
```
python3 main.py [PORTA]
```

### Servidores Distribuídos
* Acesse o diretório do servidor distribuído:

```
cd FSE_Trabalho1/servidorDistribuido
```
* Execute o comando abaixo. O código, então, irá inicializar os dois cruzamentos da placa em processos diferentes:
```
python3 main.py [ENDEREÇO IP DO SERVIDOR CENTRAL] [PORTA DO SERVIDOR CENTRAL]
```

## Observações
Alguns dos itens requisitados pelo enunciado não foram implementados a tempo. São eles:

* Mecanismo de acionar e desacionar o Modo de emergência e o Modo noturno.
* Alarme sonoro após  detecção de infração por avanço de sinal vermelho.
