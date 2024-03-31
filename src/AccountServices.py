class AccountServices:
    
    def __init__(self, init_balance=0):
        self.account_balance = init_balance
       

    def transaction_deposit(self,deposit_amount):
        return_value = {}
        try:
            # if deposit_amount <= 0:
            #     return_value["Status"] = "ERROR"
            #     return_value["Message"] = f"The transaction could not be completed: The amount must be positive!"
            #     return return_value

            self.account_balance += deposit_amount

            return_value["Status"] = "OK"
            return_value["Message"] = f"Your doposit transaction has been completed successfully.\nYour current balance = {self.account_balance}"
            return return_value
        
        except Exception as e:
            return_value["Status"] = "ERROR"
            return_value["Message"] = f"\nThe transaction could not be completed: {e}\n"            
            return return_value      

    def transaction_withdraw(self,withdraw_amount):
        return_value = {}
        return return_value        
    
    def check_account_balance(self):
        return_value = {}
        return return_value  