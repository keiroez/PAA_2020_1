from activitys.activity_140820_aed.fila.fila_lse import Fila_lse

def imprimir(lista):
    x = lista.cabeca
    while x is not None:
        print(x.valor, end=" ")
        x = x.proximo
    print("")


def testeFila():
    fila = Fila_lse(1)      #Instanciando a fila com o valor inicial 1

    fila.enfileirar(22)
    fila.enfileirar(34)      #Enfileirando novos nós
    fila.enfileirar(45)
    fila.enfileirar(56)
    fila.enfileirar(3)
    fila.enfileirar(2)

    print("Fila Inicial:")
    imprimir(fila.lista)


    fila.desenfileirar()    #Desenfileirando duas vezes
    fila.desenfileirar()

    print("Fila após primeiro desenfileiramento")
    imprimir(fila.lista)

    fila.enfileirar(6)
    fila.enfileirar(7)      #Enfileirando novamente
    fila.enfileirar(88)
    fila.enfileirar(188)

    print("Novos elementos na fila")
    imprimir(fila.lista)

    fila.desenfileirar()
    fila.desenfileirar()    #Desenfileirando novamente
    fila.desenfileirar()
    fila.desenfileirar()

    print("Novo desenfileiramento")
    imprimir(fila.lista)
