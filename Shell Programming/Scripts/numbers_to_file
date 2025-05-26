#!/bin/bash 

#creo un file chiamato pari

touch pari 

#inizializzo il conto, facendo partire la conta da 1 
n=1

#struttura while per la conta, finchè n è minore o uguale di 30

while test $n -le 30
do

#mostra in output il numero contato

echo $n

#controlla se il numero contato è pari, ovvero se il calcolo del reto della divisione n/2 è pari a 0

if test $[$n % 2] -eq 0

# se il numero contato è pari, lo inserisco nel file pari

then echo $n >> pari
fi

#aggiorno il conto

n=$[$n+1]

done

# notifica all'utente che il conto è finito 

echo Conto Finito!
