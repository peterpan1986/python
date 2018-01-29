#! python3

import re

z=open('a.txt','r')
c=z.read()

red=re.compile(r'[A-Z]{2,}')
ss=red.findall(c)

for i in ss:
    print('Enter an %s' % i.lower())
    l=re.compile(r'%s'%i)
    p=str(input())
    c=l.sub(p,c)

print(c)
dk=open('new.txt','w')
dk.write(c)
dk.close()
z.close()
