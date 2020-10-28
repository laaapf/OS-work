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
    

    def retiraProcesso(self, cpus):
        for cpu in cpus:
            if(cpu.processo.tempoProcessado == cpu.processo.tempoProcesso):
                cpu.processo = None
                continue
            if((cpu.processo.tempoProcessado % 2) == 0):
                cpu.processo = None
                continue