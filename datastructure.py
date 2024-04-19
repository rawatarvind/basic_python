

####################

# list => list is a collection of multiple items(objects).

# list : [ ] 
# list : based on index : start: 0, end (n-1)
# list : homo,hetro,duplicate
# list : mutable : add,update,delete


x=[33,"arvind",345,"vivek",3433434,"Delhi",948,93094,"noida","sam",234,24345,"king"]

print(x[5])
print (x[-2])

# slice: [start:end:steps] # end-1, steps: +1

print(x[1:5])

print(x[1:8:2])

print(x[-1:-4:-1])

x[1]="deepak"
print(x)

del x[3]
print(x)
###############################################

# function vs method 
# function is a task and method is a behaviour.
# method is always associated with object but function does not, and method is  always  call with .(dot).

# append method is used to add the object in end of the index but only one value can add.
# we can append the list also.


#print(dir(list))

x.append(56)
print(x)

#x.append([34,45,43])
#print(x)


###    insert object before the index.

x.insert(0,34)
print(x)


### extend, append, and insert are used to  add objects in the list.

x.extend([34,45,64,32])
print(x)



# index method

x.index("Delhi")
print(x)
#############################################################################

## cello copy: that means we refer same copy.

y=x 

y[1]=345

print(y)


#######################################################

# TUPLE : collection of objects 
# tuple : base on index:
# home,hetro,duplicate
# immutable

#x=(101,"amit",23,"delhi",2432432)

#y=(23,42,23,422,13,444,5552,23,4)

#print(x[3])


##############################

print(dir(tuple))


## how to convert list to tuple and tuple to list

# x=(101,"amit",23,"delhi",2432432)

# y=list(x)

# print(y)

# or

# x=(101,"amit",23,"delhi",2432432)

# y=tuple(x)
# print(y)


########################


A=(101,"amit","vivek",32,[101,102,103])

B=(A[4][2])=123
print(A)

##############################################

# Dictionary => data are stored in key value pair,
# dict: collection of keys and values.
# dict: {key:value,key:value} 
# dict:(key) : immutable
# dict: duplicate keys are not allowed.
# dict: mutable


d1={'id':101,'name':'amit','city':'Delhi','age':23,}

print(d1.get('salary',25000))


del d1['city']

print(d1)

d1.setdefault('salary',45000)
print(d1) 

k=list(d1.keys())
v=list(d1.values())
it=list(d1.items())


for x in d1.items():
  print(x)

for x in d1.keys():
 print(x)

d1.clear

print(d1)


# Que => access deepak from given dict.

d2={'people':[{'india':[{'id':101,'name':'amit'},{'id':102,'name':'deepak'}]}]} 


