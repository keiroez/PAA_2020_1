from activitys.activity_210820_sort.ordenacao_insercao.insertions import exampleInsertions
from activitys.activity_210820_sort.ordenacao_intercalacao.intercalation import exampleIntercalations
from activitys.activity_210820_sort.ordenacao_linear.linear import exampleLinear
from activitys.activity_210820_sort.ordenacao_selecao.selection import exampleSelection
from activitys.activity_210820_sort.ordenacao_troca.swap import exampleSwap
import random

x = 15
vetorOriginal = random.sample(range(100),  x)

print("Vetor Original:")
print(vetorOriginal)
print()

print("Ordenação por inserção:")
vInsertion = vetorOriginal[0:x]
vShell = vetorOriginal[0:x]
exampleInsertions(vInsertion, vShell)

print()

print("Ordenação por intercalação")
vMerge = vetorOriginal[0:x]
exampleIntercalations(vMerge)

print()

print("Ordenação por seleção")
vSelection = vetorOriginal[0:x]
vHeap = vetorOriginal[0:x]
exampleSelection(vSelection, vHeap)

print()

print("Ordenação por troca")
vSwap = vetorOriginal[0:x]
exampleSwap(vSwap)

print()

print("Ordenação por linear")
vCount = vetorOriginal[0:x]
exampleLinear(vCount)






