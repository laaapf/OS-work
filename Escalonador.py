class Escalonador(object):
    def __init__(self, cpus):
        self.filaPronto = []
        self.filaSusImpressora = []
        self.filaSusDisco = []
        self.cpus = cpus

    def retiraPronto(self, lPerifericos): #manda de pronto ao processador ou para bloqueado
        for cpu in self.cpus:   #percorrer as cpus
            if (cpu.processo != None): #caso a cpu esteja ocupada
                continue
            if (len(self.filaPronto) == 0): #não tem mais processos
                return
            p = self.filaPronto.pop()
            if not p.prioridade:
                if p.recursosDisponiveis(lPerifericos) == "semDisco " and p.tempoProcessado == 0: #envia p fila de bloq disco
                    p.bloqueia()
                    self.filaSusDisco.append(p)
                elif p.recursosDisponiveis(lPerifericos) == "semImpressora" and p.tempoProcesso - p.tempoProcessado <=2:    #envia p fila de bloq impressora
                    p.bloqueia()
                    self.filaSusImpressora.append(p)
                elif p.recursosDisponiveis(lPerifericos) == "pronto":   #envia ao processador
                    self.reservaES(p,lPerifericos)  #reserva entrada e saida na hora de enviar ao processador (rever classe da função)
                    cpu.processo = p
            else:
                cpu.processo = p
            if len(self.filaPronto) == 0:
                return

    def reservaES(self,p,lPerifericos):
        i = p.nImpressora
        while (i > 0) :
            for periferico in lPerifericos:
                if(periferico.tipo == "impressora" and periferico.disponivel):
                    periferico.disponivel = False
                    i-=1
        i = p.nDisco
        while (i > 0) :
            for periferico in lPerifericos:
                if(periferico.tipo == "disco" and periferico.disponivel):
                    periferico.disponivel = False
                    i-=1

    # def executa(self, lPerifericos):
    #     p = self.filaPronto.pop()
    #     for cpu in self.cpus:
    #         if not p.prioridade:
    #             if p.recursosDisponiveis(lPerifericos) == "semDisco " and p.tempoProcessado == 0:
    #                 p.bloqueia()
    #                 self.filaSusDisco.append(p)
    #                 if(len(self.filaPronto)!=0):
    #                     p = self.filaPronto.pop()
    #                 else:
    #                     return
    #             elif p.recursosDisponiveis(lPerifericos) == "semImpressora" and p.tempoProcesso - p.tempoProcessado <=2:
    #                 p.bloqueia()
    #                 self.filaSusImpressora.append(p)
    #                 if(len(self.filaPronto)!=0):
    #                     p = self.filaPronto.pop()
    #                 else:
    #                     return
    #             elif p.recursosDisponiveis(lPerifericos) == "pronto":
    #                 if cpu.processo == None:
    #                     cpu.processa(p,lPerifericos)
    #                     if(len(self.filaPronto)!=0):
    #                         p = self.filaPronto.pop()
    #                     else:
    #                         return
    #                 else:
    #                     continue
    #         else:
    #             if cpu.processo == None:
    #                     cpu.processa(p,lPerifericos)
    #                     if(len(self.filaPronto)!=0):
    #                         p = self.filaPronto.pop()
    #                     else:
    #                         return
    #             else:
    #                 continue
    
    def att_pronto(self, processos, lPerifericos):
        for p in processos:
            self.filaPronto.append(p)
        for i in lPerifericos:
            if i.disponivel:
                if i.tipo == "disco":
                    while len(self.filaSusDisco) != 0:
                        self.filaPronto.insert(0, self.filaSusDisco.pop())
                elif i.tipo == "impressora":
                    while len(self.filaSusImpressora) != 0:
                        self.filaPronto.insert(0, self.filaSusImpressora.pop())

    def retiraProcesso(self,memoria):
        for cpu in self.cpus:
            if(cpu.processo != None):
                if(cpu.processo.prioridade == False):
                    if(cpu.processo.tempoProcessado == cpu.processo.tempoProcesso):
                        memoria.liberaBloco(cpu.processo)
                        cpu.processo.termina()
                        cpu.processo = None

                    elif((cpu.processo.tempoProcessado % 2) == 0):
                        self.filaPronto.append(cpu.processo)
                        cpu.processo = None
                else:
                    if(cpu.processo.tempoProcessado == cpu.processo.tempoProcesso):
                        memoria.liberaBloco(cpu.processo)
                        cpu.processo.termina()
                        cpu.processo = None