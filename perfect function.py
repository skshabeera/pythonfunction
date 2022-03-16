def ek_perfect():
    sum=0
    i=1
    while i<n:
        if n%i==0:
            sum=sum+i
        i=i+1
    if sum==n:
        print(n,"perfect number")
    else:
        print(n,"is not perfect number")
n=int(input("enter the number"))
ek_perfect()