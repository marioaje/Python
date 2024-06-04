variable = open("demo.txt")
print(variable.read())  # lee todo el documento

print("///////////////////////////")
# puedo leer, la cantidad de caractertes.
variable = open("demo.txt")
print(variable.read(5))
# caso cuando es externo
# variable = open("//120-210-002/demo.txt")
# print(variable.read(5))
