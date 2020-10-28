class Escalonador(object):
    def __init__(self, cpus):
        self.filaPronto = []
        self.filaSusImpressora = []
        self.filaSusDisco = []
        self.cpus = cpus

    def executa(self, lPerifericos):
        p = self.filaPronto.pop()
        for cpu in cpus:
            if p.recursosDisponiveis(lPerifericos):
                if cpu.processo == None:
                    cpu.processa(p)
                    p = self.filaPronto.pop()
            else:
                p.bloqueia()
                self.filaSusImpressora.append(p)
                p = self.filaPronto.pop()

