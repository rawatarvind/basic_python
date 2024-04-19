 # list comprehension offers a shorter syntax when you mwant to create a new list based on the value of an existing list.


# print only even number in given list


data=[23,34,45,31,34,51,90,83,12,75]

even=[]

for x in data:
  if x%2==0:
   even.append(x)

print(even)


data1=[23,432,23,45,22,223,348,234,221,123,4,4234,233,2111,22]

new_list=[x    for x in data1  if x%2!=0]

print(new_list)



##################################


users=["amit","deepak","ram","sam","root"]

new_users=[]

for x in users:
  new_users.append(x.title())

print(new_users)


# 2nd 

new_data2=[x.title()   for x in users]  

print(new_data2)


###################################

gender=['M','F','M','F','M']

new_data3=[]

for x in gender:
 if x=="M":
     new_data3.append(1)
 else:
     new_data3.append(0)

print(new_data3)


#2nd


new_data4=[ 1 if x=="M"  else 0 for x in gender]

print(new_data4)

