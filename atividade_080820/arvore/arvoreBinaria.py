from arvore.no import No


class ArvoreBinaria: # Classe da árvore binária de busca
    def __init__(self, valor): #Construtor com valor do nó como parametro
        self.raiz = No(valor) # Instanciando o nó raiz da árvore com o valor inicial

    def buscaABB(self, raiz, valor): #Método para buscar valor na árvore
        # Se a raiz atual não for nulo ou o valor buscado não for igual ao valor da raiz atual
        if raiz is None or valor == raiz.valor:
            return raiz # Retorna a raiz atual
        elif valor < raiz.valor: # Senão se o valor buscado for menor que o valor da raiz atual
            # Retorna o resultado de uma recursão para o mesmo método enviando o filho esquerdo da raiz atual
            return self.buscaABB(raiz.esquerdo, valor)
        else: # Se o valor for maior que o valor da raiz atual, então
            #Retorna o resultado da recursão para o mesmo método enviando o filho direito
            return self.buscaABB(raiz.direito, valor)

    def insereABB(self, raiz, no): #Método para inserir novos nós na árvore
        if raiz is None: #Se a raiz atual for nula, então
            # Retorna o novo nó
            return no
        if no.valor < raiz.valor: # Se o valor do novo nó for menor que o valor da raiz atual, então
            # O o filho esquerdo da raiz atual passa a ser o retorno da recursão enviando este filho esquerdo e o novo nó
            raiz.esquerdo = self.insereABB(raiz.esquerdo, no)
        elif no.valor > raiz.valor: # Se o valor do novo nó for maior que o valor da raiz atual, então
            # O filho direito da raiz atual passa a ser o retorno da recursão enviando este filho direito e o novo nó
            raiz.direito = self.insereABB(raiz.direito, no)

        return raiz # Por fim, retorna-se a raiz atual

    def minimoABB(self, raiz): # Método para retornar o menor valor da árvore
        if raiz.esquerdo is not None: # Se o filho esquerdo da raiz atual não for nulo, então
            # Retorna-se a recursão enviando este filho esquerdo no parametro
            return self.minimoABB(raiz.esquerdo)
        # Por fim, retorna-se a raiz atual
        return raiz

    def maximoABB(self, raiz): #Método para retornar o maior valor da árvore
        if raiz.direito is not None: # Se o filho direito da raiz atual não for nulo, então
            # Retorna-se a recursão enviando este filho direito no parametro
            return self.maximoABB(raiz.direito)
        # Por fim, retorna-se a raiz atual
        return raiz

    def removeABB(self, raiz, valor): #Método para remover um nó da árvore
        if raiz is None: # Se a raiz atual for nulo, então
            # Retorna-se None
            return None

        if valor < raiz.valor: # Se o valor buscado for menor que o valor da raiz atual, então
            # O filho esquerdo recebe a recursão enviando a si mesmo e o valor requerido como parametro
            raiz.esquerdo = self.removeABB(raiz.esquerdo, valor)
        elif valor > raiz.valor: # Se o valor buscado for maior que o valor da raiz atual, então
            # O filho direito recebe a recursão enviando a si mesmo e o valor requerido como parametro
            raiz.direito = self.removeABB(raiz.direito, valor)
        else: # Se o valor for igual, então
            if raiz.esquerdo is None:# Se o filho esquerdo da raiz atual for nulo, então
                # A raiz atual passa a ser o filho direito
                raiz = raiz.direito
            elif raiz.direito is None: # Se o filho direito da raiz atual for nulo, então
                # A raiz atual passa a ser o filho esquerdo
                raiz = raiz.esquerdo
            else: # se os filhos esquerdo e direito forem nulos, então
                minimo = self.minimoABB(raiz.direito) # Busca-se o menor valor a partir do filho direito
                raiz.valor = minimo.valor # A raiz atual tem o valor alterado para o valor minimo
                # O filho direito recebe o resultado da recursão enviando como parametro a si mesmo e o nó com menor valor
                raiz.direito = self.removeABB(raiz.direito, minimo.valor)
        # Por fim, retorna-se a raiz atual
        return raiz

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