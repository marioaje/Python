#Personas
#Clase persona, atributos y funciones
class Persona:
#Primero se crea el inicializador de los datos
    def __init__(self, nombre):
        self.nombre = nombre
        #Se necesitan 6 nuevos atributos
        #email, apellido, fecha nacimiento, telefono, provincia

#Creo la funcion que muestre los datos        
    def getNombre(self):
        print(self.nombre)

#Cambiar o ajustar los datos
    def setNombre( self, nombre):
        self.nombre = nombre

#evalua formato de correo electronico        

#Se requieren los set y gets email, apellido, fecha nacimiento, telefono, provincia        
#Se requiere una funcion que calcule la edad, con base a la fecha de nacimeiento
#se necesita una funcion que imprima toda la informacion agregada.
#Fin de la clase
#se requiere una funcion que valide si el correo electronico posee el siguiente formato, @cursopython.com, esto con el fin de evaluar el formato del correo.

Usuario = Persona("Mario")
Usuario.getNombre()

texto = "Clase 24 abril dOs Mil"
print(texto)
print(texto.upper())