from Processo import Processo
from Memoria import Memoria
from Periferico import Periferico
from Escalonador import Escalonador
from Processador import Processador

import random
import string

filaChegada = []
lPerifericos = []
memoria = Memoria(16000)
escalonador = Escalonador([Processador(),Processador(),Processador(),Processador()])

arqEntradas = open("entradas.txt")
arqLinhas = arqEntradas.readlines()
arqEntradas.close()
tempos = []
nomes = []

for tempo in arqLinhas:
    tempo = tempo.split(',')
    tempos.append(int(tempo[0]))

tempos.sort

for tempo in range(0,int(tempos[-1])+1):
    filaChegada.append([])


for processo in arqLinhas:
    while(True):
        nome = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        if(len(nomes) == 0):
            nomes.append(nome)
            break
        else:
            if(nome not in nomes):
                nomes.append(nome)
                break
    novoProcesso = processo.rstrip('\n').split(',')
    filaChegada[int(novoProcesso[0])].append(Processo(nome,novoProcesso[1],novoProcesso[2],novoProcesso[4],novoProcesso[5],novoProcesso[3]))

lPerifericos.append(Periferico(True,"impressora"))
lPerifericos.append(Periferico(True,"impressora"))
lPerifericos.append(Periferico(True,"disco"))
lPerifericos.append(Periferico(True,"disco"))

for tempoAtual in range(len(filaChegada)):
    if(len(filaChegada[tempoAtual]) > 0): 
        print("TEMPO {}:".format(tempoAtual))
        print("---------------------------------------------Novos Processos------------------------------------------------")
        for processoChegando in filaChegada[tempoAtual]:
            print(processoChegando)
            print()
        print("------------------------------------------------------------------------------------------------------------")
    else:
        print("TEMPO {}: \n\tNão chegaram novos processos!!!".format(tempoAtual))

    

    # print("---------------------------------------------Mudanças de Estado---------------------------------------------")
    # filaChegada[12][0].bloqueia()
    # print("------------------------------------------------------------------------------------------------------------")