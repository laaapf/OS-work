
class Processador:
    def __init__(self):
        self.processo = None
        self.filaAtendida = None
    
    def __str__(self):
        if(self.processo == None):
            return "| Cpu Ociosa |\t"
        else:
            return "| {}: Executado:{}/{} |\t".format(self.processo.nome,self.processo.tempoProcessado, self.processo.tempoProcesso)

    def processa(self,lPerifericos):
        if(self.processo == None):
            return
        self.processo.tempoProcessado += 1
