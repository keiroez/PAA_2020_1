from busca import *
from fatorial import *
from fibonacci import *
from potencia import *
from produtorio import *
from somatorio import *

vetor = [1, 2, 3, 4, 5, 6, 8, 9, 10, 22, 100]
print("Vetor inicial")
print(vetor)

print("")
busca = 8
print("Busca linear indice: {}".format(buscaLinear(vetor, busca)))

print("")
print("Buscar linea ordem indice: {}".format(buscaLinearOrdem(vetor, busca)))

print("")
print("Busca binaria indice: {}".format(buscaBinaria(vetor, busca)))

print("")
print("Somatorio: {}".format(somatorio(vetor)))

print("")
print("Produtorio: {}".format(produtorio(vetor)))

print("")
print("SomatorioPar: {}".format(somatorioPar(vetor)))

print("")
print("Busca linear recursiva indice: {}".format(buscaLinearRecursiva(vetor, len(vetor) - 1, busca)))

print("")
nFatorial = 5
print("Fatorial de {} = {}".format(nFatorial, fatorial(nFatorial)))

print("")
xPotencia = 4
nPotencia = 5
print("{} º potencia(v1) de {} = {}".format(nPotencia, xPotencia, potenciaV1(xPotencia, nPotencia)))

print("")
print("{} º potencia(v2) de {} = {}".format(nPotencia, xPotencia, potenciaV2(xPotencia, nPotencia)))

print("")
print("{} º potencia(v3) de {} = {}".format(nPotencia, xPotencia, potenciaV3(xPotencia, nPotencia)))

print("")
print("Busca binaria recursiva indice: {}".format(buscaBinariaRecursiva(vetor, 0, len(vetor), busca)))

print("")
N = 11
print("Fibonacci recursivo de {} = {}".format(N, fibonacciRecursivo(N)))

print("")
print("Fibonacci de {} = {}".format(N, fibonacci(N)))