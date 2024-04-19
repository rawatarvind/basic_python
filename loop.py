

# loops are used to repeated task.

# range(start,end,steps)

# Start : default => 0, End => end-1(means last step will be always excluded), Steps=> default => +1

# range(10) => [0-9] =>  [0,1,2,3,4...9]
# range(3,9) => [3-9] => [3,4,5,6,7..9]
# range(1,20,2) => [1-20] => [1,3,5,7....19]
# range(10,1,-1) => [10-2] => [10,9,8,7.....2]

A=list(range(10,5,-1))
print(A)

# Type of loops : for, while, for loop is used to fix iteration when you know. while loop is used when you don't know the no of iteration and loops are condition based.

###########################################


# for var in seq:
  # code

# seq: list,tuple,dict,set,string

# for loop is associated  with sequence.

#for var in "deepak","amit":
    #print("hello")

#for var in "deepak":
 # print("hello")


# while loop

#while condition:
  #code



#for x in range(1,11):
# print(x)


#y=1

#while y<=10:
#  print(y)
#  y=y+1 




y=10 
while y>=0:
 print(y)
 y=y-1



name=None

while name!="root":
  name=input("Enter username : ")


#############################
# break is used to current iteration to break.


for x in range(5):
 if x==3:
  break
 print(x)


################################


while True:
 name=input("Enter username :")
 if name=="root":
   print("Welcome root!")
   break

###############

# continue is used to skip the current iteration in loop.

for x in range(5):
  if x==3:
   continue
  print(x)

#######################

# pass is used to null statement.

if 3>4:
  pass

else: 
  print("false")
