######################1st way to import the module ##############

from module import msg,name

msg()

print(name)

############2nd way to import the module #################
from module import *
 

msg()
add(4,5)
print(name)

#####################3rd way to import the module ###############

import module as md

md.msg()
md.add(4,5)
print(md.name)


######################## 4th way ##################################

import module 

module.msg()
module.add(4,5)
print(module.name)

######## To install module via pip #################


