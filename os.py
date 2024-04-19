import os
 
print(os.getcwd())  # get current working dir.

os.chdir("/home/sarvind/Desktop/")  # To change the current dir path.

print(os.getcwd())

#os.mkdir("dir1") # To make the dir.

#os.makedirs("/home/sarvind/Desktop/python/files")

#print(os.rmdir("dir1")) # empty dir
# os.removedirs("python/files") #empty dir

# os.removefile("dir1/abx.xyz")

# os.rename('abc.txy','newfile.txt')

data=os.listdir('/home/sarvind/Desktop')
print(data)

data1=os.walk("/home/sarvind/Desktop")

for c,d,f in data1:
  print("cwd : ",c)
  print("dirs : ",d)
  print("filess : ",f)

x=os.stat("abc.txt")

print(x)

import time

t=x.st_atime

print(time.ctime(t))


m=x.st_size

print(m)

n=x.st_mode

print(oct(n))

os.chmod("abc.txt",0o777)


file='/home/sarvind/Desktop/abc.txt'

#print(os.path.basename(file))

#print(os.path.dirname(dir))

#os.path.join("users","admin","movies")

#os.path.getsize("abc.txt") # get size of file or dir in bytes.

#os.path.getctime('abc.txt')
#os.path.getatime('abc.txti')




#file1==input("Enter name : ")

# if os.path.exists(file):
# if os.path.isdir(file):
# if os.path.isfile(file):
# if os.path.islink(file):
# if os.path.ismount(file):
#    print("exists")
#  else: 
#    print("not exists")


################# shutil module is used to copy and move the data locally not for remote. #############################

import shutil

#shutil.copy("/home/sarvind/Desktop/abc.txt","/mnt/Data/")
#shutil.copyfile("/home/sarvind/Desktop/alldata.txt","/home/sarvind/Desktop/abc.txt")
#shutil.copytree("/home/sarvind/client","/mnt/Data2/")

#shutil.move("/home/sarvind/Desktop/xyz.txt","/mnt/Data/")


print(shutil.get_archive_formats())

shutil.make_archive("/home/sarvind/Desktop/python","zip","/mnt/Data2/")
