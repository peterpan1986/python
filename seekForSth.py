#!python3
# seekForSth.py

import os,re,shutil

src='F:/python/book1/test/a/'
dst='F:/python/book1/test/b/'
ftype='.'+input("Enter the file format:")
print(ftype)
count=0

for filename in os.listdir(src):
    if filename.endswith(ftype):
        shutil.copy(src+filename,dst)
        count+=1
        print('file ' +src +filename + '\t are copied to ---> ' +dst)

print("All the files in this document "+ftype+"are copied to "+dst)
print(str(count)+ ' files have been copied.')
            
    
