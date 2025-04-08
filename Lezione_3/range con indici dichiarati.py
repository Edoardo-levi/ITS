start: int = 0
end :  int = 10
step:  int = 2
for index in range(start, end, step):
    if index % 2 == 0:
        print (index)

#Un'altro modo per scrivere un RANGE con i valori dichiarati