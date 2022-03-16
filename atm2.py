def language():
    if user ==1:
        a="English"
    else:
        a="telugu"
    return user
user=int(input("choose your language 1.English \n 2.telugu"))
def pin_code():
    if user==1:
        i=0
        while i<3:
            pin=int(input("enter the four digit number"))
            if pin==2345:
                print("correct")
                break
            else:
                print("incorrect pin")
            i=i+1
        else:
            print("your card is blocked")
    else:
        i=0
        while i<3:
            pin=int(input("4 ankela sankya nokandi"))
            if pin==2345:
                print("me pin sari inadhi")
                break
            else:
                print("mee pin sari inadhi kadhu sari cheyandhi")
            i=i+1
    return pin    
code=pin_code()
def options():
    if user==1:
        if code==2345:
            amount=20000
            print("please press 1 for your balance enquiry")
            print("please press 2 for your deposit")
            print("please press 3 for your withdraw")
            print("please press 4 for your exit")
            option=int(input("what you want to like to choose"))
            if option==1:
                ans=amount,"your current balance"
            elif option==2:
                deposit=int(input("enter the how much amount you want to deposit"))
                ans=amount+deposit,"your current balance"
            elif option==3:
                withdraw=int(input("enter the how much amount would you want to withdraw"))
                ans=amount-withdraw,"your current balace"
            else:
                ans="collect your card"
                print("thank you for visit")
    else:
        if code==2345:
            balance=10000
            print("dayasesi 1 nokandi mee dabulu telusukovadaniki")
            print("dayasesi 2 nokandi mee dabulu banklo veyadaniki")
            print("dayasesi 3 nokandi me dabulu thisukovadaniki")
            print("dayasesi 4  nokandi meru atm vadhulutaku")
            option=int(input("meeku kavalisina option enchukondi"))
            if option==1:
                ans=balance,"mee dabulu chusukondi"
            elif option==2:
                a=int(input("dyasesi meku entha dabulu kavalo avi nokandi"))
                ans=balance-a,"dayasesi mee dabulu thisukondi"
            elif option==3:
                b=int(input("dayasesi meku enni dabulu kavalo avvi nokandi"))
                ans=balance+b,"mee dabulu mee accountlo dasiunchabadai"
            else:
                ans="mee card thisukondi"
                ans="dhanyavadhamulu meru atm ni dharsinchinandhuku"
            return ans
def main():
    print(language())
    print(options())
main()