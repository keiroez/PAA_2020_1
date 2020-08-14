from heap.heapbinario import HeapBinario

vetor = [100, 3, 36, 17, 108, 25, 13, 7, 12, 5]

vetor2 = [100, 17, 36, 12, 8, 125, 1, 7, 2, 5]

vetor3 = [5, 35, 87, 13, 1, 54, 100, 154, 12, 60]

heap = HeapBinario(vetor3)

# print(vetor2)

# heap.corrigeHeapDescendo(0)
# heap.corrigeHeapSubindo(5)
# print(vetor2)

# heap.insereNaHeap(75)
# print(vetor2)

# heap.removeDaHeap()
#
# print(vetor2)
#
# heap.alteraHeap(8, 101)
#
print(vetor3)

heap.constroiHeap()

print(vetor3)

