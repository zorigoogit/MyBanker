class AccountServices:
    
    def __init__(self, init_balance=0):
        self.account_balance = init_balance
       

    def transaction_deposit(self,deposit_amount):
        return_value = {}
        return return_value      

    def transaction_withdraw(self,withdraw_amount):
        return_value = {}
        return return_value        
    
    def check_account_balance(self):
        return_value = {}
        return_value["Status"] = "OK"
        return_value["Message"] = f"Your current balance = {self.account_balance}"
        return_value["Value"] = self.account_balance
        return return_value