list1 : list = [0,1,2,3,4,5,6]

for index in range(len(list1)):     # vado a creare una lista di indici da scorrere
                                    # con la funzione len, ritorna l'intera lunghezza della lista quindi 7 
                                    # e non l'indice massimo che è 6
                                    #l'indicizzazione delle liste parte da 0 
                                    #nelll'indicizzazione di QUESTA  lista la posizione 7 non esiste
    print (list1[index])