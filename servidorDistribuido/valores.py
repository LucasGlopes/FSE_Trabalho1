import socket


CRUZAMENTO_1 = dict(
    SEMAFORO_1_VERDE=1,  
    SEMAFORO_1_AMARELO =26,
    SEMAFORO_1_VERMELHO=21,
    SEMAFORO_2_VERDE =20,
    SEMAFORO_2_AMARELO =16,
    SEMAFORO_2_VERMELHO=12,
    BOTAO_PEDESTRE_1 =8,
    BOTAO_PEDESTRE_2 =7,
    SENSOR_PASSAGEM_1=14,
    SENSOR_PASSAGEM_2=15,
    SENSOR_VELOCIDADE_1_A=18,
    SENSOR_VELOCIDADE_1_B=23,
    SENSOR_VELOCIDADE_2_A=24,
    SENSOR_VELOCIDADE_2_B=25,
    TIPO=socket.gethostname()+' - C1'
)

CRUZAMENTO_2 = dict(
    SEMAFORO_1_VERDE=2,
    SEMAFORO_1_AMARELO=3,
    SEMAFORO_1_VERMELHO=11,
    SEMAFORO_2_VERDE=0,
    SEMAFORO_2_AMARELO=5,
    SEMAFORO_2_VERMELHO=6,
    BOTAO_PEDESTRE_1=10,
    BOTAO_PEDESTRE_2=9,
    SENSOR_PASSAGEM_1=4,
    SENSOR_PASSAGEM_2=17,
    SENSOR_VELOCIDADE_1_A=27,
    SENSOR_VELOCIDADE_1_B=22,
    SENSOR_VELOCIDADE_2_A=13,
    SENSOR_VELOCIDADE_2_B=19,
    TIPO=socket.gethostname()+' - C2'
)

TEMPO = dict(
    PRINCIPAL_VERDE_MINIMO=10,
    PRINCIPAL_VERDE_MAXIMO=20,
    AUXILIAR_VERDE_MINIMO=5,
    AUXILIAR_VERDE_MAXIMO=10,
    AMARELO=3,
    VERMELHO_TOTAL=1
)

