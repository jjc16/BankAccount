'''
Created on May 10, 2015

@author: Joshua
'''
import Account as Acc

class ClosedAccount(Acc.Account):
    '''
    classdocs
    '''

    def __init__(self,account):
        '''
        Constructor
        '''
        self._balance=0;
        self.name=account.name;
        
    def assign_account_number(self):
        print('Sorry: Account Closed!');
        
    def change_balance(self,amount):
        print('Sorry: Account Closed!');
        
    