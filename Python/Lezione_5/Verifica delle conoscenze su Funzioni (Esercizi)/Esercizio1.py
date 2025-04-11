def prime_factors(n: int) -> list[int]:
    primi:list=[]
    numero=2
    while n>1:
        while n%numero==0:
            primi.append(numero)
            n//=numero
        numero+=1   
    return primi