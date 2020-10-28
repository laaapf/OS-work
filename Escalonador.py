class Escalonador(object):
    def __init__(self):
        self.filaPronto = []
        self.filaSusImpressora = []
        self.filaSusDisco = []
        self.cpus = []

    def chegada(self, filaChegada):
        self.filaPronto = filaChegada.copy()
    
    def 
