def somatorio(A):
    soma = 0
    for i in range(len(A)):
        soma += A[i]
    return soma

def somatorioPar(A):
    soma = 0
    for i in range(len(A)):
        if A[i] % 2==0:
            soma +=A[i]
    return soma