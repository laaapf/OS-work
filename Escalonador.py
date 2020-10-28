class Escalonador(object):
    def __init__(self, cpus):
        self.filaPronto = []
        self.filaSusImpressora = []
        self.filaSusDisco = []
        self.cpus = cpus

    def executa(self, lPerifericos):
        p = self.filaPronto.pop()
        for cpu in cpus:
            if not p.prioridade:
                if p.recursosDisponiveis(lPerifericos) == "semDisco " and p.tempoProcessado == 0:
                    p.bloqueia()
                    self.filaSusDisco.append(p)
                    p = self.filaPronto.pop()
                elif p.recursosDisponiveis(lPerifericos) == "semImpressora" and p.tempoProcesso - p.tempoProcessado <=2:
                    p.bloqueia()
                    self.filaSusImpressora.append(p)
                    p = self.filaPronto.pop()
                elif p.recursosDisponiveis(lPerifericos) == "pronto":
                    if cpu.processo == None:
                        cpu.processa(p)
                        p = self.filaPronto.pop()
                    else:
                        continue
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
            
        
            



    def retiraProcesso(self, cpus):
        for cpu in cpus:
            if(cpu.processo.prioridade == False):
                if(cpu.processo.tempoProcessado == cpu.processo.tempoProcesso and cpu.processo):
                    cpu.processo = None
                elif((cpu.processo.tempoProcessado % 2) == 0 and cpu.processo):
                    cpu.processo = None
            else:
                if(cpu.processo.tempoProcessado == cpu.processo.tempoProcesso and cpu.processo):
                    cpu.processo = None