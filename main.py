from Processo import Processo
import random
import string

arqEntradas = open("entradas.txt")
arqLinhas = arqEntradas.readlines()
arqEntradas.close()
processosPrioritarios = []
processosUsuario = []
tempos = []
nomes = []

for tempo in arqLinhas:
    tempo = tempo.split(',')
    tempos.append(int(tempo[0]))

tempos.sort

for tempo in range(0,int(tempos[-1])+1):
    processosPrioritarios.append([])
    processosUsuario.append([])


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
    processosPrioritarios[int(novoProcesso[0])].append(Processo(nome,novoProcesso[1],novoProcesso[2],novoProcesso[4],novoProcesso[5],novoProcesso[3]))


