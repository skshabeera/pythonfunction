def add(list):
    a=[]
    i=0
    while i<len(list):
        if list[i]%2!=0:
            a.append(list[i])
        i+=1
    return a
d=add([1,2,3,4,5,6,7,8,9,10])
def greater():
    j=0
    while j<len(d):
        if d[j]>5:
            print(d[j])
        j+=1
greater()
