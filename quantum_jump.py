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

###################### libraries pass
def agate(matrix, array):
    p = multiplicate_matrix (matrix,array)
    return p

def grafic(v):
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

def double_slit_probabily(a,m,clics):
    if clics == 0:
        return  a
    elif clics == 1:
        return multiplicate_matrix(m,a)
    else:
        return multiplicate_matrix(m,double_slit_probabily(a,m,clics-1))

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
    funcion = agate(matrix, array)
    grafic(funcion)
    A = [[[1,0]],
         [[0,0]],
         [[0,0]],
         [[0,0]],
         [[0,0]],
         [[0,0]],
         [[0,0]],
         [[0,0]],
        ]
    M = [[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
        [[1/2,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
        [[1/2,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
        [[0,0],[1/3,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0]],
        [[0,0],[1/3,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0]],
        [[0,0],[1/3,0],[1/3,0],[0,0],[0,0],[1,0],[0,0],[0,0]],
        [[0,0],[0,0],[1/3,0],[0,0],[0,0],[0,0],[1,0],[0,0]],
        [[0,0],[0,0],[1/3,0],[0,0],[0,0],[0,0],[0,0],[1,0]],
        ]
    for i in range(3):
        grafic(double_slit_probabily(A,M,i),i)
    Matr=[ [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
        [[1/2**(1/2),0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
        [[1/2**(1/2),0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
        [[0,0],[-1/6**(1/2),1/6**(1/2)],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0]],
        [[0,0],[-1/6**(1/2),-1/6**(1/2)],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0]],
        [[0,0],[1/6**(1/2),-1/6**(1/2)],[-1/6**(1/2),1/6**(1/2)],[0,0],[0,0],[1,0],[0,0],[0,0]],
        [[0,0],[0,0],[-1/6**(1/2),-1/6**(1/2)],[0,0],[0,0],[0,0],[1,0],[0,0]],
        [[0,0],[0,0],[1/6**(1/2),-1/6**(1/2)],[0,0],[0,0],[0,0],[0,0],[1,0]]
      ]
    Arra = [[[1,0]],
        [[0,0]],
        [[0,0]],
        [[0,0]],
         [[0,0]],
         [[0,0]],
         [[0,0]],
         [[0,0]]
        ]
    for i in range(3):
        grafic(double_slit_probabily(Matr,Arra,i),i)
    

if __name__ == "__main__":
    run()

