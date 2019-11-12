import numpy as np

def lectura():
    file = open('C:\Archivos\Coeficientes1.txt', mode='r')
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
            if (i % 2) == 0:
                suma = (p[i] ** n) * (p[i+1])

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
    print(mat)
    return mat

def matrizE(mat, g):    #mat=matriz g=grado
    for i in range(g):
        mat[i, g] = sumatoria(lectura(),contador, False)

if __name__ == '__main__':
    g = int(input("ingrese el grado del polinomio"))
    g = g+1
    mat = np.zeros((g,g))
    matrizE(matriz(mat, g),g)
    print(lectura())
