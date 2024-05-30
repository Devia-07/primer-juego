import random 
import math

lista = ["Funcion Lineal", "Funcion Cuadratica", "Funcion Cubica", "Funcion Raiz Cuadrada", "Funcion Logaritmica", "Funcion Parte Entera", "Funcion Valor Absoluto", "Funcion Compuesta", "Funcion Inversa"]


def random_f(): #funcion de py para elegir una funcion aleatoria
    funcion_aleatoria = 'Funcion Lineal'
    if funcion_aleatoria == 'Funcion Lineal':
        m = random.choice([i for i in range(0,20)])
        b = random.choice([i for i in range(0,20)])
        lineal(m, b)
    elif funcion_aleatoria == 'Funcion Cuadratica':
        cuadratica()
    elif funcion_aleatoria == 'Funcion Cubica':
        a = random.choice([i for i in range(0,20)])
        b = random.choice([i for i in range(0,20)])
        c = random.choice([i for i in range(0,20)])
        d = random.choice([i for i in range(0,20)])
        cubica(a,b,c,d)
    elif funcion_aleatoria == 'Funcion Raiz Cuadrada':
        f_raiz_cuadrada()
    elif funcion_aleatoria == 'Funcion Logaritmica':
        logaritmica()
    elif funcion_aleatoria == 'Funcion Parte Entera':
        parte_entera()
    elif funcion_aleatoria == 'Funcion Valor Absoluto':
        f_valor_absoluto()
    elif funcion_aleatoria == 'Funcion Compuesta':
        compuesta()
    elif funcion_aleatoria == 'Funcion Inversa':
        inversa()

def lineal(m, b):
    operador = random.choice(operandos)
    preguntas = ["Cual es el dominio y el rango", "Cuales son los cortes con x y con y", "Es creciente, decreciente o constante"]
    pregunta = random.choice(preguntas)
    print(f"¡Rapido analiza la siguiente funcion {m}x {operador} {b}")
    if pregunta == preguntas[0]:
        dominio = "todos los reales"
        rango = "todos los reales"
        print(pregunta)
        respuesta_dominio = input("Su respuesta al dominio: ")
        respuesta_rango = input("Su respuesta al rango: ")
        if respuesta_dominio.lower() == dominio and respuesta_rango.lower() == rango:
            print("Correcto")
        else:
            print("Incorrecto")
    elif pregunta == preguntas[1]:
        if b != 0 or m == 0:
            corte_y = f"0,{b}"
            x = -b / m if m != 0 else None  
            if x is not None:
                corte_x = f"{round(x, 2)},0"
            else:
                corte_x = ""
            print(pregunta)
            respuesta_x = input("Su respuesta del corte con x(el formato para escribir es x,0 y si no tiene cortes con x, simplemente das enter sin hacer nada mas): ")
            respuesta_y = input("Su respuesta del corte con y(el formato para escribir es 0,y): ")
            if respuesta_x == corte_x and respuesta_y == corte_y:
                print("Correcto")
            else:
                print(f"Incorrecto, la respuesta correcta era {corte_x}")
        else:
            corte_x = "0,0"
            corte_y = "0,0"
            print(pregunta)
            respuesta_x = input("Su respuesta del corte con x(el formato para escribir es x,0 y si no tiene cortes con x, simplemente das enter sin hacer nada mas): " )
            respuesta_y = input("Su respuesta del corte con y(el formato para escribir es 0,y): ")
            if respuesta_x == corte_x and respuesta_y == corte_y:
                print("Correcto")
            else:
                print("Incorrecto")

    elif pregunta == preguntas[2]:
        if m > 0:
            respuesta = "creciente"
        elif m < 0:
            respuesta = "decreciente"
        else:
            respuesta = "constante"
        print(pregunta)
        tu_respuesta = input("Su respuesta: ")
        if tu_respuesta == respuesta:
            print("Correcto")
        else:
            print("Incorrecto")

def cuadratica():
    
    # seleciona un problema aleatorio

    eleccion = random.randint(1, 3)
    
    # lista de ecuaciones cuadraticas con sus soluciones,cortes x y y, vertice y rango,dominio
    ecuaciones_cuadraticas = [
    ("x**2 - 4*x + 4 ", [2, 2, 0],[2,0],["R","y>=0"]), #soluciones cortes x y y, vertice, rango
    ("2*x**2 - 3*x + 1 ", [0.5, 1, 1],[0.75, -0.125],["R","y>=-0.125"]),
    ("3*x**2 + 6*x + 3 ", [-1, -1, 3],[-1, 0],["R","y>=0"]),
    ("x**2 + 5*x + 6 ", [-3, -2, 6],[-2.5,-0.25],["R","y>=-0.25"]),
    ("4*x**2 - 4*x + 1 ", [0.5, 0.5, 1],[0.5, 0],["R","y>=0"]),
]
    
    #elige una ecuacion aleatoria
    
    ecuacion,soluciones,soluciones_vertice,rango_Dominio = random.choice(ecuaciones_cuadraticas)
    print(f"¡Rapido analiza la siguiente funcion: {ecuacion}")
    
    if eleccion == 1:
        
        print("calcula los cortes con x y y")
        corte_x1 = int(input("Corte con x1: "))
        corte_x2 = int(input("Corte con x2: "))
        corte_y = int(input("Corte con y: "))
        if [corte_x1, corte_x2, corte_y] == soluciones:
            print("Correcto")
        else:
            print("Incorrecto")
            intento += 1
    elif eleccion == 2:
        print("Calcula el vertice de la parabola")
        vertice_x = int(input("Vertice x: "))
        vertice_y = int(input("Vertice y: "))
        if [vertice_x, vertice_y] == soluciones_vertice:
            print("Correcto")
        else:
            print("Incorrecto")
    else:
        print("calcula en rango y dominio de la funcion")
        dom = input("Dominio: ")
        ran = input("Rango: ")
        if [dom, ran] == rango_Dominio:
            print("Correcto")
        else:
            print("Incorrecto")
def cubica():
    pass

def f_raiz_cuadrada():
    pass

def logaritmica():
    pass

def parte_entera():

    decimal = round(random.uniform(-10, 10), 1) #genera un numero decimal aleatorio
    x = [f"¡Rapido realiza la funcion parte entera: ⌊{decimal}⌋ ", f"¡Rapido realiza la funcion parte entera: ⌈{decimal}⌉ "] #preguntas posibles
    preg_0 = random.choice(x) #elige una pregunta aleatoria
    if preg_0 == x[0]:
        print(f"¡Rapido realiza la funcion parte entera: ⌊{decimal}⌋ ")
        ans = int(input("Respuesta: "))
        if ans == math.floor(decimal):
            print("¡Correcto!")  
        else: 
            print("¡Incorrecto!")
    elif preg_0 == x[1]:
        print(f"¡Rapido realiza la funcion parte entera: ⌈{decimal}⌉ ")
        ans = int(input("Respuesta: "))
        if ans == math.ceil(decimal) or (decimal < 0 and ans == math.floor(decimal)): #si el numero es negativo se redondea hacia abajo
            print("¡Correcto!")
        else:
            print("¡Incorrecto!")
    
def f_valor_absoluto():
    x = random.randint(-50, 50)
    print(f"¡Rapido realiza la funcion valor absoluto: |{x}| ")
    ans = int(input("Respuesta: "))
    if ans == abs(x):
        print("¡Correcto!")
    else:
        print("¡Incorrecto!")
        
def compuesta():
    pass

def inversa():
    a = "Cual es la funcion inversa de: F(x) = 2x + 1"
    b = "Cual es el punto de corte en X de: F(x) = 2x + 1"
    c = "Cual es la funcion inversa de: G(x) = 3x - 2"
    d = "Cual es el dominio y rango de: G^-1(y) = 2(y-1)"
    e = "Cuales son los puntos de corte en X y en Y de: H(x) = 1/2x + 3"
    originales = [a, b, c, d, e]
    x = random.choice(originales)
    
    if x == a:
        r_a = "f^-1(x)=(x-1)/2"
        print(a)
        r_u = input("Respuesta: ").lower().strip().replace(" ", "")
        if r_u == r_a.lower().strip().replace(" ", ""):
            print("¡Correcto!")
        else:
            print("¡Incorrecto!")
    
    elif x == b:
        r_b = "(-1/2,0)"
        print(b)
        r_u = input("Respuesta: ").lower().strip().replace(" ", "")
        if r_u == r_b.lower().strip().replace(" ", ""):
            print("¡Correcto!")
        else:
            print("¡Incorrecto!")
    
    elif x == c:
        r_c = "g^-1(x)=(x+2)/3"
        print(c)
        r_u = input("Respuesta: ").lower().strip().replace(" ", "")
        if r_u == r_c.lower().strip().replace(" ", ""):
            print("¡Correcto!")
        else:
            print("¡Incorrecto!")
    
    elif x == d:
        r_s = ["r", "losreales", "todoslosreales", "todoslosnumerosreales"]
        print(d)
        r_u = input("Dominio: ").lower().strip().replace(" ", "")
        r_u2 = input("Rango: ").lower().strip().replace(" ", "")
        if r_u and r_u2 in r_s:
            print("¡Correcto!")
            
        else:
            print("¡Incorrecto!")
    
    elif x == e:
        r_e = "(-6,0)"
        print(e)
        r_u = input("Respuesta para X: ").lower().strip().replace(" ", "")
        if r_u == r_e.lower().strip():
            r_ey = "(0,3)"
            r_uy = input("Respuesta para Y: ").lower().strip().replace(" ", "")
            if r_uy == r_ey.lower().strip():
                print("¡Correcto!")
            else:
                print("¡Incorrecto!")
        else:
            print("¡Incorrecto!")
    
    
    

if __name__ == '__main__':
    
    funciones = [
    "Funcion Lineal",
    "Funcion Cuadratica",
    "Funcion Cubica",
    "Funcion Raiz Cuadrada",
    "Funcion Logaritmica",
    "Funcion Parte Entera",
    "Funcion Valor Absoluto",
    "Funcion Compuesta",
    "Funcion Inversa"
    ]
    operandos = ["+", "-"]
    # cuadratica()
    random_f()
