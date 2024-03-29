import numpy as np
import matplotlib.pyplot as plt

def lectura():
    file = open('C:\Archivos\Coeficientes.txt', mode='r')
    puntosO = file.read()
    puntos = puntosO.splitlines()
    puntos1= []
    for i in range(len(puntos)):
        aux = puntos[i]
        aux = aux.split(',')
        for j in aux:
            puntos1.append(float(j))
    return puntos1


def sumatoria(p, n, eje): # p= lista n=potencia eje=elegir si sumar x o y (true o false)
    suma = 0
    for i in range(len(p)):
        if eje:
            if (i % 2) == 0:
                suma += p[i]**n
        else:
            if (i % 2) != 0:
                if n == 0:
                    suma += p[i]
                else:
                    suma += (p[i-1] ** n) * (p[i])
    return suma


def matriz(mat, g):
    potencia = 0
    for i in range(g): # x
        contador = potencia
        for j in range(g): #y
            mat[j,i] = sumatoria(lectura(),contador, True)
            contador += 1
        potencia += 1
    mat[0,0] = 1
    return mat


def matrizE(mat, g):    #mat=matriz g=grado
    contador = 0
    matB = np.zeros((g))
    for i in range(g):
        matB[i] = sumatoria(lectura(),contador, False)
        contador += 1
    return matB

def grafica(result):
    PuntosX = []
    PuntosY = []
    x = np.arange(-5,5,.01)
    y = np.poly1d(result)(x)
    plt.grid(True)
    plt.plot(x,y, label="curva",color="blue")
    puntos = lectura()
    for i in range(len(puntos)):
        if (i % 2) == 0:
            PuntosX.append(puntos[i])
        else:
            PuntosY.append(puntos[i])
    plt.scatter(PuntosX, PuntosY, label="puntos", color="red")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    g = int(input("ingrese el grado del polinomio "))
    g = g+1
    mat = np.zeros((g,g))
    Result = (np.linalg.inv(matriz(mat, g)).dot(matrizE(matriz(mat, g), g))[::-1])
    print(np.poly1d(Result))
    grafica(Result)