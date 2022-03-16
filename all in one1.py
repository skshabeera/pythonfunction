def arm():
    sum=0
    a=n1
    while a>0:
        b=a%10
        sum=sum+b**3
        a=a//10
    if n1==sum:
        return (n1,"arm strong")
    else:
        return (n1,"not armstrong")
n1=int(input("enter num"))
def harshad():
    sum=0
    c=num
    r=0
    while c>0:
        r=c%10
        sum=sum+r
        c=c//10
    if num%sum==0:
        return (num,"harshad num")
    else:
        return (num,"notharshad num")
num=int(input("enter num"))
def perfect():
    sum=0
    i=1
    while i<n:
        if n%i==0:
            sum=sum+i
        i=i+1
    if sum==n:
        return (n,"perfect")
    else:
        return (n,"notperfect")
n=int(input("enter num"))
def prime():
    i=1
    c=0
    while i<n2:
        if n2%i==0:
            c=c+1
        i=i+1
    if c==1:
        return (n2,"prime number")
    else:
        return (n2,"not prime")
n2=int(input("enter num"))
def main():
    print(arm())
    print(harshad())
    print(perfect())
    print(prime()) 
main() 