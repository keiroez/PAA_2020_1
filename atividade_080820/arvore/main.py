from arvore.arvoreBinaria import ArvoreBinaria, No

ab = ArvoreBinaria(10)

ab.insereABB(ab.raiz, No(5))
ab.insereABB(ab.raiz, No(15))
ab.insereABB(ab.raiz, No(13))
ab.insereABB(ab.raiz, No(11))
ab.insereABB(ab.raiz, No(1))
ab.insereABB(ab.raiz, No(3))
ab.insereABB(ab.raiz, No(100))
ab.insereABB(ab.raiz, No(84))

def imprimir(raiz):
    while raiz is not None:
        print(raiz.valor)
        raiz = raiz.esquerdo

def mostrar(nivel=1,noArvore=None):
        if (noArvore is None):
            noArvore = ab.raiz
        arrow = "---" * nivel
        print ("|%s>%s" % (arrow, noArvore.valor))
        if (noArvore.esquerdo is not None):
            mostrar(nivel+1,noArvore.esquerdo)
        if (noArvore.direito is not None):
            mostrar(nivel+1,noArvore.direito)

mostrar()


# print(ab.buscaABB(ab.raiz, 15))
ab.removeABB(ab.raiz, 5)

print("=====================")
mostrar()

# print(ab.raiz.esquerdo.valor)
# print(ab.raiz.direito.valor)
# print(ab.raiz.direito.esquerdo)



