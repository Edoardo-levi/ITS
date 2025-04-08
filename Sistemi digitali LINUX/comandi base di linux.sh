#!/bin/bash

pwd
mkdir cartella_di_prova # creo una cartella chiamata cartella_di_prova
echo "------"
cd cartella_di_prova   # mi sposto all'interno della cartella_di_prova
echo "------"
pwd                    # stampo il percorso e contenuto della cartella 
touch file_di_test.py  # creo un file vuoto chiamato file_di_test
echo "------" 
ls                     # visualizzo il contenuto della cartella
mv file_di_test.py file_python.py # cambio il nome del file_di_test con file_python
ls
cd ..                  # torno alla cartella iniziale NON è cartella_di_prova
pwd                    # stampo il contenuto della cartella inizaiale
ls                     # visualizzo il contenuto della cartella 
rm -r cartella_di_prova   # rimuovo la cartella di prova
ls                        #visualizzo il contenuto della cartella e noto che non c'è più cartella di prova