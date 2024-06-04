variable = open("demos.txt", "r")

# print(variable.readline())
# print(variable.readline())
# print(variable.readline())
#print(variable.readline())
contador = 0
for x in variable:
    contador = contador+1
    if (contador == 4):
        print(x)