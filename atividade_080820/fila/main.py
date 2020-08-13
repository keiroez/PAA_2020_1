from fila.fila_lse import Fila_lse

def imprimir(lista):
    x = lista.cabeca
    while x is not None:
        print(x.valor)
        x = x.proximo

fila = Fila_lse(1)

fila.enfileirar(2)
fila.enfileirar(3)
fila.enfileirar(4)
fila.enfileirar(5)

imprimir(fila.lista)
print("############################")

fila.desenfileirar()
fila.desenfileirar()

imprimir(fila.lista)
print("############################")

fila.enfileirar(6)
fila.enfileirar(7)
fila.enfileirar(8)

imprimir(fila.lista)
print("############################")

