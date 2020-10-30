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
        while not vazio:
            reportChegada = ""

            if(tempoAtual == len(self.filaChegada)):
                fimFila = True

            emMemoria = []
            print("########################################## TEMPO {} ##########################################\n".format(tempoAtual))
            if(not fimFila and len(self.filaChegada[tempoAtual]) > 0): 
                for processoChegando in self.filaChegada[tempoAtual]:
                    if(self.memoria.firstFit(processoChegando)): #quando tem espaço
                        self.memoria.atualizaAlocacao()
                        emMemoria.append(processoChegando)
                        reportChegada += str(processoChegando)
                    else: #quando não tem
                        if(tempoAtual+1 == len(self.filaChegada)):
                            self.filaChegada.append([])
                        self.filaChegada[tempoAtual+1].insert(0,processoChegando)

                
            reportPerifericos = ""
            for p in self.lPerifericos:
                reportPerifericos += str(p)
            self.escalonador.entradaPronto(emMemoria,self.lPerifericos)
            self.escalonador.saidaPronto(self.lPerifericos)
            

            reportCpuInicio = ""
            reportMemoriaInicio = str(self.memoria)
            reportCpuFinal = ""
            for cpu in self.escalonador.cpus:
                reportCpuInicio += str(cpu)                
                cpu.processa(self.lPerifericos)
                reportCpuFinal += str(cpu)
            self.escalonador.retiraProcesso(self.memoria, self.lPerifericos)
            
            if reportChegada != "":
                print("-----------------------------------Novos Processos-----------------------------------")
                print(reportChegada)
                print("-------------------------------------------------------------------------------------")
            else:
                print("-----------------------------------Não chegaram novos processos-----------------------------------")
            print("\nInicio do clock:")
            print("\tProcessadores:{}\n\n\tMemoria:{}\n".format(reportCpuInicio, reportMemoriaInicio))
            if self.escalonador.historicoClock != "":
                print("Mudanças de estado")
                print("{}".format(self.escalonador.historicoClock))
            print("Perifericos:")
            print("{}\n".format(reportPerifericos))
            print("Fim do clock:")
            print("\tProcessadores:{}\n\n\tMemoria:{}".format(reportCpuFinal, self.memoria))
            print()
            tempoAtual += 1

            self.escalonador.historicoClock = ""
            if fimFila:
                if(len(self.escalonador.filaPronto) + len(self.escalonador.filaSusDisco) + len(self.escalonador.filaSusImpressora) != 0 ) : vazio=False
                else: vazio=True
                for cpu in self.escalonador.cpus:
                    if(cpu.processo != None):
                        vazio = False
                        break