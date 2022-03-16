def main(num1,num2):
    if user=="add":
        add(num1,num2)
    elif user=="sub":
        sub(num1,num2)   
    elif user=="mul":
        mul(num1,num2)
    elif user=="div":
        user(num1,num2)
def add(num1,num2):
    print(num1+num2)
def sub(num1,num2):
    print(num1-num2)
def mul(num1,num2):
    print(num1*num2)
def div(num1,num2):
    print(num1%num2)  
user=input("add,sub,mul,div")
num1=int(input("enter num"))
num2=int(input("enter num"))
main(num1,num2)