
file = open('TheZenOfPython.txt','r')

lines = file.readlines()

for line in lines:
    print(line)

file.close()