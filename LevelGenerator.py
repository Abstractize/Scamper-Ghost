import random
def NullMatrix(i,j):#Creador de matriz nula
    ji=j#Guarda el valor de j
    matrix=[]
    matrixinside=[]
    while i != 0:#indice de filas
        while j!=0:#indice de columnas
            matrixinside.append(0)#coloca "0" en toda la matriz hasta que el j se acabe
            j-=1
        else:#en caso de que le j sea 0 vuelve a darle valor a j y coloca las columnas de la fila en la matriz
            matrix.append(matrixinside)
            matrixinside=[]
            i-=1
            j=ji
    return matrix
def set_level_values(level):#Agrega los valores de cada objeto según cada nivel
    coins=15*level#15 monedas multiplicado por el nivel en que se encuentre
    drugs= 4*level#4 pastillas de poder multiplicado por el nivel en que se encuentre
    food= 6*level#6 objetos para aumentar el puntaje multiplicado por el nivel en que se encuentre
    Matrix=NullMatrix(32,30)
    while coins != 0:
        i=random.randrange(0,32)
        j=random.randrange(0,30)
        if Matrix[i][j] == 0:
            Matrix[i][j]=1
            coins-=1
    while drugs != 0:
        i=random.randrange(0,32)
        j=random.randrange(0,30)
        if Matrix[i][j] == 0:
            Matrix[i][j]=2
            drugs-=1        
    while food != 0:
        i=random.randrange(0,32)
        j=random.randrange(0,30)
        if Matrix[i][j] == 0:
            Matrix[i][j]=3
            food-=1
    return Matrix        
