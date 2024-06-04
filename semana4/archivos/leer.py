import csv

# demos= open("grupo.csv","r")
# print(demos)
with open("grupo.csv", newline='') as File:
    reader = csv.reader(File)
    for fila in reader:
        print(fila)
