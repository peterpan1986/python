def collatz(number):
    if number % 2 ==0:
        res=number//2
    else:
        res = 3*number +1
    print(res)
    return res


while True:
    try:
        num=int(input('Pls enter a number:'))
        if num==0:
            print("The number con't be 0")
            continue
        while num !=1:
            num=collatz(num)
        break
    except ValueError:
        print("It's not a number!")
        continue


