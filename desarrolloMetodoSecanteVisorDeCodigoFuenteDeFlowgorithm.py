def evaluarFx(a, b, c, x):
    resultado = a * x * x + b * x + c
    evaluarFx = resultado
    
    return evaluarFx

def secante(a, b, c, x0, x1, epsilon, maxIter):
    iteracion = 0
    terminate = False
    while iteracion < maxIter and not terminate:
        fx0 = evaluarFx(a, b, c, x0)
        fx1 = evaluarFx(a, b, c, x1)
        if fabs(fx1) < epsilon:
            print("Raíz: " + str(x1) + ", Iteraciones: " + str(iteracion))
            secante = x1
            terminate = True
        if fx1 - fx0 == 0:
            print("Error: el método no converge.")
            secante = 999999999
            terminate = True
        else:
            xNuevo = x1 - fx1 * x1 - x0 / fx1 - fx0
            x0 = x1
            x1 = xNuevo
            iteracion = iteracion + 1
        print("Iteraciones realizadas: " + str(iteracion))
    print("Raíz: " + str(x1) + ", Iteraciones: " + str(iteracion))
    secante = x1
    
    return secante

# Main
x0neg = -5
x0pos = 1
x1neg = -1
x1pos = 5
print("Ingresa a: ")
a = float(input())
print("Ingresa b: ")
b = float(input())
print("Ingresa c: ")
c = float(input())
print("Ingresa x0: ")
x0 = float(input())
print("Ingresa x1: ")
x1 = float(input())
print("Ingresa epsilon: ")
epsilon = float(input())
print("Ingresa maxIter: ")
maxIter = int(input())
raiz1 = secante(a, b, c, x0neg, x1neg, epsilon, maxIter)
print("Raíz 1 (aprox.): " + str(raiz1))
raiz2 = secante(a, b, c, x0pos, x1pos, epsilon, maxIter)
print("Raíz 2 (aprox.): " + str(raiz2))
