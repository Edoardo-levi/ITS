"""Scrivi una funzione che verifica se in una stringa le parentesi 
'(' e ')' sono bilanciate, cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude."""

def check_parentheses(expression: str) -> bool:
   

    for par in expression:
        if par =='(':
           for j in expression:
               if j== ')':
                   verifica=True
               else:
                   verifica=False
                
                    
    return verifica

print(check_parentheses("(()()))()"))
print(check_parentheses("()()())()()()()"))
print(check_parentheses("()()()()()()()()()()()()"))