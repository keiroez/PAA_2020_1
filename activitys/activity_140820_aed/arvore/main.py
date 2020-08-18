from activitys.activity_140820_aed.arvore.arvoreBinaria import ArvoreBinaria, No


def mostrar(nivel=1,noArvore=None, ab=None):
        if (noArvore is None):
            noArvore = ab.raiz
        arrow = "---" * nivel
        print ("|%s>%s" % (arrow, noArvore.valor))
        if (noArvore.esquerdo is not None):
            mostrar(nivel+1,noArvore.esquerdo)
        if (noArvore.direito is not None):
            mostrar(nivel+1,noArvore.direito)

def testeArvore():
    ab = ArvoreBinaria(10)  #Instanciando a arvore com a raiz tendo valor 10

    ab.insereABB(ab.raiz, No(5))
    ab.insereABB(ab.raiz, No(15))
    ab.insereABB(ab.raiz, No(13))
    ab.insereABB(ab.raiz, No(11))   #Inserindo novos nós na arvores
    ab.insereABB(ab.raiz, No(111))
    ab.insereABB(ab.raiz, No(3))
    ab.insereABB(ab.raiz, No(100))
    ab.insereABB(ab.raiz, No(84))

    print("Valores inicias na arvore:")
    mostrar(ab=ab)
    print()

    print("Buscando valor 15 na arvore:")
    print(ab.buscaABB(ab.raiz, 15))
    print()                                     #Teste de busca
    print("Buscando valor 101 na arvore:")
    print(ab.buscaABB(ab.raiz, 101))
    print()

    ab.removeABB(ab.raiz, 5)
    ab.removeABB(ab.raiz, 11)                   #Teste de remoção
    ab.removeABB(ab.raiz, 3)
    print("Aŕvore com elementos Removidos")
    mostrar(ab=ab)
    print()

    ab.insereABB(ab.raiz, No(555))
    ab.insereABB(ab.raiz, No(104))              #Inserindo novos elementos
    ab.insereABB(ab.raiz, No(432))
    ab.insereABB(ab.raiz, No(7))
    ab.insereABB(ab.raiz, No(9))
    print("Árvore com novos elementos")
    mostrar(ab=ab)
    print()

    print("Menor valor: " + str(ab.menorValor(ab.raiz).valor))
    print("Maior valor: " + str(ab.maiorValor(ab.raiz).valor))
    print("Sucessor: " + str(ab.sucessor(ab.raiz).valor))
    print("Predecessor: " + str(ab.predecessor(ab.raiz).valor))

