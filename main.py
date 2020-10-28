from Processo import Processo

arqEntradas = open("entradas.txt")
arqLinhas = arqEntradas.readlines()
arqEntradas.close()
processos = []
for processo in arqLinhas:
    novoProcesso = processo.rstrip('\n').split(',')
    print(novoProcesso)
    #processos.add(Processo()) 
    