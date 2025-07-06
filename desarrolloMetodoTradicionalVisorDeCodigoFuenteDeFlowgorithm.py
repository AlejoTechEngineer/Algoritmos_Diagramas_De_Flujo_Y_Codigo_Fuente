negativo = "La ecuación de segundo grado no tiene solución en el conjunto de los números reales."
a = float(input())
b = float(input())
c = float(input())
if b ** 2 - 4 * a * c >= 0:
    x1 = -b - sqrt(b ** 2 - 4 * a * c) / 2 * a
    x2 = -b + sqrt(b ** 2 - 4 * a * c) / 2 * a
    print(x1)
    print(x2)
else:
    print(negativo)
