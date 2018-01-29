#! python3
# findTheText(): Open all the ".txt" files. find all the lines which include the input text.

import re, os

path='F:\\python\\book1\\test'
fileNameList=os.listdir(path)
finding=input('Enter the word:')
for fileNameString in fileNameList:
    mo=re.compile(r'.+\.txt$').search(fileNameString)
    if mo ==None:
        continue
    else:
        textFileString=open(os.path.join(path,mo.group())).read()
        #resultList=re.compile(r'\d{3}).findall(txtFileString)
        resultList=re.compile(finding).findall(textFileString)
        print('\n'.join(resultList))
                              


