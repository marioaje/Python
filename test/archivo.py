f = open("demofile.txt", "r")
print(f.read())

#Return the 5 first characters of the file:
f = open("demofile.txt", "r")
print(f.read(5))


f = open("demofile.txt", "r")
print(f.readline())

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())


f = open("demofile.txt", "r")
for x in f:
  print(x)

f = open("demofile.txt", "r")
print(f.readline())
f.close()  
# f = open("D:\\myfiles\welcome.txt", "r")
# print(f.read())
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists