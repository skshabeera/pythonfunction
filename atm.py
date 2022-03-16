print("welcome to atm")
print("swipe card")
pin=1234
balance=20000

def fun1(language):
    if language=="English"  or language=="Hindi" or language=="Telugu":
        print("your language is accepted")
fun1("English")

def fun2(): 	
	i=0
	while i<3:
		pin=int(input("enter the pin number="))
		if pin==1234:
			print("Your pin number is correct")
			break
		else:
			print("Incorrect Pin try again!")		
		i+=1
	else:
    		print("Your card is block you reach out you limit!")

	return pin

pin=fun2()

def fun3():
	if pin==1234:
		account_type=int(input("enter the 1.current ,2. joint"))
		if account_type==1 or account_type==2:
				print("your account_type is correct")
		else:
			print("your account_type is in correct")
	else:
		pass


fun3()

balance=20000
def fun4():
	if transaction==1:
		a=int(input("enter how much money you want to withdrawl="))
		check=balance-a
		print("collect your money", check)
	elif transaction==2:
		a=int(input("enter hoew much money you want to deposit="))
		check=balance+a
		print("your money is deposited", check)
	elif transaction==3:
		pin2=int(input("enter the password"))
		print("confirm your pin")
		print("your pin is generated")
	else:
		print("quit")

transaction=int(input("enter the 1.withdraw ,2.deposit,3.pin change="))

fun4()