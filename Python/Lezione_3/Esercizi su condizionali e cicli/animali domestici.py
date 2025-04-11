'''crea diversi dizionari, dove ogni dizionario rappresenta 
un animale domestico diverso. In ogni dizionario, 
includi il tipo di animale e il nome del proprietario. 
Memorizza questi dizionari in un elenco chiamato animali domestici.
Quindi, fai un ciclo nell'elenco e, mentre
lo fai, stampa tutto ciò che sai su ogni animale domestico. '''
diz1={"razza": "Barboncino", "nome_prop": "Edoardo"}
diz2={"razza": "Maremmano", "nome_prop": "Letizia"}
diz3={"razza": "Cavalier King", "nome_prop": "Giorgia"}

animali_domaestici= [diz1, diz2, diz3]

for diz in animali_domaestici:
    print (f"razza razza:{diz['razza']} \n\
proprietario: {diz['nome_prop']}\n")