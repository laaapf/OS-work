class Processador:
    def __init__(self):
        self.processo = None
        self.clock = 0
    
    def getProcesso(self):
        return self.processo

    def processa(self,p):
        self.processo = p
        self.clock += 1
        self.processo.tempoProcessado += 1
