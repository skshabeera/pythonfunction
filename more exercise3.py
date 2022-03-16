def max():
    if num1>num2 and num1>num3:
        print("num1 is maximum")
    elif num2>num1 and num2>num3:
        print("num2 is maximum")
    elif num3>num2 and num3>num1:
        print("num3 is maximum")
    else:
        pass
num1=int(input("enter the number"))
num2=int(input("enter the number"))
num3=int(input("enter the number"))
max()