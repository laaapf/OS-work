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

    def __str__(self):
        return "\tProcesso {}   Estado {}   Prioridade {}\n\tTamanho do Processo:{}Mbytes\n\tProcessado:{}/{}".format(self.nome, self.estado, self.prioridade, self.tamanho, self.tempoProcessado, self.tempoProcesso)
    
    def recursosDisponiveis(self, lPerifericos,):
        impressoras = 0
        discos = 0
        for p in lPerifericos:
            if(p.tipo == "impressora" and p.disponivel):
                impressoras += 1
            if(p.tipo == "disco" and p.disponivel):
                discos += 1
        if(impressoras < self.nImpressora):
            return "semImpressora"
        else: 
            if (discos < self.nDisco):
                return "semDisco"
            else:
                return "pronto"
    def bloqueia(self):
        estadoAntigo = self.estado
        self.estado = "bloqueado"
        print("\tProcesso {}   Estado {} --> Bloqueado".format(self.nome, estadoAntigo))

    def apronta(self):
        estadoAntigo = self.estado
        self.estado = "pronto"   
        print("\tProcesso {}   Estado {} --> Pronto".format(self.nome, estadoAntigo))
