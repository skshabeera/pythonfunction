def function1(language):
    if language=="hindi" or language=="english" or language=="karnataka":
        print("acseapted your",language)
        def function2(pin_code):
            if pin_code==1347:
                print("acseapt your pincode")
                def function3(type_acount):    
                    if type_acount=="curunt" or type_acount=="joint":
                        print("acsept your ",type_acount)
                        def function4(amount):
                            total_money=6000            
                            if amount>total_money or amount<=total_money:
                                print("we can withdraw the ",amount)
                                def function5(transaction):
                                    if transaction<amount or transaction>amount:
                                        print("we can", transaction)
                                        print(amount-transaction)
                                    else:
                                        print("you cant transaction")
                                    
                                function5(4000)
                            else:
                                print("we can not withdraw the account")
                        function4(5000)
                    else:
                        print("not acseapted your","type_acount")
                function3("curunt")
            else:
                print("your pin_code is not acsept")
        function2(1347)
    else:
        print("not acsepted your",language)
function1("english")