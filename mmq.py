def ajuste_linear(x, y):
    n = len(x)
    soma_x = sum(x)
    soma_y = sum(y)
    soma_xy = 0
    soma_x2 = 0

    for i in range(n):
        soma_xy += x[i] * y[i]
        soma_x2 += x[i] * x[i]
    a = (
        n * soma_xy - soma_x * soma_y
    ) / (
        n * soma_x2 - soma_x ** 2
    )
    b = (
        soma_y - a * soma_x
    ) / n
    return a, b

def prever(a, b, x):
    return a * x + b