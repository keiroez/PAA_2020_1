def bubbleSort5(A,d=0):
# sem usar break mas naive como o 2,
# pode ser melhorado usando técnicas do 1 ou do 4
    n = len(A) - 1
    s=0
    c=" "
    ordenado = False
    k = 0

    while not ordenado and k<len(A)-1:
        newn = 0
        ordenado = True
        # adaptado do algoritmo bbs1 (k)
        for i in range(0,len(A) - k - 1):
            s+=1
            if d: print(A)
            if A[i] > A[i + 1]:      
                if d:
                    m=(2*c)+"|"+(2*c)
                    l=(i)*(4*c)+m+(n-i-len(m))*(4*c)
                    print(l)
                    print(i)  
                A[i], A[i + 1] = A[i + 1], A[i]
                ordenado = False
                newn = i+1
        k+=1
        # adaptado do algoritmo bbs4 (newn)
        n = newn
        if n < 1:
            ordenado = True
    
    print(s," passos - ", end=" ")
    print(A)


import random
print("Caso aleatório")
w=random.sample(range(10,100),15)
print(w)
s=w.copy()
bubbleSort5(s)

print("Pior caso")
w=list(range(150,0,-10))
print(w)
s=w.copy()
bubbleSort5(s)

print("Melhor caso")
w=list(range(10,160,10))
print(w)
s=w.copy()
bubbleSort5(s)