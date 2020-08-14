from listaSimples.listasimples import ListaSimples

class Fila_lse:
    def __init__(self, valor):              #Construtor iniciando lista com um valor
        self.lista = ListaSimples(valor)    #Atributo lista do tipo LSE recebendo o valor com parametro

    def enfileirar(self, valor):            #Método para enfileirar na fila
        if self.lista.cabeca is not None:   #Verifica se a lista possui cabeça
            self.lista.inserirFim(valor)    #Insere um novo nó no final da fila
        else:                               #Verifica se a lista não possui cabeça
            self.lista.inserirInicio(valor) #Enfileira o nó na cabeça da lista

    def desenfileirar(self):                #Método para desinfileirar da fila
        if self.lista.cauda is not None:    #Verifica se a cauda não é nula
            self.lista.removerIndex(0)      #Remove o índice 0 da lista, que é sua cabeça