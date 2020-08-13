from listaSimples.listasimples import ListaSimples

class Fila_lse:
    def __init__(self, valor):
        self.lista = ListaSimples(valor)

    def enfileirar(self, valor):
        if self.lista.cabeca is not None:
            self.lista.inserirFim(valor)
        else:
            self.lista.inserirInicio(valor)

    def desenfileirar(self):
        if self.lista.cauda is not None:
            self.lista.removerIndex(0)