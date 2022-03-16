def strong_password(password):
    capital_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_letters="abcdefghijklmnopqrstuvwxyz"
    special_characters="@#$&*!%^_-"
    numerics="0123456789"
    sum=0
    a=0
    b=0
    c=0
    d=0
    if len(password)>5 or len(password)<17:
        print("password length shoulb be 6 to 16=")
        user_password=input("enter the password")
    for i in range(len(user_password)):
        if user_password[i] in capital_letters:
            a=1
        elif user_password[i] in small_letters:
            b=1
        elif user_password[i] in special_characters:
            c=1
        elif user_password[i] in numerics:
            d=1
    sum=a+b+c+d
    if sum==4:
        # print("password should be present capital_letters,small_letters,special_letters,numerics")
        print(  "correct password")
    else:
        print(" wrong  password ")
user_password=input("enter the password")
strong_password(user_password)
         