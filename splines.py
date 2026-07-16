def spline_linear(x, y, valor):

    for i in range(len(x) - 1):
        if x[i] <= valor <= x[i + 1]:
            coeficiente = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
            return y[i] + coeficiente * (valor - x[i])
    return None

def spline_cubica_natural(x, y, valor):
    n = len(x)
    h = []

    for i in range(n - 1):
        h.append(x[i + 1] - x[i])
    alfa = [0] * n

    for i in range(1, n - 1):
        alfa[i] = (
            (3 / h[i]) * (y[i + 1] - y[i])
            - (3 / h[i - 1]) * (y[i] - y[i - 1])
        )

    l = [1] * n
    u = [0] * n
    z = [0] * n

    for i in range(1, n - 1):
        l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * u[i - 1]
        u[i] = h[i] / l[i]
        z[i] = (alfa[i] - h[i - 1] * z[i - 1]) / l[i]
    c = [0] * n
    b = [0] * (n - 1)
    d = [0] * (n - 1)

    for j in range(n - 2, -1, -1):
        c[j] = z[j] - u[j] * c[j + 1]
        b[j] = (
            (y[j + 1] - y[j]) / h[j]
            - h[j] * (c[j + 1] + 2 * c[j]) / 3
        )
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    for i in range(n - 1):
        if x[i] <= valor <= x[i + 1]:
            dx = valor - x[i]
            return (
                y[i]
                + b[i] * dx
                + c[i] * dx ** 2
                + d[i] * dx ** 3
            )
    return None