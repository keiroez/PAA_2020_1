import time

def countingSort(vetor, k):


    B = k + 1           #Maior valor do vetor
    C = [0] * B         #Inicializa vetor com quantidades de zeros igual ao maior valor do vetor

    for i in vetor:     #Encontra a quantidade de ocorrências de cada elemento e seta 1 na sua posição
        C[i] += 1

    i = 0

    for a in range(B):  #Restaura os valores com ocorrências para o vetor original em ordem
        for c in range(C[a]):
            vetor[i] = a
            i += 1


def exampleLinear():
    vetor = [99, 55, 33, 109, 23, 89, 21, 2, 30, 55, 78, 90, 400]
    print("Vetor inicial:")
    print(vetor)
    inicio = (time.time() * 1000)
    countingSort(vetor, 400)
    fim = (time.time() * 1000)
    print()
    print("Vetor ordenado:")
    print(vetor)
    print("Tempo: " + str(round(fim - inicio, 4)) + " ms")

exampleLinear()
