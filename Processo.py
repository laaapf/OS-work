class Processo(object):
    def __init__(self, nome, prioridade, tempoProcesso, nImpressora, nDisco, tamanho):
        self.nome = nome
        self.prioridade = prioridade
        self.estado = "pronto"
        self.tempoProcesso = tempoProcesso
        self.tempoProcessado = 0
        self.nImpressora = nImpressora
        self.nDisco = nDisco
        self.tamanho = tamanho

    
    def bloqueia(self):
        self.estado = "bloqueado"

    def apronta(self):
        self.estado = "pronto"    


    
        