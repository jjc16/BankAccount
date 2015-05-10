'''
Created on May 5, 2015

@author: Joshua
'''
#from object import *
import ClosedAccount as ClAc

class Bank:

    def __init__(self):
        '''
        Constructor
        '''
        bank_name=raw_input('Enter the name of the bank you would like to access: ')
        self.bank_name=bank_name;
        
        self.accounts_list={};
        self.bank_name=[];
        print('Confirmed')
        
    def add_account(self):
        nm=raw_input('Enter account holder\'s name:')
        bl=raw_input('Enter starting balance: ');
        
        from Account import * 
        ac=Account(nm,bl);
        
        #associate name to object
        self.accounts_list[nm]=ac;
        return ac;
        
    def close_account(self,account):
        
        
        clac=ClAc.ClosedAccount(account)
        return clac; 
        
    def change_account(self):
        
        print('Account list: ');
        print(self.accounts_list.keys());
        nm=raw_input('Type the name of the account you wish to switch to: ')
        
        ac = self.accounts_list[nm];
        return ac;
    
    def list_all_accounts(self):
    
        print(self.accounts_list.keys())
            
    