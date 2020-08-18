from activitys.activity_140820_aed.heap.heapbinario import HeapBinario

def testeHeap():
    vetor = [100, 3, 36, 17, 108, 25, 13, 7, 12, 5]

    vetor2 = [100, 17, 36, 12, 8, 125, 1, 7, 2, 5]

    vetor3 = [5, 35, 87, 13, 1, 54, 100, 154, 12, 60]

    heap = HeapBinario(vetor)
    heap2 = HeapBinario(vetor2)
    heap3 = HeapBinario(vetor3)


    print("Heap 1:")
    print(vetor)
    heap.corrigeHeapDescendo(1)
    print("Heap 1 corrigido descendo")
    print(vetor)
    print("Heap 1 corrigindo subindo")
    heap.corrigeHeapSubindo(1)
    print(vetor)
    print()

    print("Heap 2")
    print(vetor2)
    heap2.insereNaHeap(75)
    heap2.insereNaHeap(88)
    heap2.insereNaHeap(75)
    heap2.insereNaHeap(4)
    print("Inserido valores no heap 2")
    print(vetor2)

    heap2.removeDaHeap()
    heap2.removeDaHeap()
    heap2.removeDaHeap()
    heap2.removeDaHeap()
    print("Removendo valores do heap 2")
    print(vetor2)
    print()

    heap2.corrigeHeapSubindo(2)
    print("Corrigindo heap 2 subindo")
    print(vetor2)
    print()

    print("Heap 3")
    print(vetor3)
    heap3.alteraHeap(5, 70)
    print("Heap 3 com indice 5 alterado")
    print(vetor3)
    heap3.alteraHeap(7, 160)
    print("Heap 3 com indice 7 alterado")
    print(vetor3)
    print()

    print("Construindo heap 3")
    heap3.constroiHeap()
    print(vetor3)
