class HeapBinario:
    def __init__(self, vetor):
        self.vetor = vetor
        self.tamanho = len(self.vetor)

    def corrigeHeapDescendo(self, i):
        pi = i+1
        pm = pi
        maior = i

        if 2*pi <= self.tamanho and self.vetor[2*pi-1] > self.vetor[pm-1]:
            maior = 2*pi-1
            pm = maior+1

        if 2*pi+1 <= self.tamanho and self.vetor[2*pi] > self.vetor[pm-1]:
            maior = 2*pi
            pm = maior+1

        if maior != i:
            aux = self.vetor[i]
            self.vetor[i] = self.vetor[maior]
            self.vetor[maior] = aux
            self.corrigeHeapDescendo(maior)

    def corrigeHeapSubindo(self, i):
        pai = int((i+1) / 2) - 1

        if i+1 >= 2 and self.vetor[i] > self.vetor[pai]:
            aux = self.vetor[i]
            self.vetor[i] = self.vetor[pai]
            self.vetor[pai] = aux
            self.corrigeHeapSubindo(pai)

    def insereNaHeap(self, x):
        self.vetor.append(x)
        self.tamanho += 1
        self.corrigeHeapSubindo(self.tamanho - 1)


    def removeDaHeap(self):
        x = None
        if self.tamanho >= 0:
            x = self.vetor[0]
            self.tamanho -= 1
            self.vetor[0] = self.vetor[self.tamanho]
            del self.vetor[-1]
            self.corrigeHeapDescendo(0)


    def alteraHeap(self, i, k):
        aux = self.vetor[i]
        self.vetor[i] = k

        if aux < k:
            self.corrigeHeapSubindo(i)
        if aux > k:
            self.corrigeHeapDescendo(i)

    def constroiHeap(self):
        for i in range(int(self.tamanho/2), -1, -1):
            self.corrigeHeapDescendo(i)


