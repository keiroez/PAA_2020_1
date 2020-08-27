import time

def multiplicaInteiros(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:    #Verifica o tamanho de x ou y igual a 1
        return x * y                            #Retorna a multiplicação de x e y

    m = max(len(str(x)), len(str(y)))           #Pega o maior número de caracteres entre x e y
    m2 = m // 2                                 #Define m2 como o piso de m por 2

    a = x // 10 ** (m2)                 #Define "a" como os "m2" digitos iniciais de x
    b = x % 10 ** (m2)                  #Define "b como os "m2" digitos finais de x
    c = y // 10 ** (m2)                 #Define "c" como os "m2" digitos iniciais de y
    d = y % 10 ** (m2)                  #Define "d" como os "m2" digitos finaix de y


    p1 = multiplicaInteiros(a, c)       #Aplica recursão enviando a e c
    p2 = multiplicaInteiros(a, d)       #Aplica recursão enviando a e d
    p3 = multiplicaInteiros(b, c)       #Aplica recursão enviando b e c
    p4 = multiplicaInteiros(b, d)       #Aplica recursão enviando a e d

    return (10**(2*m2))*p1 + (10**(m2))*(p2+p3) + p4        #Retorna o resultado da equação de multiplicação

def karatsuba(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:    #Verifica o tamanho de x ou y igual a 1
        return x * y                            #Retorna a multiplicação de x e y

    m = max(len(str(x)), len(str(y)))           # Pega o maior número de caracteres entre x e y
    m2 = m // 2                                 # Define m2 como o piso de m por 2

    a = x // 10 ** (m2)                 # Define "a" como os "m2" digitos iniciais de x
    b = x % 10 ** (m2)                  # Define "b como os "m2" digitos finais de x
    c = y // 10 ** (m2)                 # Define "c" como os "m2" digitos iniciais de y
    d = y % 10 ** (m2)                  # Define "d" como os "m2" digitos finaix de y

    p1 = karatsuba(a, c)        #Aplica recursão enviando a e c
    p2 = karatsuba(b, d)        #Aplica recursão enviando b e d
    p3 = karatsuba(a+b, c+d)    #Aplica recursão enviando a soma de a e b e a soma de c e d

    return 10**(2*m2)*p1 + (10**(m2)*(p3-p1-p2)) + p2   #Retorna o resultado da equação de karatsuba

def exemploDivisionAndConquest():
    print("MULTIPLICAÇÃO TRADICIONAL")
    inicio = (time.time() * 1000)
    print(multiplicaInteiros(12345, 56789))
    fim = (time.time() * 1000)
    print("Tempo: "+str(round(fim - inicio, 4)))

    print()

    print("KARATSUBA")
    inicio = (time.time() * 1000)
    print(karatsuba(12345, 56789))
    fim = (time.time() * 1000)
    print("Tempo: " + str(round(fim - inicio, 4)))


