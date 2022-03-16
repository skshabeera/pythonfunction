a=["my name is shabeera","i love chocolate"]
i=0
c=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if a[i][j]!= " ":
            pass
        else:
            c=c+1
        i=i+1
    j=j+1
    print(c)