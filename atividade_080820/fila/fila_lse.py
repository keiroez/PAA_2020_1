from listaSimples.listasimples import ListaSimples

class Fila_lse: #Classe fila com lista simplesmente encadeada
    def __init__(self, valor): #Construtor iniciando lista com um valor
        self.lista = ListaSimples(valor) #Atributo lista do tipo LSE recebendo o valor com parametro

    def enfileirar(self, valor): #Método para enfileirar na fila
        if self.lista.cabeca is not None: #Se a lista possuir cabeça
            self.lista.inserirFim(valor) #é inserido um novo nó no final da fila
        else: #Se a lista não possuir cabeça, então
            self.lista.inserirInicio(valor) # O nó é enfileirado na cabeça da lista

    def desenfileirar(self): #Método para desinfileirar da fila
        if self.lista.cauda is not None: #Se a cauda não for nula, então
            self.lista.removerIndex(0) #é removido o índice 0 da lista, que é sua cabeça