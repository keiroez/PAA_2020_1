from listaSimples.no import No

class ListaSimples:
    def __init__(self, valor):  #construtor recebendo um valor para iniciar o nó
        novoNo = No(valor)      #novo nó instanciado com o valor como parametro
        self.cabeca = novoNo    #atribui o novo nó à cabeça da lista
        self.cauda = novoNo     #atribui o novo nó à cauda da lista

    def inserirInicio(self, valor): #Metodo para inserir nó no inicio da lista
        novoNo = No(valor)          #novo nó instanciado

        if(self.cabeca is not None):        #Verifica se a cabeça da lista não é nula
            novoNo.proximo = self.cabeca    #Atribui a cabeça atual como o proximo do novo nó
        else:                               #Verifica se a cabeça da lista é nula
            self.cauda = novoNo             #A cauda também será o novo nó
        self.cabeca = novoNo                #A cabeça da lista passa a ser o novo nó

    def inserirFim(self, valor):        #Método para inserir nó no fim da lista
        novoNo = No(valor)              #novo nó instanciado
        if self.cauda is not None:      #Verifica se a cauda não é nula
            self.cauda.proximo = novoNo #Atribui o novo nó como proximo da cauda
        else:                           #Verifica se a cauda é nula
            self.cabeca = novoNo        #A cabeça também será o novo nó
        self.cauda = novoNo             #A cauda passa a ser o novo nó


    def buscarNaLista(self, valor):     #Metodo para buscar valor na lista
        x = self.cabeca                 # Atribui a cabeça da lista a variável x
        while x is not None and x.valor != valor:   # Enquanto x não for nulo e x.valor for diferente do valor buscado
            x = x.proximo                           # atribui o proximo elemento da lista a x
        if x is not None:
            return str(x.valor)+" encontrado"                          #retorna x com o nó (se encontrado) ou como None, caso não encontrado
        else:
            return "Valor "+str(valor)+" Não encontrado"
    def removerValor(self, valor):      #Método para remover um valor na lista
        x = self.cabeca                 # atribui a cabeça da lista à variável x

        if x.valor == valor:            #Verifica se o valor está na cabeça da lista
            self.cabeca = x.proximo     # a cabeça passa a ser o próximo elemento da lista
            self.removerValor(valor)    # por meio de recursão continua-se procurando o valor na lista
        else:                           #Verifica se não está na cabeça da lista
            anterior = None             #cria-se uma variável "anterior" com valor Nulo
            while x is not None and x.valor != valor:   #Enquanto x não for nulo e x.valor não for o valor buscado
                anterior = x            # Atribui- x à variavel "anterior"
                x = x.proximo           # x passa a ser o próximo elemento da lista

            if x is None:               # Verifica se x é nulo
                print("Valor "+valor+" Não encontrado") # Imprime o texto de "não encontrado"
                return None             # Retorna None

            if x.proximo is not None:           #Verifica se x não é nulo
                anterior.proximo = x.proximo    #o próximo do anterior passa a ser o próximo de x
            else:                       # Verifica se x for nulo
                anterior.proximo = None # O próximo do anterior passa a ser nulo

    def removerIndex(self, index):  # Método para remover por index da lista
        x = self.cabeca # Atribui a cabeça da lista a x
        anterior = None # cria uma variável para guardar o anterior

        if index==0:    #Verifica se o index é 0
                self.cabeca = x.proximo     #cabeça passa a ser o próximo da lista

        else:                           # Verifica se o index é diferente de 0
            for i in range(index):      # para i num range do tamanho do index
                anterior = x            # Atribui x à variável anterior
                x = x.proximo           # x passa a ser o próximo da lista
                if(x is None):          #Verifica se x é nulo
                    break               # Para o laço

            if x is not None:                   # Verifica se x não é nulo
                anterior.proximo = x.proximo    #o próximo do anterior passa a ser o próximo de x
            else:                               #Verifica se x é nulo
                print("Indice "+index+" não encontrado")  #Imprime que o índice não existe






