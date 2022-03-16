def prime ():
    a=int(input("enter the number"))
    i=1
    c=0
    while i<=a:
        if a%i==0:
            c=c+1
        i=i+1
    if c==2:
        print( a,"is prime number")
    else:
        print( a,"is not a prime number")
def armstrong():
    b=int(input("enter the number"))
    sum=0
    n=b
    while n>0:
        t=n%10
        sum+=t**3
        n=n//10
    if b==sum:
        print(b,"is a armstrong number")
    else:
        print(b,"is not a armstrong number")
def harshad():
    c=int(input("enter the number"))
    sum=0
    h=c
    while h>0:
        r=h%10
        sum=sum+r
        h=h//10
    if c%sum==0:
        print(c,"is harshad")
    else:
        print(c,"is not harshad number")
def perfect():
    e=int(input("enter the number"))
    j=1
    f=0
    while j<e:
        if e%j==0:
            f1=f+j
        j=j+1
    if f==e:
        print(e,"is perfect number")
    else:
        print(e,"is not a perfect number")
def main():
    prime()
    armstrong()
    harshad()
    perfect()
main()

    