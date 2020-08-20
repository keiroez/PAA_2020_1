import time

def particiona(vetor, inicio, fim):
    pivo = vetor[fim]       #Seleciona o ultimo elemento como pivot
    i = inicio - 1          #Pega o index do menor elemento

    for j in range(inicio, fim):
        if vetor[j] <= pivo:        #Troca se o elemento for melhor ou igual ao pivot
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]


    vetor[i+1], vetor[fim] = vetor[fim], vetor[i+1]
    return i+1

def quicksort(vetor, inicio, fim):
    if inicio < fim:
        x = particiona(vetor, inicio, fim)
        quicksort(vetor, inicio, x-1)       #Ordena os elementos antes e depois da partição
        quicksort(vetor, x+1, fim)



def exampleSwap(vetor):
    # vetor = [99, 55, 33, 109, 23, 89, 21, 2, 30, 55, 78, 90, 400]

    print("QUICKSORT")
    inicio = (time.time() * 1000)
    quicksort(vetor, 0, len(vetor) - 1)
    fim = (time.time() * 1000)
    print(vetor)
    print("Tempo: " + str(round(fim - inicio, 4)) + " ms")
