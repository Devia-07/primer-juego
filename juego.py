import random
import math


lista = ["Funcion Lineal", "Funcion Cuadratica", "Funcion Parte Entera", "Funcion Valor Absoluto", "Funcion Inversa"]
def funciones():
    
    ecuaciones_cuadraticas = [
        ("x**2 - 4*x + 4 ", [2, 2, 0],[2,0],["R","y>=0"]),
        ("2*x**2 - 3*x + 1 ", [0.5, 1, 1],[0.75, -0.125],["R","y>=-0.125"]),
        ("3*x**2 + 6*x + 3 ", [-1, -1, 3],[-1, 0],["R","y>=0"]),
        ("x**2 + 5*x + 6 ", [-3, -2, 6],[-2.5,-0.25],["R","y>=-0.25"]),
        ("4*x**2 - 4*x + 1 ", [0.5, 0.5, 1],[0.5, 0],["R","y>=0"]),
    ]
    return ecuaciones_cuadraticas

def random_f(): 
    funcion_aleatoria = random.choice(lista)
    if funcion_aleatoria == 'Funcion Lineal':
        m = random.choice([i for i in range(0,20)])
        b = random.choice([i for i in range(0,20)])
        return lineal(m, b)
    elif funcion_aleatoria == 'Funcion Cuadratica':
        return cuadratica()
    elif funcion_aleatoria == 'Funcion Cubica':
        a = random.choice([i for i in range(0,20)])
        b = random.choice([i for i in range(0,20)])
        c = random.choice([i for i in range(0,20)])
        d = random.choice([i for i in range(0,20)])
    elif funcion_aleatoria == 'Funcion Parte Entera':
        return parte_entera()
    elif funcion_aleatoria == 'Funcion Valor Absoluto':
        return f_valor_absoluto()
    elif funcion_aleatoria == 'Funcion Inversa':
        return inversa()

def lineal(m, b):
    operador = random.choice(["+", "-"])
    preguntas = ["Cual es el dominio y el rango", "Cuales son los cortes con x y con y", "Es creciente, decreciente o constante"]
    pregunta = random.choice(preguntas)
    return f"¡Rapido analiza la siguiente funcion {m}x {operador} {b}: {pregunta}"

def cuadratica():
    global ecuaciones_cuadraticas
    ecuaciones_cuadraticas = [
        ("x**2 - 4*x + 4 ", [2, 2, 0],[2,0],["R","y>=0"]),
        ("2*x**2 - 3*x + 1 ", [0.5, 1, 1],[0.75, -0.125],["R","y>=-0.125"]),
        ("3*x**2 + 6*x + 3 ", [-1, -1, 3],[-1, 0],["R","y>=0"]),
        ("x**2 + 5*x + 6 ", [-3, -2, 6],[-2.5,-0.25],["R","y>=-0.25"]),
        ("4*x**2 - 4*x + 1 ", [0.5, 0.5, 1],[0.5, 0],["R","y>=0"]),
    ]
    ecuacion, soluciones, soluciones_vertice, rango_Dominio = random.choice(ecuaciones_cuadraticas)
    return f"¡Rapido analiza la siguiente funcion: {ecuacion} calcula los cortes con x y y"


def parte_entera():
    decimal = round(random.uniform(-10, 10), 1)
    x = [f"¡Rapido realiza la funcion parte entera: ⌊{decimal}⌋", f"¡Rapido realiza la funcion parte entera: ⌈{decimal}⌉"]
    return random.choice(x)

def f_valor_absoluto():
    x = random.randint(-50, 50)
    return f"¡Rapido realiza la funcion valor absoluto: |{x}|"



def inversa():
    preguntas = [
        "Cual es la funcion inversa de: F(x) = 2x + 1",
        "Cual es el punto de corte en X de: F(x) = 2x + 1",
        "Cual es la funcion inversa de: G(x) = 3x - 2",
        "Cual es el dominio y rango de: G^-1(y) = 2(y-1)",
        "Cuales son los puntos de corte en X y en Y de: H(x) = 1/2x + 3"
    ]
    return random.choice(preguntas)

if __name__ == '__main__':
    print(random_f())
