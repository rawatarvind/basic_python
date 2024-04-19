
# find index number for all value (Dehli) ? 

list = [101,"amit",23,"Dehli",39493,"Dehli"]

value="Dehli"

indices = []

for index in range(len(list)):
  if list[index] == value:
     indices.append(index)
print(indices)
