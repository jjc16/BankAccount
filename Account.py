'''
Created on May 5, 2015

@author: Joshua
'''
from numpy.matlib import rand
#from object import *


class Account:
    '''
    This class sets up a bank account object 
    '''
  

    def __init__(self, name, balance=0):
        '''
        Constructor
        '''
        self.name=name;
        self._balance=float(balance);
        
        self.assign_account_number()
        
        
    def assign_account_number(self):
        
            self.account_number=round(float(rand(1))*100000,0);
            print(str('Your account number is {}').format(self.account_number));
            
            
    def change_balance(self,amount):
        
        if self._balance + float(amount) < 0:
            print (str('Cannot withdraw  {} : Insufficient funds').format(-float(amount)));
        else:            
            self._balance += float(amount);
            print(str('Your new balance is {}').format(self._balance));
            
    def check_balance(self):
        
        print(str('Your account balance is: {}').format(self._balance));
        #return self._balance;
        
    def print_current_accout(self):
        print('Current Account: ' + self.name)
            