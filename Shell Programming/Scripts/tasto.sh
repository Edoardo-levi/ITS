#! /bin/bash


#chiedere all'utente di inserire un tasto

echo "Premi un tasto e poi invio"

#salvo nella variabile tasto, il tasto premuto dall'utente

read tasto

#struttura per ananlizzare il tasto premuto 

case $tasto in 
# usiamo le ReGEX per verificare i vari casi di tasti premuti
[a-z] ) echo Lettera ;; #primo caso (il due ;; servono per chiudere un pattern e riaprilo un'altro)
[0-9] ) echo Numero ;;

* ) echo Punteggiatura, spaziatura o altro ;;

esac
