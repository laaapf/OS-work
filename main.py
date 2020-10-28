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
    if(int(novoProcesso[1]) == 0):
        novoProcesso[1] = True
    else:
        novoProcesso[1] = False
    filaChegada[int(novoProcesso[0])].append(Processo(nome,novoProcesso[1],int(novoProcesso[2]),int(novoProcesso[4]),int(novoProcesso[5]),int(novoProcesso[3])))

lPerifericos.append(Periferico(True,"impressora"))
lPerifericos.append(Periferico(True,"impressora"))
lPerifericos.append(Periferico(True,"disco"))
lPerifericos.append(Periferico(True,"disco"))

for tempoAtual in range(len(filaChegada)):
    emMemoria = []
    if(len(filaChegada[tempoAtual]) > 0): 
        print("TEMPO {}:".format(tempoAtual))
        print("---------------------------------------------Novos Processos------------------------------------------------")
        for processoChegando in filaChegada[tempoAtual]:
            if(memoria.firstFit(processoChegando)): #quando tem espaço
                memoria.atualizaAlocacao()
                emMemoria.append(processoChegando)
                print(processoChegando)
                print()
            else: #quando não tem
                if(tempoAtual+1 == len(filaChegada)):
                    filaChegada.append([])
                filaChegada[tempoAtual+1].insert(0,processoChegando)
        print("------------------------------------------------------------------------------------------------------------")
    else:
        print("TEMPO {}: \n\tNão chegaram novos processos!!!".format(tempoAtual))
    escalonador.att_pronto(emMemoria,lPerifericos)
    if(len(escalonador.filaPronto)!=0):
        escalonador.executa(lPerifericos)
    escalonador.retiraProcesso(memoria)

vazio = False
for cpu in escalonador.cpus:
    if(cpu.processo != None):
        vazio = True
        break
if(len(escalonador.filaPronto)!=0) : vazio=False
else: vazio=True

while not vazio:
    for cpu in escalonador.cpus:
        if(cpu.processo != None):
            vazio = True
            break
    if(len(escalonador.filaPronto)!=0) : vazio=False
    else: vazio=True
    
    tempoAtual += 1
    print("TEMPO {}: \n\tNão chegaram novos processos!!!".format(tempoAtual))
    escalonador.att_pronto(emMemoria,lPerifericos)
    escalonador.executa(lPerifericos)
    escalonador.retiraProcesso(memoria)
    # print("---------------------------------------------Mudanças de Estado---------------------------------------------")
    # filaChegada[12][0].bloqueia()
    # print("------------------------------------------------------------------------------------------------------------")

print("------------------------------------------------Fim da Execução------------------------------------------------")