#El for es como un contador, este ciclo tiene un inicio y un final
#son 10 elementos lo que va a contar
#0, 1 2 3 4 5 6 7 8 9
#1
# 2, 3, 4
#contador accedente
# for conti in range (1, 4 , 1):
#     print (conti)

contador = 0
#contador descendente
for conti in range (4 , 1, -1):
    contador = contador + 1
    contador += 1 #(contador + 1)
    
    print (conti) 
print ("Cantidad de elementos", contador)       