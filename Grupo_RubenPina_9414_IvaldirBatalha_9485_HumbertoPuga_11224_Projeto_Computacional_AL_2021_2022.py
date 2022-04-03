import numpy as np

#--------------------------Exercicio_1_2----------------------------

#--------------------------Exercicio 1------------------------------

#Alinea A de 1

def transposta(A):
    return 

#Alinea B de 1

def traco():
    return 

#Alinea C de 1

def traco_secundaria():
    return

#Alinea D de 1

def soma_mat():
    return

#Alinea E de 1

def mult_escalar_mat():
    return

#Alinea F de 1

def prod_mat():
    return

#--------------------------Exercicio 2

A = np.array ([[1, 2, 3], [1, 3, 4], [2, 6, 7]])
B = np.array ([[1, 2, 3, 1, -5, 6], [1, 3, 4, -2, 1, 8], [2, 4, 7, 3, 4, 1]])
C = np.array ([[1, 3, 4, -2, 1, 8], [8, -2, 7, 1, -5, 6], [1, 3, 4, -2, 1, -9], [-6, 4, 7, 3, -2, 1], [1, 9, 3, 1, -5, 6], [-4, 4, 1, 3, -7, 1]])

def main(A, B, C):
    M = []
    linhas = len(M)
    colunas = len(M[0])
    for i in range[linhas]:
        for j in range[colunas]:

            #Funcao (a) de 1
            transposta(A)
            imprimeMatriz(A)

            #Funcao B de 1
            traco(A)
            imprimeMatriz(A)

            #Funcao C de 1
            traco_secundaria(A)
            imprimeMatriz(A)

            #Funcao D de 1
            soma_mat(A, B)
            imprimeMatriz(A, B)

            #Funcao E de 1
            mult_escalar_mat(A)
            imprimeMatriz(A)

            #Funcao F de 1
            prod_mat(A, B)  
            imprimeMatriz(A)  


#############################################

def imprimeMatriz(M):
    l, c = dimensao(M)
    for i in range(l):
        for j in range[c]:
            print(M[i][j], end="\t")
        print()

#############################################

def dimensao(M):
    l = len(M)
    c = len(M[0])
    if (l != 0):
        return l, c
    return False 

#--------------------------Exercicio_3_4
#--------------------------Exercicio 3
#Algoritmo 1 de 3

def forma_escalonada():
    return

#Algoritmo 2 de 3

def forma_escalonada_reduzida_por_linha():
    return

#Alinea (a) de 3

def primeira_col_nao_nula():
    return

#Alinea (b) de 3

def troca_linhas():
    return

#Alinea (c) de 3

def cria_zeros():
    return

#Alinea (d) de 3

def elimina_linha_1():
    return

#Alinea (e) de 3

def forma_escalonada():
    return

#Alinea (f) de 3

def  forma_escalonada_reduzida():
    return

#Alinea (g) de 3

def gauss_jordan():
    return

#--------------------------Exercicio 4

gauss_jordan()

#--------------------------Exercicio_5_6
#--------------------------Exercicio 5
#Alinea (a) de 5

def posto():
    return

#Alinea (b) de 5

def sistema_eq_linear():
    return

#--------------------------Exercicio 6
#Funcao (a) de 5

posto()

#Funcao (b) de 5

sistema_eq_linear()

#--------------------------Exercicio_7_8
#Exercicio 7

def determinante():
    return

forma_escalonada()

#Exercicio 8
#Funcao de 7

determinante()