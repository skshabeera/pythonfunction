def duplicate():
    list1=["shabeera","manasa","anusha","sindhu","manasa","shabeera"]
    i=0
    new=[]
    while i<len(list1):
        if list1[i] not in new:
            new.append(list1[i])
        i=i+1
    print(new)
duplicate()
