list_1: list = ["ciao", "come", "stai"]
list_2 : list= [42,98]



for index in range(len(list_1)):
    
    if index < len(list_2):
    
        print (list_1[index], list_2[index])
        
        
    else:
        print (list_1[index])
        
      
# questo programma genera un errore in quanto la prima lista è più lunga della secoda
# per evitare che il progranma vadi in errore, utilizzo gli if      

