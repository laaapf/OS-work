class Processo(object):
    def __init__(self, nome, tempoProcesso, nImpressora, nDisco, tamanho):
        self.nome = nome
        self.estado = "novo"
        self.tempoProcesso = tempoProcesso
        self.tempoProcessado = 0
        self.nImpressora = nImpressora
        self.nDisco = nDisco
        self.tamanho = tamanho
    


    
        