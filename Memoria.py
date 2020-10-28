from BlocoDeMemoria import BlocoDeMemoria
from Processo import Processo
class Memoria:
    def __init__(self, listaDeBlocos, tamanhoAlocado, tamanhoMaximo):
        self.listaDeBlocos = listaDeBlocos
        self.tamanhoAlocado = tamanhoAlocado
        self.tamanhoMaximo = tamanhoMaximo

    def atualizaAlocacao(self):
        alocado = 0
        for i in self.listaDeBlocos:
            alocado += i.tamanho
        self.tamanhoAlocado = alocado

    def firstFit(self,processo):
        if(self.tamanhoAlocado + processo.tamanho <= self.tamanhoMaximo):
            pos = 0
            for bloco in self.listaDeBlocos:
                if(bloco.livre):
                    if(bloco.tamanho < processo.tamanho):  #aloca o bloco em uma espaço livre gerando um espaço ocupado e outro livre
                        bloco.tamanho -= processo.tamanho
                        self.listaDeBlocos.insert(pos,BlocoDeMemoria(processo.tamanho, processo, False))
                        return True
                    if(bloco.tamanho == processo.tamanho):   #o bloco encaixa exatamente no espaço livre
                        bloco.livre = False
                        bloco.processo = processo
                        return True
                pos += 1
            self.garbageCollector()
            self.listaDeBlocos.append(BlocoDeMemoria(processo.tamanho, processo, False))
            return True
        else:
            return False

    def garbageCollector(self):
        for b in self.listaDeBlocos:
            if(b.livre):
                self.listaDeBlocos.remove()
        self.atualizaAlocacao()
        