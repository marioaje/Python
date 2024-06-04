mylista = ['mario', "Jimenez", 44, 10.1, True]
#            0    ,     1    ,  2,   3  ,  4
print(mylista)

print( mylista[1])
mylista[1]=input("Ingrese el valor: ")
print( mylista[0], mylista[1])
print(mylista)

mylista.append('Vivo en Costa Rica')
print(mylista)

mylista.pop()
print(mylista)