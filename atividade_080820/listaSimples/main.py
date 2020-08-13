from listaSimples.listasimples import ListaSimples

def imprimir(lista):
    x = lista.cabeca
    while x is not None:
        print(x.valor)
        x = x.proximo

values = [10, 30, 20, 50, 60,76, 54, 100, 99, 110]


lista = ListaSimples(1)

for v in values:
    lista.inserirFim(v)


print("Lista Inicial:")
imprimir(lista)


print("#########################################")
lista.removerValor(54)
lista.removerValor(100)
lista.removerValor(20)
print("Lista após remover valores:")
imprimir(lista)

print("#########################################")
lista.removerIndex(2)
print("Lista após remover indices:")
imprimir(lista)
