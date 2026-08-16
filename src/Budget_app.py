class Category:
    ledger = []
    def deposit(self,amount,description):
        self.amount=amount
        self.description=description
        
        ledger.append({'amount': self.amount, 'description': self.description})

    def withdraw(self,amount,description):
        self.amount=amount
        self.description=description
        ledger.append(description,-amount)
        if self.amount>=0:
            return True
        else:
            return False
            

    def get_balance(self):
        return f'{ledger.amount}'
    def transfer(self,amount,description):
        pass

        
        


def create_spend_chart(categories):
    pass
