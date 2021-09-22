from Account import BankAccount
# Create 2 accounts
vacationsBankAccount = BankAccount( "SummerVacations", 0.03, 500 )
vacationsBankAccount.display_user_balance()

newCarBankAccount = BankAccount( "BuyNewCar", 0.05, 1500 )
newCarBankAccount.display_user_balance()


#To the first account, make 3 deposits and 1 withdrawal, 
# then yield interest and display the account's info all 
# in one line of code (i.e. chaining)
vacationsBankAccount.make_deposit(500).make_deposit(500).make_deposit(750).withdraw(250).yield_interest( 0.03 ).display_user_balance()

#To the second account, make 2 deposits and 4 withdrawals, 
# then yield interest and display the account's info all in
#  one line of code (i.e. chaining)
newCarBankAccount.make_deposit(1000).make_deposit(1000).withdraw(250).withdraw(250).withdraw(250).withdraw(250).yield_interest( 0.05 ).display_user_balance()


#NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
BankAccount.printAllAccountsInfo()