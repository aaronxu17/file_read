## read a file from command
## count the number of float numbers
## compute the sum of numbers
## if there exists non-number, omit it, only count numbers
import os
import os.path
import io, sys

Max_File_Size = 1000000 # MB,1TB
print "Type the filename:"
filename = raw_input("> ")

def isNumber(number):
    try:
        float(number)
        return True
    except ValueError:
        return False
        

if os.path.isfile(filename) and os.access(filename,os.R_OK):
    if float(os.path.getsize(filename))/(1024*1024)> Max_File_Size:
        print "File is too large!"
    else:
        try:
            file = open(filename)
        except IOError:
            print 'cannot open file',filename
        else:
            content=file.readlines()
            numsum= 0.0
            numcount=0

            for line in content:
                for item in line.split():   
                    item_is_number = isNumber(item)
                    while item_is_number:
                        try:
                            numsum+=float(item)
                        except:
                            print 'Overflowed! '
                        else:    
                            numcount+=1
                            item_is_number=False

                    
            print numsum
            print numcount    
else:
    print "Cannot manipulate the file"
            

