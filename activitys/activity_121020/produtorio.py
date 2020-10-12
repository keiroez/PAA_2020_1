def produtorio(A):
    produto = 1
    for i in range(len(A)):
        produto *= A[i]
    return produto