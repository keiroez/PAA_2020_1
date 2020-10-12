def fibonacciRecursivo(n):
    if n <= 2:
        return 1
    return fibonacciRecursivo(n - 1) + fibonacciRecursivo(n - 2)


def fibonacci(n):
    if n <= 2:
        return 1
    F = [0]
    F = F*n

    F[0] = 1
    F[1] = 1

    for i in range(2, n):
        F[i] = F[i - 1] + F[i - 2]
    return F[n-1]
