from Processo import Processo
from Memoria import Memoria
from Periferico import Periferico
from Escalonador import Escalonador
from Processador import Processador
from Computador import Computador

arqEntradas = open("entradas.txt")
arqLinhas = arqEntradas.readlines()
arqEntradas.close()
tempos = []
nomes = []
filaChegada = []

for tempo in arqLinhas:
    tempo = tempo.split(',')
    tempos.append(int(tempo[0]))

tempos.sort

for tempo in range(0,int(tempos[-1])+1):
    filaChegada.append([])

nProcesso = 0
for processo in arqLinhas:
    nome = "P" + str(nProcesso)
    novoProcesso = processo.rstrip('\n').split(',')
    if(int(novoProcesso[1]) == 0):
        novoProcesso[1] = True
    else:
        novoProcesso[1] = False
    filaChegada[int(novoProcesso[0])].append(Processo(nome,novoProcesso[1],int(novoProcesso[2]),int(novoProcesso[4]),int(novoProcesso[5]),int(novoProcesso[3])))
    nProcesso += 1


computador = Computador(filaChegada)

computador.sistemaOperacional()