def potenciaV1(x, n):
    if n == 0:
        return 1
    return x * potenciaV1(x, n - 1)


def potenciaV2(x, n):
    if n == 0:
        return 1

    if n % 2 == 0:
        return potenciaV2(x, n / 2) * potenciaV2(x, n / 2)
    else:
        return x * potenciaV2(x, (n - 1) / 2) * potenciaV2(x, (n - 1) / 2)


def potenciaV3(x, n):
    if n == 0:
        return 1

    if n % 2 == 0:
        aux = potenciaV3(x, n / 2)
        return aux * aux
    else:
        aux = potenciaV3(x, (n - 1) / 2)
        return x * aux * aux
