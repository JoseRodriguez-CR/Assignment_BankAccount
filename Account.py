class BankAccount:
    allBankAccounts = []

# don't forget to add some default values for these parameters!
    def __init__(self, nameAccount, int_rate, balance): 
        self.nameAccount = nameAccount
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.allBankAccounts.append( self )

    def make_deposit( self, amount ):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print( "Insufficient funds: Charging a $5 fee" )
            self.balance -= 5
        return self

    def display_user_balance( self ):
        print(f"Balance in your {self.nameAccount} Bank Account is: ${self.balance}")
        return self

    def yield_interest( self, int_rate ):
        if(self.balance > 0):
            self.balance += self.balance * int_rate
            print(f"Your Balance Account has been increased by {int_rate},\nnow your Balance Accout has: ${self.balance}")
        return self   


    @classmethod
    def printAllAccountsInfo( cls ):
        for account in cls.allBankAccounts:
            account.display_user_balance()

            # print( f"Account number: {self.accountNum}." )


