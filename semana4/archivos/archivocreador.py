#Permite que pythpm te cree un archivo
fileOpen = open("fileOpen.txt", "a")
fileOpen.write("Un nuevo texto desde python")
fileOpen.close()
# a= append
# w= write
# r= read
archivocrear = open("archivocrear.sql", "a")
archivocrear.write("select * from datos")
archivocrear.close()

fileOpen = open("demo.txt", "w")
fileOpen.write("Un nuevo texto desde python reescribiendo")
fileOpen.close()