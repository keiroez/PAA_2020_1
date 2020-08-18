from activitys.activity_140820_aed.listaSimples.listasimples import ListaSimples

def imprimir(lista):
    x = lista.cabeca
    while x is not None:
        print(x.valor, end=" ")
        x = x.proximo
    print("")

def testeListaSimples():
    values = [10, 30, 20, 50, 60,76, 54, 100, 99, 110]
    lista = ListaSimples(1)     #Instanciando lista com o valor 1 no primeiro nó

    for v in values:
        lista.inserirFim(v)     #Adicionando os valores do vetor em nós no fim da lista

    print("Lista Inicial:")
    imprimir(lista)             #Imprime a lista inicial


    lista.inserirInicio(14)
    lista.inserirInicio(78)     #Inserindo novos nós no inicio da lista
    lista.inserirInicio(440)
    print("Lista após inserir no inicio:")
    imprimir(lista)

    lista.removerValor(54)
    lista.removerValor(100)     #Removendo valores na lista
    lista.removerValor(20)
    print("Lista após remover valores:")
    imprimir(lista)

    lista.removerIndex(2)       #Removendo indices da lista
    lista.removerIndex(0)
    lista.removerIndex(4)
    print("Lista após remover indices:")
    imprimir(lista)

    print("Buscando valores")
    print(lista.buscarNaLista(99))
    print(lista.buscarNaLista(50))
