class Escalonador(object):
    def __init__(self, cpus):
        self.filaPronto = []
        self.filaSusImpressora = []
        self.filaSusDisco = []
        self.cpus = cpus
        self.historicoClock = ""


    def saidaPronto(self, lPerifericos): #manda de pronto ao processador ou para bloqueado
        for cpu in self.cpus:   #percorrer as cpus
            if (cpu.processo != None): #caso a cpu esteja ocupada
                continue
            if (len(self.filaPronto) == 0): #não tem mais processos
                return
            p = self.filaPronto.pop()
            if not p.prioridade:
                rDisp = p.recursosDisponiveis(lPerifericos)
                if rDisp == "semDisco":
                    if  p.tempoProcessado == 0: #envia p fila de bloq disco
                        self.historicoClock += p.bloqueia()
                        self.filaSusDisco.append(p)
                    else:
                        rDisp = "pronto"
                elif rDisp == "semImpressora":
                    if p.tempoProcesso - p.tempoProcessado <=2:    #envia p fila de bloq impressora
                        self.historicoClock += p.bloqueia()
                        self.filaSusImpressora.append(p)
                    else:
                        rDisp = "pronto"
                if rDisp == "pronto":   #envia ao processador
                    p.reservaES(lPerifericos)  #reserva entrada e saida na hora de enviar ao processador (rever classe da função)
                    self.historicoClock += p.executa()
                    cpu.processo = p
            else:
                cpu.processo = p
            if len(self.filaPronto) == 0:
                return

    def entradaPronto(self, processos, lPerifericos):
        for p in processos:
            self.filaPronto.append(p)
        for i in lPerifericos:
            if i.disponivel:
                if i.tipo == "disco":
                    while len(self.filaSusDisco) != 0:
                        p = self.filaSusDisco.pop()
                        self.historicoClock += p.apronta()
                        self.filaPronto.insert(0, p)
                elif i.tipo == "impressora":
                    while len(self.filaSusImpressora) != 0:
                        p = self.filaSusImpressora.pop()
                        self.historicoClock += p.apronta()
                        self.filaPronto.insert(0, p)

    def retiraProcesso(self,memoria, lPerifericos):
        for cpu in self.cpus:
            if(cpu.processo != None):
                if(cpu.processo.prioridade == False):
                    if(cpu.processo.tempoProcessado == cpu.processo.tempoProcesso):
                        memoria.liberaBloco(cpu.processo)
                        self.historicoClock += cpu.processo.termina()
                        if cpu.processo.tempoProcessado == 2:
                            cpu.processo.liberaES(cpu.processo.nDisco, "disco",lPerifericos)
                        cpu.processo.liberaES(cpu.processo.nImpressora, "impressora",lPerifericos)
                        cpu.processo = None

                    elif((cpu.processo.tempoProcessado % 2) == 0):
                        self.historicoClock += cpu.processo.apronta()
                        if cpu.processo.tempoProcessado == 2:
                            cpu.processo.liberaES(cpu.processo.nDisco, "disco",lPerifericos)
                        self.filaPronto.append(cpu.processo)
                        cpu.processo = None
                else:
                    if(cpu.processo.tempoProcessado == cpu.processo.tempoProcesso):
                        memoria.liberaBloco(cpu.processo)
                        self.historicoClock += cpu.processo.termina()
                        cpu.processo = None