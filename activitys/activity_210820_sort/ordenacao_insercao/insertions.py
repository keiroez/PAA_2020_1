import time

def insertionSort(vetor):
    n = len(vetor)
    inicio = (time.time() * 1000)
    for i in range(2, n):
        atual = vetor[i]
        j = i - 1
        while j>0 and vetor[j]>atual:
            vetor[j+1] = vetor[j]
            j = j - 1
        vetor[j+1] = atual
    fim = (time.time() * 1000)
    return str(round(fim - inicio, 4))

def shellsort(vetor):
    inicio = (time.time() * 1000)
    n = len(vetor)
    gap = n//2

    while gap > 0:
        for i in range(gap, n):
            temp = vetor[i]
            j = i
            while j >= gap and vetor[j-gap] > temp:
                vetor[j] = vetor[j-gap]
                j -= gap

            vetor[j] = temp
        gap //= 2

    fim = (time.time() * 1000)
    return str(round(fim - inicio, 4))

def exampleInsertions():
    v = [4, 6, 2, 60, 10, 33, 88, 9]
    v2 = [4, 6, 2, 60, 10, 33, 88, 9]

    tempo = insertionSort(v)
    print("INSERTIONSORT")
    print(" Tempo: "+ tempo + " ms")
    print()

    print("SHELLSORT")
    tempo = shellsort(v2)
    print(v2)
    print(" Tempo: "+ tempo + " ms")