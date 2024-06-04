#Si condicional, nos permite entregar una respuesta personaliza
variable = 1 > 2
#print(variable)
a=2000
b=22


if a == b:
    mensaje = f"""El valor de {b} es igual que {a} """
    print ( mensaje )#true
elif a < b:
    mensaje = f"""El valor de {b} es mayor que {a} """
    print ( mensaje )#true    
else:
    mensaje = f"""El valor de {a} es mayor que {b} """
    print (mensaje)#false  





# if a < b:
#     mensaje = f"""El valor de {b} es mayor que {a} """
#     print ( mensaje )#true
# else:
#     mensaje = f"""El valor de {a} es mayor que {b} """
#     print (mensaje)#false    

# login = "mariosss"
# password = "mario"
# if login == password:   
#     print("Bienvenido al sistema...") 
# else:
#     print("Usuario o clave incorrecta")    