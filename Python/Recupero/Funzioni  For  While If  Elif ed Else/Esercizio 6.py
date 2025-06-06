"""Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 2, 4, 6, 8, 10, 12, 14
b) 1, 4, 7, 10, 13
c) 30, 25, 20, 15, 10, 5, 0
d) 5, 15, 25, 35, 45"""
list1=[]
list2=[]
list3=[]
list4=[]
for i in range (2,16,2):

    list1.append(i)
print(f"A) {list1}")

for j in range (1,14,3):
    list2.append(j)
print(f"B) {list2}")

for k in range (30,-5,-5):
    list3.append(k)
print(f"C) {list3}")

for t in range (5,55,10):
    list4.append(t)
print(f"D) {list4}")