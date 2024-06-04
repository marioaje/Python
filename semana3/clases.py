#las son segmento de codigo,
#que nos permite simplificar el desarrollo
#reutilizar codigo

#1-Un nombre (como se llama el archivo, el programa y modulo)
#class, palabra reservada.
class persona:
    #incializador del programa, clase
    #self hacia mi mismo, self es palabra reservada
    def __init__(self, cedula, nombre, apellido):#lo que esta adentro se le conoce como atributos
        #declaracion de atributos o variables asignadas a la clase
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.version = "2023"


        
    #funciones de retorno
    def devuelvacedula(self):
        print("la cedula es: ", self.cedula)

    def regresameelnombre(self):
        print("el nombre es:", self.nombre)

    def regresameversion(self):
        print("version es:", self.version)

    #funciones de ajuste, de cambio de valores.
    def cambiocedula(self, cedula):
        self.cedula = cedula
##########################################################################

# #aca se trabaja con la clase
# #nueva variable, del tipo clase
# variablea = persona("123", "Mario", "Jimenez")
# variableb = persona( 9, "Isaac", "Jimenez")
# variablea.devuelvacedula()
# variablea.regresameelnombre()
# variablea.regresameversion()
# nuevacedula = 32166
# variablea.cambiocedula(nuevacedula)
# variablea.devuelvacedula()
# variableb.devuelvacedula()
