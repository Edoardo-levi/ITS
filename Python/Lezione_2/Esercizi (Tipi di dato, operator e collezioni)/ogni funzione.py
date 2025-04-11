'''pensa a cose che potresti archiviare in una lista. Ad esempio, 
potresti creare una lista di montagne, fiumi, paesi, città, lingue o qualsiasi altra 
cosa tu voglia. Scrivi un programma che crei una 
lista contenente questi elementi e poi utilizzi ogni funzione
introdotta in questo capitolo almeno una volta.'''


montagne = ["Everest", "K2", "Kangchenjunga", "Lhotse", "Makalu"]
fiumi    = ["Nilo", "Po", "Tevere", "Gange", "Danubio"]
paesi    = ["Italia", "Francia", "Giappone", "Canada", "India"]


print("Le liste trovate sono:\n")
print(*montagne, sep=", ", end="\n")
print(*fiumi, sep=", ", end="\n")
print(*paesi, sep=", ")

montagne.sort()
fiumi.sort()
paesi.sort()

print("Le liste scritte in ordine alfabetico sono:\n")
print(*montagne, sep=", ", end="\n")
print(*fiumi, sep=", ", end="\n")
print(*paesi, sep=", ")


montagne.reverse()
fiumi.reverse()
paesi.reverse()

print("Le liste scritte in ordine alfabetico contrario sono:\n")
print(*montagne, sep=", ", end="\n")
print(*fiumi, sep=", ", end="\n")
print(*paesi, sep=", ")

montagne.append("Alpi")
fiumi.insert(2,"Ticino")
paesi.pop(3)

montagne.sort()
fiumi.sort()
paesi.sort()
print("\n")
print(*montagne, sep=", ", end="\n")
print(*fiumi, sep=", ", end="\n")
print(*paesi, sep=", ")


lunghezza= len(montagne)
lung= len(paesi)
lennght= len(fiumi)

print(f"la lunggezza della lista dei fiumi e':\n{lennght}")
print(f"la lunggezza della lista dei paesi e':\n{lung}")
print(f"la lunggezza della lista delle montagne e':\n{lunghezza}")