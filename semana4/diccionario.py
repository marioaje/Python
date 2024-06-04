class diccionario:

    def __init__ (self):
       self.listadatos = [] 

    def muestredatos(self):
        return self.listadatos


#diccionario es a quel que agrupa n cantidad de valores
sopyvariable ="mario"

mydiccionario = {
    "nombre": sopyvariable,
    "apellido": "Jimenez",
    "estado": True
}
#casado
mydiccionario2 = {
    "nombre": "Isaac",
    "casado": True,
    "apellido": "Jimenez",
    "estado": True,
    "fecha": "2023"
}
#0 , 1,2,3,4
arreglo = [ 
    "Mario",
    True,
    "2023",
    True,
    "Jimenez"
]

arreglo2 = [ 
    "Isaac",
    "Jimenez",
    True,
    "2023",
    True
]

arreglos = [ arreglo, arreglo2]



soyarreglo = [ mydiccionario, mydiccionario2]

#un arreglo es un matriz unimedimensional, que permite alcenar datos
#arreglo[0 ,"mario"]

#list de diccionario es un matriz multimed

#print(mydiccionario["nombre"])
# print (arreglos[0][1])
# print(soyarreglo[0]["apellido"])
# print(mydiccionario)
#print(soyarreglo)


for item in soyarreglo:
    print("Key o elemento de la lista", item["apellido"])