import os 

#print(dir(os))

#print(help(os.chdir))


##################################

##  open function

# f=open(filename,mode)

#  mode 'r' : 'rt' read : default mode
#       'w' : 'wt' write : if file exits : override , if file does not exit : create
#       'a' : 'at' append : if file exits : append , if file does not exit : create 
#       'r+': 'rt+' : read and write : data does not override 
#       'w+': 'wt+" : write and read  : override the data



#   'rb', 'wb','ab','rb+','wb+','ab+' b: byte or binary

#f=open("/home/sarvind/Desktop/abc.txt",'w')

#print(f.name)
#print(f.mode)
#print(f.readable())
#print(f.writable())
#print(f.closed)

#f.close()
#print(f.closed)



#f1=open("/home/sarvind/Desktop/abc.txt",'w')

#f1.write("hello welcome to vehant")

#f1.close()

#f1=open("/home/sarvind/Desktop/abc.txt",'r')
#f1.readline()
#data=f1.read()
#data=f1.readline()
#data=f1.read(3) 
#data=f1.readlines() #list
#print(data)

#print(f1.read(7))
#print(f1.readline())
#print(f1.read(5))
#print(f1.read())
#print(f1.read())

# To move the cursor point to move in the text

# seek

#print(f1.read())
#f1.seek(0)
#print(f1.read())

with open("/home/sarvind/Desktop/abc.txt",'r') as f:



 print(f.closed)



