class Periferico(object):
    def __init__(self, disponivel, tipo, nome):
        self.nome = nome
        self.disponivel = True
        self.tipo = tipo
    
    def __str__(self):
        if self.disponivel:
            aux = "Disponivel"
        else:
            aux = "Em uso"
        return "\t| {} {}({}) |".format(self.tipo.title(), self.nome, aux)

