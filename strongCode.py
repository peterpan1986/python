#! python3
# strongOrder

import re

def strongOrder(order):
    #orderRegex1=re.compile(r'([a-zA-Z0-9]{8,})')
    length=len(order)
    #chpw1 = re.compile(r'.*[A-Z]+.*')
    #chresult1 = chpw1.search(passwd)
    #print("匹配大写字符",chresult1)
    orderRegex2=re.compile(r'([a-z]+)') 
    orderRegex3=re.compile(r'([A-Z]+)')
    orderRegex4=re.compile(r'(\d+)')
    if length<8:
        print('Code is less than 8!')
        return False
    elif orderRegex2.search(order)==None:    
        print('Code must include a-z!')
        return False
    elif orderRegex3.search(order)==None:
        print('Code must include A-Z!')
        return False
    elif orderRegex4.search(order)==None:
        print('Code must include one number')
        return False
    else:
        print('It\'s a strong code!')
        return True
    
while True:
    pw=input('Pls enter the code:')
    if strongOrder(pw)==True:
        break
    
    
