import unittest
from src.AccountServices import AccountServices
  
class MyTestCases(unittest.TestCase):
    def setUp(self):
        self.initial_amount = 1000
        self.testing_bank_account = AccountServices(1000)
        
    def test_case1_transaction_deposit(self):
        print("\nTest Case 1: Deposit testing -----------------------------------------")
        print("Inital balance = ", self.initial_amount, "\n")
        transaction_amount = 800
        ret_value = self.testing_bank_account.transaction_deposit(transaction_amount)
        print(f"Deposit = {transaction_amount}")
        print(ret_value["Message"])
        
        transaction_amount = 300
        ret_value= self.testing_bank_account.transaction_deposit(transaction_amount)
        print(f"Deposit = {transaction_amount}")
        print(ret_value["Message"])
              
        expected_balance = 2100
        current_balance = self.testing_bank_account.check_account_balance()["Value"]
        print("\nExpected balance = ", expected_balance)
        print("Current balance  = ", current_balance)
        
        try:
            self.assertEqual(current_balance, expected_balance)  
        except AssertionError as e:
            print("Failed....!")
            raise
        else:
            print("Passed....")   
        
      
        
    def test_case2_transaction_withdraw(self):
        print("\n\nTest Case 2: Withdraw testing ----------------------------------------")

        print("Inital balance = ", self.initial_amount, "\n")
        transaction_amount = 100
        ret_value = self.testing_bank_account.transaction_withdraw(transaction_amount)
        print(f"Withdraw = {transaction_amount}")
        print(ret_value["Message"])

        transaction_amount = 50
        ret_value = self.testing_bank_account.transaction_withdraw(transaction_amount)
        print(f"Withdraw = {transaction_amount}")
        print(ret_value["Message"])

        expected_balance = 850
        current_balance = self.testing_bank_account.check_account_balance()["Value"]
        print("\nExpected balance = ", expected_balance)
        print("Current balance  = ", current_balance)
        
        try:
            self.assertEqual(current_balance, expected_balance)  
        except AssertionError as e:
            print("Failed....!")
            raise
        else:
            print("Passed....")      
        
        
    def test_case3_transaction_mixed(self):
        print("\n\nTest Case 3: Mixed testing -------------------------------------------")
        
        print("Inital balance = ", self.initial_amount, "\n")
        transaction_amount = 2000
        ret_value = self.testing_bank_account.transaction_deposit(transaction_amount)
        print(f"Deposit = {transaction_amount}")
        print(ret_value["Message"])
        
        transaction_amount = 200
        ret_value = self.testing_bank_account.transaction_withdraw(transaction_amount)
        print(f"Withdraw = {transaction_amount}")
        print(ret_value["Message"])    
        
        expected_balance = 2800
        current_balance = self.testing_bank_account.check_account_balance()["Value"]
        print("\nExpected balance = ", expected_balance)
        print("Current balance  = ", current_balance)
        
        try:
            self.assertEqual(current_balance, expected_balance)  
        except AssertionError as e:
            print("Failed....!")
            raise
        else:
            print("Passed....")             
        
        
       
    def test_case4_transaction_withdraw_with_insufficient_balance(self):
        print("\n\nTest Case 4: Insufficient account balance ----------------------------")
        print("Inital balance = ", self.initial_amount)
        transaction_amount = 5000
        ret_value = self.testing_bank_account.transaction_withdraw(transaction_amount)  
        print(f"Withdraw = {transaction_amount}")
        print(ret_value["Message"])  
            
        
        expected_balance = self.initial_amount
        current_balance = self.testing_bank_account.check_account_balance()["Value"]
        print("Expected balance = ", expected_balance)
        print("Current balance  = ", current_balance)
        
        try:
            self.assertEqual(current_balance, expected_balance)  
        except AssertionError as e:
            print("Failed....!")
            raise
        else:
            print("Passed....")   
        
        
    def test_case5_transaction_deposit_with_negative_amount(self):
        print("\n\nTest Case 5: Deposit testing with negative amount --------------------")
        print("Inital balance = ", self.initial_amount)
        transaction_amount = -100
        ret_value = self.testing_bank_account.transaction_deposit(transaction_amount)  
        print(f"Deposit = {transaction_amount}")
        print(ret_value["Message"])   
            
        
        expected_balance = self.initial_amount
        current_balance = self.testing_bank_account.check_account_balance()["Value"]
        print("Expected balance = ", expected_balance)
        print("Current balance.  = ", current_balance)
        
        try:
            self.assertEqual(current_balance, expected_balance)  
        except AssertionError as e:
            print("Failed....!")
            raise
        else:
            print("Passed....")   

if __name__ == '__main__':
    unittest.main()