class Processo(object):
    def __init__(self, nome, tempoProcesso, nImpressora, nDisco, tamanho):
        self.nome = nome
        self.estado = "novo"
        self.tempoProcesso = tempoProcesso
        self.tempoProcessado = 0
        self.nImpressora = nImpressora
        self.nDisco = nDisco
        self.tamanho = tamanho
    
    def recursosDisponiveis(self, lPerifericos):
        impressoras = 0
        discos = 0
        for p in lPerifericos:
            if(p.tipo == "impressora" and p.disponivel):
                impressoras += 1
            if(p.tipo == "disco" and p.disponivel):
                discos += 1
        if(impressoras < self.nImpressora or discos < self.nDisco):
            return False
        else:
            True
    
        