class Escalonador(object):
    def __init__(self, cpus):
        self.filas = [[],[],[]]
        self.cpus = cpus
        self.historicoClock = ""


    def saidaPronto(self,n ,lPerifericos): #manda de pronto ao processador ou para bloqueado
        if n < 2:
            fila = n+1
        else:
            fila = n
        for cpu in self.cpus:   #percorrer as cpus
            if (cpu.processo != None): #caso a cpu esteja ocupada
                continue
            if (len(self.filas[n]) == 0): #não tem mais processos
                return
            p = self.filas[n].pop()
            if not p.prioridade:
                if p.estado != "bloqueado":
                    rDisp = p.recursosDisponiveis(lPerifericos)
                    if rDisp == "semDisco":
                        if  p.tempoProcessado == 0: #envia p fila de bloq disco
                            self.historicoClock += p.bloqueia()
                            self.filas[fila].insert(0,p)
                        else:
                            rDisp = "pronto"
                    elif rDisp == "semImpressora":
                        if p.tempoProcesso - p.tempoProcessado <=2:    #envia p fila de bloq impressora
                            self.historicoClock += p.bloqueia()
                            self.filas[fila].insert(0,p)
                        else:
                            rDisp = "pronto"
                    if rDisp == "pronto":   #envia ao processador
                        p.reservaES(lPerifericos)  #reserva entrada e saida na hora de enviar ao processador (rever classe da função)
                        self.historicoClock += p.executa()
                        cpu.processo = p
                        cpu.filaAtendida = n
                else:
                    self.filas[n].insert(0,p)
            else:
                cpu.processo = p
                cpu.filaAtendida = n
                self.historicoClock += p.executa()
            if len(self.filas[n]) == 0:
                return

    def entradaPronto(self, processos):
        for p in processos:
            self.filas[0].append(p)

    def verificaES(self, lPerifericos):
        nImpressora = 0
        nDisco = 0
        for periferico in lPerifericos:
            if periferico.disponivel:
                if periferico.tipo == "impressora":
                    nImpressora +=1
                else:
                    nDisco += 1
        
        for fila in self.filas:
            for processo in fila:
                if processo.estado == "bloqueado" and (processo.nImpressora <= nImpressora and processo.nDisco <= nDisco):
                     self.historicoClock += processo.apronta()



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
                        cpu.filaAtendida = None

                    elif((cpu.processo.tempoProcessado % 2) == 0):
                        self.historicoClock += cpu.processo.apronta()
                        if cpu.processo.tempoProcessado == 2:
                            cpu.processo.liberaES(cpu.processo.nDisco, "disco",lPerifericos)
                        if cpu.filaAtendida < 2:                       
                            self.filas[cpu.filaAtendida+1].insert(0,cpu.processo)
                        else:
                            self.filas[cpu.filaAtendida].insert(0,cpu.processo)
                        cpu.filaAtendida = None
                        cpu.processo = None
                else:
                    if(cpu.processo.tempoProcessado == cpu.processo.tempoProcesso):
                        memoria.liberaBloco(cpu.processo)
                        self.historicoClock += cpu.processo.termina()
                        cpu.processo = None
                        cpu.filaAtendida = None

    def printa_filas(self):
        resp = ""
        for i in range(len(self.filas)):
            aux = "\tfila {}: ".format(i)
            for j in range(len(self.filas[i])-1, -1,-1):
                aux += "{} ".format(self.filas[i][j].nome)
            resp = resp + aux + "\n"
        return resp