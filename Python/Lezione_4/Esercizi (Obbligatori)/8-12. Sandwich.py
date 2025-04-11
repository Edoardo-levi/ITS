'''scrivi una funzione che accetti un elenco di elementi che una persona desidera in un sandwich. 
La funzione dovrebbe avere un parametro che raccolga tutti gli elementi forniti dalla chiamata di 
funzione e dovrebbe stampare un riepilogo del sandwich ordinato. Chiama la funzione tre volte, 
utilizzando ogni volta un numero diverso di argomenti.'''



def sandwich(*args):
    print("Ordine dei sandwich:")
    for ingrediente in args:
        print(f"- {ingrediente}")
    


sandwich("pane integrale", "prosciutto", "formaggio", "lattuga")
sandwich("pane bianco", "tonno", "pomodoro", "maionese")
sandwich("pane ai cereali", "pollo", "avocado")
