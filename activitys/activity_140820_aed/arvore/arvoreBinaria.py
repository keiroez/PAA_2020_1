from activitys.activity_140820_aed.arvore.no import No


class ArvoreBinaria:
    def __init__(self, valor):                  #Construtor com valor do nó como parametro
        self.raiz = No(valor)                   #Instanciando o nó raiz da árvore com o valor inicial

    def buscaABB(self, raiz, valor):
        if raiz is None or valor == raiz.valor:         # Verifica se a raiz atual é nula ou se o valor buscado é o valor da raiz atual
            if raiz is not None:
                return str(raiz.valor)+" encontrado"                                 # Retorna a raiz atual
            else:
                return "Não encontrado"
        elif valor < raiz.valor:                        # Verifica se o valor buscado é menor que o valor da raiz atual
            return self.buscaABB(raiz.esquerdo, valor)  #Executa e retorna uma recursão enviando o filho esquerdo
        else:                                           #Verifica se o valor buscado é maior que o valor da raiz atual
            return self.buscaABB(raiz.direito, valor)   #Executa e retorna uma recursão enviando o filho direito

    def insereABB(self, raiz, no):
        if raiz is None:                                # Verifica se a raiz atual é nula
            return no                                   # Retorna o novo nó
        if no.valor < raiz.valor:                       # Verifica se o valor do novo nó é menor que o valor da raiz atual
            raiz.esquerdo = self.insereABB(raiz.esquerdo, no)   #O filho esquerdo passa a ser o retorno da recursão enviando o filho esquerdo
        elif no.valor > raiz.valor:                             #Verifica se o valor do novo nó é maior que o valor da raiz atual
            raiz.direito = self.insereABB(raiz.direito, no)     #O filho direito passa a ser o retorno da recursão enviando o filho direito
        return raiz                                             # Por fim, retorna-se a raiz atual

    def minimoABB(self, raiz):
        if raiz.esquerdo is not None:               #Verifica se o filho esquerdo da raiz atual não é nulo
            return self.minimoABB(raiz.esquerdo)    #Retorna a recursão enviando o filho esquerdo
        return raiz                 # Por fim, retorna-se a raiz atual

    def maximoABB(self, raiz):
        if raiz.direito is not None:            # Verifica se o filho direito da raiz atual não é nulo
            return self.maximoABB(raiz.direito) #Retorna a recursão enviando o filho direito
        return raiz                 # Por fim, retorna-se a raiz atual

    def removeABB(self, raiz, valor):
        if raiz is None:        # Verifica se a raiz atual não é nula
            return None         # Retorna nulo

        if valor < raiz.valor:      # Verifica se o valor buscado é menor que o valor da raiz atual
            raiz.esquerdo = self.removeABB(raiz.esquerdo, valor)    #O filho esquerdo passa a ser o retorno da recursão enviando a si mesmo como raiz
        elif valor > raiz.valor:    # Verifica se o valor buscado é maior que o valor da raiz atual
            raiz.direito = self.removeABB(raiz.direito, valor)      #O filho direito passa a ser o retorno da recursão enviando a si mesmo como raiz
        else:                       #Verifica se o valor buscado é igual ao valor da raiz
            if raiz.esquerdo is None:   # Verifica se o filho esquerdo é nulo
                raiz = raiz.direito     # A raiz passa a ser o filho direito
            elif raiz.direito is None:  # Verifica se o filho direito é nulo
                raiz = raiz.esquerdo    # A raiz passa a ser o filho esquerdo
            else:                       # Verifica se os filhos esquerdo e direito são nulos
                minimo = self.minimoABB(raiz.direito)   # Busca o menor valor a partir do filho direito
                raiz.valor = minimo.valor               # Altera o valor da raiz atual para o valor minimo
                raiz.direito = self.removeABB(raiz.direito, minimo.valor)   #O filho direito passa a ser o retorno da recurso enviando a si mesmo como parametro e o nó com menor valor
        return raiz     # Retorna a raiz atual

    def menorValor(self, raiz): # Método para retornar o menor valor a partir de tal raiz
        return self.minimoABB(raiz)

    def maiorValor(self, raiz): # Método para retornar o maior valor a partir de tal raiz
        return self.maximoABB(raiz)

    def sucessor(self, raiz): # Método para retornar o valor sucessor a partir do valor de tal raiz
        if raiz.direito is not None:
            return self.minimoABB(raiz.direito)
        else:
            return raiz

    def predecessor(self, raiz): # Método para retornar o valor predecessor a partir do valor de tal raiz
        if raiz.esquerdo is not None:
            return self.maximoABB(raiz.esquerdo)
        else:
            return raiz