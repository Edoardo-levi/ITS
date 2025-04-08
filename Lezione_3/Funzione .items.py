dict= {1: 'ciao', 2: 'come',3: 'stai'}
for key, value in dict.items(): # con la funzione .items, mi ritrona una lista di tuple
                                #al posto di un dizionario USATA SOLO PER I DIZIONARI
    print(key, value)           #1,2,3 (key)
                                # ciao, come, stai (value)