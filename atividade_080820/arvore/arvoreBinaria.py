from arvore.no import No


class ArvoreBinaria:
    def __init__(self, valor):
        self.raiz = No(valor)


    def buscaABB(self, raiz, valor):
        if raiz is None or valor == raiz.valor:
            return raiz
        elif valor < raiz.valor:
            return self.buscaABB(raiz.esquerdo, valor)
        else:
            return self.buscaABB(raiz.direito, valor)

    def insereABB(self, raiz, no):
        if raiz is None:
            return no
        if no.valor < raiz.valor:
            raiz.esquerdo = self.insereABB(raiz.esquerdo, no)
        elif no.valor > raiz.valor:
            raiz.direito = self.insereABB(raiz.direito, no)
        return raiz

    def minimoABB(self, raiz):
        if raiz.esquerdo is not None:
            return self.minimoABB(raiz.esquerdo)
        return raiz

    def removeABB(self, raiz, valor):
        if raiz is None:
            return None

        if valor < raiz.valor:
            raiz.esquerdo = self.removeABB(raiz.esquerdo, valor)
        elif valor > raiz.valor:
            raiz.direito = self.removeABB(raiz.direito, valor)
        else:
            if raiz.esquerdo is None:
                raiz = raiz.direito
            elif raiz.direito is None:
                raiz = raiz.esquerdo
            else:
                minimo = self.minimoABB(raiz.direito)
                raiz.valor = minimo.valor
                raiz.direito = self.removeABB(raiz.direito, minimo.valor)
        return raiz
