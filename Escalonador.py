class Escalonador(object):
    def __init__(self, cpus):
        self.filaPronto = []
        self.filaSusImpressora = []
        self.filaSusDisco = []
        self.cpus = cpus

    def executa(self, lPerifericos):
        p = self.filaPronto.pop()
        for cpu in cpus:
            if not p.prioridade and p.tempoProcesso - p.tempoProcessado <=2:
                if p.recursosDisponiveis(lPerifericos) == "pronto":
                    if cpu.processo == None:
                        cpu.processa(p)
                        p = self.filaPronto.pop()
                    else:
                        continue
                elif p.recursosDisponiveis(lPerifericos) == "semDisco ":
                    p.bloqueia()
                    self.filaSusDisco.append(p)
                    p = self.filaPronto.pop()
                elif p.recursosDisponiveis(lPerifericos) == "semImpressora":
                    p.bloqueia()
                    self.filaSusImpressora.append(p)
                    p = self.filaPronto.pop()
            else:
                if cpu.processo == None:
                        cpu.processa(p)
                        p = self.filaPronto.pop()
                else:
                    continue
    
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
            
        
            



