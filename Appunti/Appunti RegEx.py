'''
Mentre programmeremo ci capiterà di dover rappresentare dati con degli standard,
ad esempio un cf deve avere 16 cifre, come possiamo fare per rapresentare gli standard?
Useremo le RegEx (Regular Expression), che sono un insieme di simboli che identificano in un testo un gruppo di stringhe,
danno possibilità di trovare un pattern in una stringa.

Le RegEx hanno una serie id elementi, le prima che  andremo a vedere sono le Ancore:

--- "^" -> Andremo a trovare le righe che iniziano con quella parola:
    Esempio: ^Ciao caro utente^, cerca la linee che iniziano esattamente con quella stringa

---  "$" -> Andremo a trovare le righe che finiscono con quella stringa:
    Esempio: $Addio carissimo$, cerca le linee che finiscono esattamente con quella stringa

    
    QUANTIFIERS:

--- "*" -> cerchiamo tutte le stringhe che hanno in comunei caratteri tranne alpiù l'ultimo carattere:
    Esempio: abc*, andrà a considerare "ab", "abc", "abcc", "abccccccc", etc

--- "+" -> cerchiamo tutte le stringhe che hanno in comune tutti i caratteri compreso almeno uno dell'ultimo:
    Esempio: abc+, considererà "abc", "abcccccc", ma non "ab"
    
--- "?" -> 

--- "{n}" -> Conta quante volte compare una stringa:
    Esempio: abc{3}, considera "abccc" / a(bc){3}, considera "abcbcbc"

--- "{n,}" -> Almeno n volte:
    Esempio: abc{2}, considera "abcc", "abccc", "abcccc", etc

--- "{n, m}" -> Almeno tra n e m volte:
    Esempio: abc{2, 4}, considera "abcc", "abccc", "abcccc".

    
    WILDCARDS:

--- "." -> Ogni carattere in mezzo:
    Esempio: a.c, considera "abc", "afc", "a^c", non "abbbc" o "ac"

--- ".*" -> Tanti caratteri tra x e y:
    Esempio: a.*c, considera "ac", "acjnnfsvnc", etc

--- ".+" -> Tra x e y ci deve essere almeno un carattere:
    Esempio: a.+c, considera "afc", "assvfdcdcdsc", non "ac"

    
    OPERATORS:

--- "|" -> Alternanza:
    Esempio: cane|gatto, considera "cane", "gatto" e "canegatto", non "caneuvdjcgatto"

--- "(...)" -> Cattura = permette di creare dei gruppi a cui possiamo fare sempre riferimento:
    Esempio: (abc)+, considera "abc", "abcabc" etc, non "abcabd". Le parentesi creano dei gruppi su cui possono agire altri operatori.
    Da usare quando devo solo trovare una data sequenza che sappiamo si ripresenta nel codice

--- "(?:...)" -> Gruppi che non catturano = non catturano il riferimento del testo:
    Esempio: (?:abcd)+, considera "ab", "cd", "abcd", "abcdabcd" etc.
    Da usare se mi serve trovare un pattern logico

--- (?=...) -> Positive lookhead:
    Esempio: a(?=b), considera "a" solo se il carattere successivo è "b"

--- (?!...) -> Negative lookhead:
    Esempio: a(?!b), considera "a" solo se il carattere successivo non è "b"


    CLASS CHARACTER:

--- [...] : considera ogni singolo carattere dei caratteri inseriti dentro le parentesi
    Esempio: gr[ae]y, considera sia "gray" che "grey" 

--- [a-z][A-Z] : considera singolarmente ogni carattere compreso tra i caratteri tra parentesi
    Esempio: [a-z][A-Z], considera i casi in cui il primo carattere è minuscolo e il secondo è maiuscolo

--- [0-9] : considera una cifra tra 0 e 9

--- [^abc] considera tutto tranne quello a, b o c; il "^" significa "non"

--- [a-zA-Z0-9_] considera ogni lettera, numero o trattino

--- "\d" : considera ogni singolo numero
    Esempio: \d\d, cosnidera "42" o "99" o "22" etc.

--- "\D" : considera ogni carattere che non sia numero
    Esempio: \D, considera "abcdef", "dfavf" etc, non "341"

--- \w : consdera ogni letera maiuscola, minuscola, numero o trattino, spazi e caratteri speciali non inclusi (equivalente [a-zA-Z0-9_])
    Esempio: \w, considera "Hello_123"

--- \W : non considera nessun carattere tranne i caratteri speciali, equivalente di [^a-zA-Z0-9]
    Esempio: \W, considera solo spazi e simboli come "!, #, %, etc"

--- \s : considera ogni spazio, tab, invio etc
    Esempio: \s, considera " ", "\n"

--- \S : considera caratteri che non sono spazi, tab o invio
    Esempio: \S, considera tutto tranne che i caratteri


Per usare le RegEx in python occorre prima importare la librearia re.'''

import re

testo="La mia mail è edoardovale2003v5@gmail.com"
risultato=re.findall(r'\S+@\S+', testo)
print(risultato) # grazi al carattere +, l'output è soltanto la parte prima e dopo la chiocciola


risultato2=re.match(r'[A-Z][a-z]+', testo)  # "match" controlla se avviene un match all'inizio della stringa
print(risultato2.group()) # con .group non viene stampato l'oggetto "La" ma soltanto i caratteri che hanno fatto match


risultato3=re.findall(r'[0-9]+', testo)   # considera tutti i caratteri numerici
print(risultato3)

'''
come match e findall esistono altri metodi della libreria re:
- search
- fullmatch
- sub: rimpiazza il match che trova con una stringa
- finditer -> restituisce oggetto -> occorre usare .group
- split: splitta una stringa in più stringhe quando trova un match
- compile

Per vedere esempi, vedi slide 17 e 18, ppt RegEx
'''

esempio="il codice è: 123-abc"
match=re.search(r'(\d+)-([A-Z]+)', esempio)

if match:
    print("Intera corrispondenza:", match.group(0))
    print("Gruppo 1 (numeri): ", match.group(1))
    print("Gruppo 2 (lettere): ", match.group(2))