class HeapBinario:
    def __init__(self, vetor):
        self.vetor = vetor              #Construtor definindo os atributos do vetor e tamanho deste
        self.tamanho = len(self.vetor)

    def corrigeHeapDescendo(self, i):
        adapted_i = i+1                 #Adapta o valor de i para o algoritmo
        adapted_maior = adapted_i       #Adapta o valor de maior para o algoritmo
        maior = i                       #Atribui i à várivavel maior

        if 2*adapted_i <= self.tamanho and self.vetor[2*adapted_i-1] > self.vetor[adapted_maior-1]: #Verifica se o filho esquerdo é maior
            maior = 2*adapted_i-1       #Atribui o indice do filho esquerdo como maior
            adapted_maior = maior+1     #Adapta o valor de maior novamente

        if 2*adapted_i+1 <= self.tamanho and self.vetor[2*adapted_i] > self.vetor[adapted_maior-1]: #Verifica se o filho direito é maior
            maior = 2*adapted_i         #Atribui o indice filho direito como maior
            adapted_maior = maior+1     #Adapta o valor de maior novamente

        if maior != i:                          #Vefirifica se o maior é diferente do indice iniciado
            aux = self.vetor[i]
            self.vetor[i] = self.vetor[maior]   #Troca o vetor[i] e o vetor[maior] de lugar
            self.vetor[maior] = aux
            self.corrigeHeapDescendo(maior)

    def corrigeHeapSubindo(self, i):
        pai = int((i+1) / 2) - 1                            #Faz o cálculo do pai através do piso da divisão

        if i+1 >= 2 and self.vetor[i] > self.vetor[pai]:    #Verifica se o i+1 é maior que 2 e se o filho é maior que o pai
            aux = self.vetor[i]
            self.vetor[i] = self.vetor[pai]                 #Troca o pai de lugar com o filho
            self.vetor[pai] = aux
            self.corrigeHeapSubindo(pai)

    def insereNaHeap(self, x):
        self.vetor.append(x)                                #Adiciona um novo elemento no final do vetor
        self.tamanho += 1                                   #Aumenta o tamanho do vetor
        self.corrigeHeapSubindo(self.tamanho - 1)           #Corrige o heap subindo a partir do novo elemento


    def removeDaHeap(self):
        x = None
        if self.tamanho >= 0:                               #Verifica se o vetor não está vazio
            x = self.vetor[0]
            self.tamanho -= 1                               #Diminui o tamanho do vetor
            self.vetor[0] = self.vetor[self.tamanho]        #Coloca o valor do ultimo elemento do vetor no inicio
            del self.vetor[-1]                              #Deleta o ultimo indice do vetor
            self.corrigeHeapDescendo(0)                     #Corrige o heap subindo


    def alteraHeap(self, i, k):
        aux = self.vetor[i]
        self.vetor[i] = k                   #troca o valor do elemento por um novo

        if aux < k:                         #Verifica se o valor anterior é menor que o novo
            self.corrigeHeapSubindo(i)      #Corrige o heap subindo a partir do elemento alterado
        if aux > k:                         #Verifica se o valor anterior é maior que o novo
            self.corrigeHeapDescendo(i)     #Corrige o heap descendo

    def constroiHeap(self):
        for i in range(int(self.tamanho/2), -1, -1):    #Faz um for em todos os nós do heap a partir do último
            self.corrigeHeapDescendo(i)                 #corrige o heap descendo a partir do nó atual


