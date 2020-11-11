from Processo import Processo
from Memoria import Memoria
from Periferico import Periferico
from Escalonador import Escalonador
from Processador import Processador

class Computador(object):
    def __init__(self, filaChegada):    
        self.filaChegada = filaChegada
        self.lPerifericos = [Periferico(True,"impressora", "1"),Periferico(True,"impressora", "2"), Periferico(True,"disco", "1"),Periferico(True,"disco","2")]
        self.memoria = Memoria(16000)
        self.escalonador = Escalonador([Processador(),Processador(),Processador(),Processador()])
        
    def sistemaOperacional(self):
        tempoAtual = 0

        fimFila = False
        vazio = False
        continuar = False
        while not vazio:
            if not continuar:
                x = input("Deseja continuar?")
                if x == "s":
                    continuar = True 
            #Seta os reports no inicio do clock
            reportChegada = ""
            reportPerifericosInicio = ""
            reportPerifericosFinal = ""
            reportCpuInicio = ""
            reportCpuFinal = ""
            reportFilas = ""

            #Verifica se ainda irão chegar processos
            if(tempoAtual == len(self.filaChegada)):
                fimFila = True

            
            emMemoria = []
            #Alocação de memoria
            if(not fimFila and len(self.filaChegada[tempoAtual]) > 0): 
                for processoChegando in self.filaChegada[tempoAtual]:
                    if(self.memoria.firstFit(processoChegando)): #quando tem espaço
                        self.memoria.atualizaAlocacao()
                        emMemoria.insert(0,processoChegando)
                        reportChegada += str(processoChegando)
                    else: #quando não tem
                        if(tempoAtual+1 == len(self.filaChegada)):
                            self.filaChegada.append([])
                        self.filaChegada[tempoAtual+1].insert(0,processoChegando)

            #Registra memoria no inicio do clock    
            reportMemoriaInicio = str(self.memoria)
            #Registra estado dos perifericos no inicio do clock
            for p in self.lPerifericos:
                reportPerifericosInicio += str(p)
            
            #Bota processos que chegaram na fila 0
            self.escalonador.entradaPronto(emMemoria)

            reportFilas = self.escalonador.printa_filas()

            #Verifica se os perifericos foram liberados
            self.escalonador.verificaES(self.lPerifericos)

            #Trata a saida do processo da fila de prontos para o processador
            for n in range(len(self.escalonador.filas)):
                self.escalonador.saidaPronto(n ,self.lPerifericos)
            
            #Trata o processo dentro de cada cpu e registra o estado antes e depois do processamento
            for cpu in self.escalonador.cpus:
                reportCpuInicio += str(cpu)                
                cpu.processa(self.lPerifericos)
                reportCpuFinal += str(cpu)

            #Registra estado dos perifericos no fim do clock
            for p in self.lPerifericos:
                reportPerifericosFinal += str(p)
            
            #Remove os processos da memoria
            self.escalonador.retiraProcesso(self.memoria, self.lPerifericos)
            
            #Printa o clock
            print("########################################## TEMPO {} ##########################################\n".format(tempoAtual))
            if reportChegada != "":
                print("-----------------------------------Novos Processos-----------------------------------")
                print(reportChegada)
                print("-------------------------------------------------------------------------------------")
            else:
                print("-----------------------------------Não chegaram novos processos-----------------------------------")
            print("\n>>>> Inicio do clock:\n")
            print(reportFilas)
            print("\tPerifericos: {}\n".format(reportPerifericosInicio))
            print("\tProcessadores: {}\n".format(reportCpuInicio))
            print("\tMemoria: {}\n".format(reportMemoriaInicio))
            if self.escalonador.historicoClock != "":
                print(">>> Mudanças de estado:")
                print(self.escalonador.historicoClock)
            print(">>> Fim do clock:\n")
            print(self.escalonador.printa_filas())
            print("\tPerifericos: {}\n".format(reportPerifericosFinal))
            print("\tProcessadores: {}\n".format(reportCpuFinal))
            print("\tMemoria: {}\n".format(self.memoria))
            print()
            tempoAtual += 1

            #Reseta o historico de mudança dos processos
            self.escalonador.historicoClock = ""

            #Verifica se a fila acabou
            if fimFila:
                if(len(self.escalonador.filas[0]) + len(self.escalonador.filas[1]) + len(self.escalonador.filas[2]) != 0 ) : vazio=False
                else: vazio=True
                for cpu in self.escalonador.cpus:
                    if(cpu.processo != None):
                        vazio = False
                        break