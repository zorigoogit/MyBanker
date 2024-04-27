from AccountServices import AccountServices

def main():
    my_account = AccountServices()
    #my_account = AccountServices(100)
    
    print("*********************************************************************************")
    print("*                                                                               *")
    print("*                    Welcome to the MyBanker application                        *")
    print("*                                                                               *")   
    print("*********************************************************************************")    
    
    print("\nYour initial account balance = ", my_account.check_account_balance()["Value"],"\n")
    
    while True:
        try:
            print("Select your account service :")
            print("1. Deposit Money")
            print("2. Withdraw Money")
            print("3. Check Balance")
            print("4. Exit")


            choice = input("Enter the operation number: ")

            if choice == "1":
                transaction_amount = float(input("Enter deposit transaction amount: "))
                ret_value = my_account.transaction_deposit(transaction_amount)
                print(ret_value["Message"])
            elif choice == "2":
                transaction_amount = float(input("Enter withdraw transaction amount: "))
                ret_value = my_account.transaction_withdraw(transaction_amount)
                print(ret_value["Message"])
            elif choice == "3":
                ret_value = my_account.check_account_balance()    
                print(ret_value["Message"])
            elif choice == "4":
                print("\nThank you for using our service. Have a nice day!")
                break
            else:
                print("\nWrong request. Please try again.")
            
            
        except Exception as e:
            print(f"\nThe transaction could not be completed: {e}\n")
        finally:
            print("\n--------------------------------------------------------------------------------\n")    


if __name__ == '__main__':
    main()




