
def coefBinominal(n, k):
    matriz = []
    linha = []



    for i in range(0, n):
        linha.append(1)
        linha.append(1)
        matriz.append(linha[0])
        matriz.append(linha[i])
        # matriz[i][i] = matriz[i][0] = 1

    for i in range(1, n):
        for j in range(1, i-1):
            linha[j] = linha[j-1]

            matriz[i][j] = matriz[i-1][j-1] + matriz[i-1][j]

    return matriz[n][k]

coefBinominal(3, 5)
