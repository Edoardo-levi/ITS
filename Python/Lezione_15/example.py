PATH :str = "Python/Lezione_15/example.txt"
mode:str= "w"
encoding:str="utf-8"
file= open (PATH, mode)
print(file)

output:str= file.write("Hello world\n")
print(output)
file.close()