## read a file from command
## count the number of float numbers
## compute the sum of numbers

import io


print "Type the filename:"
filename = raw_input("> ")

file = open(filename)
content=file.readlines()

numsum=0.0
numcount=0
for line in content:
    for item in line.split():
        numsum+=float(item)
        numcount+=1
        

print numsum
print numcount      

