
class Processador:
    def __init__(self):
        self.processo = None
    
    def getProcesso(self):
        return self.processo

    def processa(self,p,lPerifericos):
        self.processo = p
        self.processo.tempoProcessado += 1
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