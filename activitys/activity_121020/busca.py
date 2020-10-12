def buscaLinear(A, k):
    i = 0
    while i < len(A):
        if A[i] == k:
            return i
        i += 1
    return -1


def buscaLinearOrdem(A, k):
    i = 0
    while i <= len(A) and k >= A[i]:
        if A[i] == k:
            return i
        i = i + 1
    return -1


def buscaBinaria(A, k):
    esquerda = 1
    direita = len(A)

    while esquerda <= direita:
        meio = int((esquerda + direita) / 2)

        if A[meio] == k:
            return meio

        elif k > A[meio]:
            esquerda = meio + 1

        else:
            direita = meio - 1

    return -1


def buscaLinearRecursiva(A, n, k):
    if n == 0:
        return -1

    if A[n] == k:
        return n
    return buscaLinearRecursiva(A, n - 1, k)


def buscaBinariaRecursiva(A, esquerda, direita, x):
    if esquerda > direita:
        return -1
    meio = int((esquerda + direita) / 2)

    if A[meio] == x:
        return meio

    elif x < A[meio]:
        for i in range(len(A)):
            return buscaBinariaRecursiva(A, esquerda, meio - 1, x)

    else:
        for i in range(len(A)):
            return buscaBinariaRecursiva(A, meio + 1, direita, x)
