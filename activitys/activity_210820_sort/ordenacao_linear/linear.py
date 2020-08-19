import time

def countingSort(vetor, k):

    B = k + 1
    C = [0] * B

    for i in vetor:
        C[i] += 1
    i = 0

    for a in range(B):
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


