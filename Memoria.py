from BlocoDeMemoria import BlocoDeMemoria
from Processo import Processo
class Memoria:
    def __init__(self, tamanhoMaximo):
        self.listaDeBlocos = [BlocoDeMemoria(16000,None,True)]
        self.tamanhoAlocado = 0
        self.tamanhoMaximo = tamanhoMaximo

    def atualizaAlocacao(self):
        alocado = 0
        for i in self.listaDeBlocos:
            if not i.livre:
                alocado += i.tamanho
        self.tamanhoAlocado = alocado

    def firstFit(self,processo):
        if(self.tamanhoAlocado + processo.tamanho <= self.tamanhoMaximo):
            pos = 0
            for bloco in self.listaDeBlocos:
                if(bloco.livre):
                    if(bloco.tamanho > processo.tamanho):  #aloca o bloco em uma espaço livre gerando um espaço ocupado e outro livre
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
        aux = self.listaDeBlocos.copy()
        for b in aux:
            if(b.livre):
                self.listaDeBlocos.remove(b)
        self.atualizaAlocacao()
        
    def liberaBloco(self,processo):
        for bloco in self.listaDeBlocos:
            if(bloco.processo == processo):
                bloco.livre = True
        self.atualizaAlocacao()
    

    def __str__(self):
        esp = 0
        resp = "|"
        for i in self.listaDeBlocos:
            esp += i.tamanho 
            if i.livre:
                resp += " LIVRE - {}MB |".format(i.tamanho)
            else:
                resp += " {} - {}MB |".format(i.processo.nome, i.tamanho)
        if esp < self.tamanhoMaximo:
            resp += " LIVRE - {}MB |".format(self.tamanhoMaximo-esp)
        return resp 