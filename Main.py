'''
Created on May 6, 2015

This is a program is a simple Automated Teller Machine program. It is designed
to demonstrate some very simple object oriented programming (OOP) in Python.

Bank.py is the module that is the bank part of the ATM. It can open accounts,
close accounts, and switch between accounts. 

Account.py is the module that handles individual accounts in a bank. 

TODO: Add options to allow a user to switch between banks. 

@author: Joshua jjc16_1@yahoo.com
'''
#import sys

bank=[];

def main_loop(account):
    
    ac=account; 
    
    while True:
        ch=raw_input('\nEnter action -- "a" to add account, "c" to check balance, ' +
                     '"cl" to close the account\n' +
              '"f" to add funds, "l" to list all accounts, "n" to return current account name\n' +
              ' "s" to switch accounts' +
              ' "w" to withdraw funds,' +
              'and "x" to exit:  ');
    
        if ch == 'a':
            ac=bank.add_account();
        elif ch == 'c':  
            ac.check_balance();
        elif ch == 'cl':
            ac=bank.close_account(ac)
        elif ch == 'f':
            am = raw_input('Enter amount to add: ')
            ac.change_balance(am);
        elif ch == 'l':
            bank.list_all_accounts();
        elif ch == 'n':
            ac.print_current_accout();
        elif ch == 's':
            ac=bank.change_account();
        elif ch == 'w':
            am = raw_input('Enter amount to withdraw: ')
            ac.change_balance(-float(am));
        elif ch == 'x':
            return False
            #break
        else: print('Input not recognized!')
       
    
if __name__ == '__main__':
    pass

from Bank import *

bank=Bank();

ac=bank.add_account();
main_loop(ac)
