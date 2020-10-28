from Processo import Processo
import random
import string

arqEntradas = open("entradas.txt")
arqLinhas = arqEntradas.readlines()
arqEntradas.close()
processos = []
tempos = []

for tempo in arqLinhas:
    tempo = tempo.split(',')
    tempos.append(int(tempo[0]))

tempos.sort

for tempo in range(0,int(tempos[-1])+1):
    processos.append([])
print(processos)


for processo in arqLinhas:
    nome = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    print(nome)
    novoProcesso = processo.rstrip('\n').split(',')
    processos[int(novoProcesso[0])].append(Processo(nome,novoProcesso[1],novoProcesso[2],novoProcesso[4],novoProcesso[5],novoProcesso[3]))
print(processos)