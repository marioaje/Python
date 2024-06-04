import os
variable = "demo.txt"
if os.path.exists(variable):
    print("El archivo fue encontrado", variable)
    os.remove(variable)
    print("El archivo fue eliminado", variable)
else:
    print("no existe un archivo con ese nombre")
        