import time
from activitys.activity_140820_aed.heap.heapbinario import HeapBinario
def selectionSort(vetor):

    for i in range(len(vetor)):     #Encontrando o menor valor no vetor
        indiceMin = i
        for j in range(i+1, len(vetor)):
            if vetor[indiceMin] > vetor[j]:
                indiceMin = j

        #Troca  menor elemento encontrado pelo primeiro elemento
        vetor[i], vetor[indiceMin] = vetor[indiceMin], vetor[i]


def heapsort(vetor):

    heap = HeapBinario(vetor)       #Cria heap
    n = heap.tamanho                #Determina n como o tamanho do heap
    heap.constroiHeap()             #Chama a função para construir o heap, colocando o maior elemento em primeiro
    for i in range(n-1, 0, -1):     #Corrige o Heap e coloca os maiores valores no final do vetor
        vetor[0], vetor[i] = vetor[i], vetor[0]
        heap.tamanho -= 1
        heap.corrigeHeapDescendo(0)



def exampleIntercalations():
    vetor = [99, 55, 33, 109, 23, 89, 21, 2, 30, 55, 78, 90, 400]

    print("Vetor inicial:")
    print(vetor)
    print()

    print("SELECTIONSORT")
    inicio = (time.time() * 1000)
    selectionSort(vetor)
    fim = (time.time() * 1000)
    print("Vetor ordenado:")
    print(vetor)
    print("Tempo: "+ str(round(fim - inicio, 4))+" ms")

    print()

    print("HEAPSORT")
    vetor2 = [99, 55, 33, 109, 23, 89, 21, 2, 30, 55, 78, 90, 400]
    inicio = (time.time() * 1000)
    heapsort(vetor2)
    fim = (time.time() * 1000)
    print("Vetor ordenado:")
    print(vetor2)
    print("Tempo: " + str(round(fim - inicio, 4)) + " ms")

exampleIntercalations()