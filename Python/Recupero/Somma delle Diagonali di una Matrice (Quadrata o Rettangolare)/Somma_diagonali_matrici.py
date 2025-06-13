"""Data una matrice 2D (lista di liste) di interi con dimensioni n X n, scrivi due funzioni:
1. sum_primary_diagonal(matrix) che restituisce la somma della “diagonale
primaria” (dall’angolo in alto a sinistra verso il basso a destra).
2. sum_secondary_diagonal(matrix) che restituisce la somma della “diagonale
secondaria” (dall’angolo in alto a destra verso il basso a sinistra).
Requisiti:
● Entrambe le funzioni accettano una lista di liste.
● Restituisci un intero per ciascuna funzione.
Esempi:
mat1 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
sum_primary_diagonal(mat1) # restituisce 1 + 5 + 9 = 15
sum_secondary_diagonal(mat1) # restituisce 3 + 5 + 7 = 15"""

def sum_primary_diagonal(matrix:list[list[int]])->int:
    somma:int=0
    somma_2=0
    for i in range(len(matrix)):
        somma+=matrix[i][i]
        counter=len(matrix)-1
        somma_2+=matrix[i][counter]
        counter-=1
    return somma,somma_2


print ("\nPrimo Test!")
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(sum_primary_diagonal(matrix1))
print("----------------------------------")


print("Secondo Test!")
matrix2 = [
    [10, 20],
    [30, 40]
]

print(sum_primary_diagonal(matrix2))
print("----------------------------------")

print("Terzo Test!")
matrix3 = [[99]]

print(sum_primary_diagonal(matrix3))
