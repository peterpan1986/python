#! python3
# mad_Libs

import re

f1=open('a.txt','r')
strf1=f1.read()
print("The content of the original:")
print(strf1)

strf1_list=strf1.split(' ')
f1.close()

replist=re.findall(r'[\'\"]?[A-Z]{2,}[\,\.\?\!\'\"]?',strf1)
print("these are the words should be replaced")
print(replist)
print()
for rep in replist:
    inputstr=input("Enter a %s:" % rep)
    print(inputstr)

    inputstr=re.sub( r'([\'\"])?[A-Z]{2,}([\,\.\?\!\'\"])?',r'\1'+inputstr+r'\2',rep)

    print(inputstr)

    strf1_list.insert(strf1_list.index(rep),inputstr)

    strf1_list.remove(rep)

newstr= ' '.join(strf1_list)
print("The words after subsitituted")
print(newstr)

f2=open('b.txt','w+')
f2.write(newstr)
f2.close()
f3=open('b.txt','r')
print(f3.read())
f3.close()
