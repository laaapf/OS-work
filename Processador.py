
class Processador:
    def __init__(self):
        self.processo = None
        self.filaAtendida = None
    
    def __str__(self):
        if(self.processo == None):
            return "Cpu Ociosa\t"
        else:
            return "{}  Executado:{}/{}\t".format(self.processo.nome,self.processo.tempoProcessado, self.processo.tempoProcesso)

    def processa(self,lPerifericos):
        if(self.processo == None):
            return
        self.processo.tempoProcessado += 1

    # def processa(self,p,lPerifericos):
    #     self.processo = p
    #     self.processo.tempoProcessado += 1
    #     print(self.processo)
    #     i = p.nImpressora
    #     while (i > 0) :
    #         for periferico in lPerifericos:
    #             if(periferico.tipo == "impressora" and periferico.disponivel):
    #                 periferico.disponivel = False
    #                 i-=1
    #     i = p.nDisco
    #     while (i > 0) :
    #         for periferico in lPerifericos:
    #             if(periferico.tipo == "disco" and periferico.disponivel):
    #                 periferico.disponivel = False
    #                 i-=1