# String
# st[-3]
# st[1:4]
# string  is immutable item.

st="Welcome"

print(len(st))

#st[1]='t' # error
#####################################
####################################
# In Window  for path and url we can use double \\ or r .

#path="D:\\users\\sarvind\\newfile\\tmp\\abc.txt"

#& 

#path=r"D:\users\sarvind\newfile\tmp\abc.txt"

#print(path)


#x=int(input("Enter the number : ")
#y=int(input("Enter the number : ")

#z=x+y
#st="sum of {} and {} is {}".format(x,y,z)
#or 
#st=f"sum of {x} and {y} is {z}"
#print(st)

# replace method



x="$34"
y="57%"
z="12,482,00"

a=int(x.lstrip('$'))

print(a)

b=int(y.rstrip('%'))
print(b)


st="hello hi how are you"

c=st.replace('h','H')

print(c)

d=int(z.replace(',',''))

print(d)


# split method

st="Filesystem     Type      Size  Used Avail Use% Mounted on"

print(st.split())


########################

files=["abc.txt","file1.txt","dir1","image.png"]

for file in files:
  st=file.split(".")
  if st[-1]=="txt":
    print(file)

#############################

# join method

path=["path1","path2","path3","path4"]

new_path=":".join(path)

print(new_path)

########## lower, upper, swapcase, title & capitalize method. #########################

st="hello tHis pyThon class"

print(st.lower())
print(st.upper())
print(st.swapcase())
print(st.title())
print(st.capitalize())

################################
# convert string data to bytes.

x=b"hello"

print(x)

data="hello this is file data"
data.encode('UTF-8')

print(data)

y=b'hello this is file data'

d=y.decode()

print(d)





