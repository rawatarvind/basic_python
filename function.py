
#def fun_name(args):
    # code

def msg():
  print("welcome to vehant")


msg()


def add(x,y):
  z=x+y
  print(z)

a=int(input("Enter a number : "))
b=int(input("Enter a nuber : "))

add(a,b)

def info(id,name,age):
  print("id is :",id)
  print("name is :",name)
  print("age is :",age)

info(101,"amit",45)

# Required paramete which function doesn't have any value. that is called the required parameter.


# name args (keyword)

info(age=24,id=101,name="amit")

####################  variable lenth arguement .##############################

def add(*x):
  result=0
  for i in x:
    result=result+i
  return result


a=add(3,4,5)

print(a)

############## variable lenth arguement with keyword ########################

def adduser(**var):
      print(var)

adduser(password="redhat",username="root")


# Types of variable local: inside function  and global: outside function



 
