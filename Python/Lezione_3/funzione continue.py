start: int = 0
end :  int = 10
step:  int = 2
for index in range(start, end):
    if index % 2 == 1:
        
        continue                # quello che c'è dopo il continue non viene calcolato
                                # se la condizione dell'if è vera, il continue salta quello che c'è dopo
    print (index)