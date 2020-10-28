class Processador:
    def __init__(self, processo):
        self.processo = processo
    
    def getProcesso(self):
        return self.processo

    def contadorTempo(self):
        self.processo.tempoProcessado += 1