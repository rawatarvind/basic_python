
import os
import glob

files=os.listdir("/home/sarvind/Desktop/")

#print(files)

files1=glob.glob("/home/sarvind/Desktop/**/*.txt",recursive=True)

print(files1)

with open("/home/sarvind/Desktop/alldata.txt",'a') as f:
  for file in files1:
     with open(file,"r+") as f1:
       f.write(f1.read())
       f1.truncate(0)


