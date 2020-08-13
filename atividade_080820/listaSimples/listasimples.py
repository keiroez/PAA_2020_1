from listaSimples.no import No

class ListaSimples: #Lista simplesmente encadeada
    def __init__(self, valor): #construtor recebendo um valor para iniciar o nó
        novoNo = No(valor) #novo nó instanciado com o valor como parametro
        self.cabeca = novoNo #atribuindo o novo nó à cabeça da lista
        self.cauda = novoNo #atribuindo o novo nó à cauda da lista

    def inserirInicio(self, valor): #Metodo para inserir nó no inicio da lista
        novoNo = No(valor) #novo nó instanciado

        if(self.cabeca is not None): #se a cabeça da lista não for nula então:
            novoNo.proximo = self.cabeca # o proximo do novo nó será a cabeça anterior
        else: # se a cabeça da lista for nula então:
            self.cauda = novoNo # a cauda também será o novo nó
        self.cabeca = novoNo #A cabeça da lista passa a ser o novo nó

    def inserirFim(self, valor): #inserir nó no fim da lista
        novoNo = No(valor) #novo nó instanciado
        if self.cauda is not None: # Se a cauda não for nula então:
            self.cauda.proximo = novoNo # O proximo da cauda passa a ser o novo nó
        else: # Se a cauda for nula então a lista está vazia e:
            self.cabeca = novoNo # A cabeça também será o novo nó
        self.cauda = novoNo # A cauda passa a ser o novo nó


    def buscarNaLista(self, valor): #Metodo para buscar valor na lista
        x = self.cabeca # Atribuindo a cabeça da lista a variável x
        while x is not None and x.valor != valor: # Enquanto x não for nulo e x.valor for diferente do valor buscado
            x = x.proximo # é atribuido a x o próximo elemento da lista
        return x #Por fim, retorna-se x com o nó (se encontrado) ou como None, caso não encontrado

    def removerValor(self, valor): #Método para remover um valor na lista
        x = self.cabeca # atribuido a cabeça da lista à variável x

        if x.valor == valor: # Se o valor estiver na cabeça então:
            self.cabeca = x.proximo # a cabeça passa a ser o próximo elemento da lista
            self.removerValor(valor) # e por meio de recursão continua-se a procurar o valor na lista
        else: # Se não estiver na cabeça da lista, então:
            anterior = None #cria-se uma variável anterior com valor Nulo
            while x is not None and x.valor != valor: #Enquanto x não for nulo e x.valor não for o valor buscado
                anterior = x # Atribui-se x à variavel "anterior"
                x = x.proximo # x passa a ser o próximo elemento da lista

            if x is None: # Se x for nulo, então:
                print("Não encontrado") # Imprime o texto de não encontrado
                return None # Retorna-se None

            if x.proximo is not None: # Se x não for nulo, então:
                anterior.proximo = x.proximo # o próximo do anterior passa a ser o próximo de x
            else: # Se x for nulo, então:
                anterior.proximo = None # O próximo do anterior passa a ser nulo

    def removerIndex(self, index): # Método para remover por index da lista
        x = self.cabeca # Atribui-se à x a cabeça da lista
        anterior = None # cria-se uma variável para guardar o anterior

        if index==0: #Se o index for 0,
                self.cabeca = x.proximo # então a cabeça passa a ser o próximo da lista

        else: # Se o index for diferente de 0, então:
            for i in range(index): # para i num range do tamanho do index
                anterior = x # Atribui-se x à variável anterior
                x = x.proximo # x passa a ser o próximo da lista
                if(x is None): # Se x for nulo
                    break # O for é parado

            if x is not None: # Se x não for nulo
                anterior.proximo = x.proximo # o próximo do anterior passa a ser o próximo de x
            else: # Se x for nulo
                print("Indice não encontrado") #Imprime que o índice não existe






