## read a file from command
## count the number of float numbers
## compute the sum of numbers
## if there exists non-number, omit it, only count numbers

import io


print "Type the filename:"
filename = raw_input("> ")

file = open(filename)
content=file.readlines()

numsum=0.0
numcount=0

def isNumber(number):
    try:
        float(number)
        return True
    except ValueError:
        return False
        
for line in content:
    for item in line.split():
        item_is_number = isNumber(item)
        while item_is_number:
            numsum+=float(item)
            numcount+=1
            item_is_number=False
            
print numsum
print numcount      

