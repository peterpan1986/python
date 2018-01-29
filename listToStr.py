def listToStr(something):
    for i in range(len(something)):
        if i==0:
            strings=str(something[i])
        elif i == len(something)-1:
            strings= strings+' and '+str(something[i])
        else:
            strings=strings+', '+str(something[i])   
    return strings

spam=[]
for i in range(3):
    spam.append(str(input("Input something:")))
print(listToStr(spam))
