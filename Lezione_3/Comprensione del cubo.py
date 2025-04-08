''' usa una comprensione di elenco per generare un elenco dei primi 10 cubi.
'''

# Cubi usando la comprensione del list
cubi = [x**3 for x in range(1, 11)]
print(*cubi)
