import matplotlib.pyplot as plt
import numpy as np
def multiplation (c1, c2):

    real = c1[0] * c2[0] - c1[1] * c2[1]
    imaginate = c1[0] * c2[1] + c1[1] * c2[0]

    print_beatiful(real, imaginate)
    return (real, imaginate)
def print_beatiful (a,b):
    if b == None :
        print (a)
    else:
        print ("( " , a ," , ",b ,"i)")
def multiplicate_matrix(matrix1,matrix2):
    filaA = len(matrix1)
    filaB = len(matrix2)
    columnaA = len(matrix1[0])
    columnaB = len(matrix2[0])

    if columnaA!=filaB:
       print("The matrix doesn´t have same dimentions")
    else:
        result = [[[0,0] for columna in range(columnaB)] for fila in range(filaA)]
        for i in range(filaA):
            for j in range(columnaB):
                for k in range(filaB):
                    result[i][j] = sum(result[i][j],multiplation(matrix1[i][k],matrix2[k][j]))
        return result

###################### libraries
def canicas(matrix, array):
    p = multiplicate_matrix (matrix,array)
    return p

def grafica(v):
    print('array end state:', v)
    labels = []
    estado = []
    for i in range(len(v)):
        labels.append('Probability'+str(i))
        estado.append(v[i][0][0])

    index = np.arange(len(labels))
    plt.bar(index, estado)
    plt.xlabel('State')
    plt.ylabel('Content')
    plt.xticks(index, labels)
    plt.show()

def run():
    array = [[6],
             [2],
             [1],
             [5],
             [3],
             [10]
             ]
    matrix = [
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,1,0,0,0,1],
        [0,0,0,1,0,0],
        [0,0,1,0,0,0],
        [1,0,0,0,1,0]
    ]
    funcion = canicas(matrix, array)
    grafica(funcion)




if __name__ == "__main__":
    run()

