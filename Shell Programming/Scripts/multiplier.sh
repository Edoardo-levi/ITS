#! /bin/bash

echo "Inserisci il primo numero: "

read n1

echo "Inserisci il secondo numero: "

read n2

risultato=$(($n1 * $n2))

echo "Il risultato della moltiplicazione tra $n1 e $n2 è= $risultato"

