def prime():
    n=int(input("enter the number"))
    i=0
    while i<=n:
        if n%i==0:
            c=c+1
        i=i+1
    if c==2:
        return n,"it is a prime number"
    else:
        return n,"it is not a prime number"
# n=int(input("enter the number"))
def armstrong():
    a=int(input("enter the number"))
    sum=0
    b=a
    while b>0:
        sum+=a**3
        b=b//10
    if a==sum:
        return(a,"is armstrong number")
    else:
        return(a,"is not armstrong number")
# a=int(input("enter the number"))
def harshad ():
    b=int(input("enter the number"))
    s=0
    m=b
    r=0
    while b>0:
        r=m%10
        sum=s+r
        m=m//10
    if m%sum==0:
        return(m,"is harshad number")
    else:
        return(m,"is not a harshad number")
# b=int(input("enter the number"))
def perfect():
    c=int(input("enter the number"))
    i=0
    sum=0
    while i<=c:
        sum1=sum+i
        if i%c==0:
            return(c,"is perfect number")
        else:
            return(c,"is not perfect number")
        i=i+1
def main ():
    print(n ,"is prime")
    print(a,"is armstong")
    print(m,"is harshad")
    print(c,"is perfect")
main()
prime()
armstrong()
harshad()
perfect()