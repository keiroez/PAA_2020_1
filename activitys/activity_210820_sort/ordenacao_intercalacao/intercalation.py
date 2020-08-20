import time

def mergeSort(vetor):
    if len(vetor) > 1:
        mid = len(vetor) // 2  # Encontrando o meio do vetor
        L = vetor[:mid]  # Dividindo os elementos do vetor no meio
        R = vetor[mid:]

        mergeSort(L)  # Ordenando a primeira metade
        mergeSort(R)  # Ordenando a segunda metade

        i = j = k = 0

        # Copiando os dados para os vetores temporários L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                vetor[k] = L[i]
                i += 1
            else:
                vetor[k] = R[j]
                j += 1
            k += 1

        # Verificando se algum elemento foi deixado
        while i < len(L):
            vetor[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            vetor[k] = R[j]
            j += 1
            k += 1


def exampleIntercalations(vetor):
    # vetor = [99, 55, 33, 109, 23, 89, 21, 2, 30, 55, 78, 90, 400]

    # print("Vetor inicial:")
    # print(vetor)
    inicio = (time.time() * 1000)
    mergeSort(vetor)
    fim = (time.time() * 1000)
    print("MERGESORT:")
    print(vetor)
    print("Tempo: "+ str(round(fim - inicio, 4))+" ms")
