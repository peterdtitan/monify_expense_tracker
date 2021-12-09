import datetime
from pandas import DataFrame as df
import pandas as pd
from csv import writer
import glob
import os.path
import os


def checkIf(month):
    try :
        df = pd.read_csv(f'{month}.csv')
        return df.empty
    except :
        return True
    
    
def check_month(month):
    switch = {
        1 : 'January',
        2 : 'February',
        3 :'March',
        4 :'April',
        5 :'May',
        6 :'June',
        7 :'July',
        8 :'August',
        9 :'September',
        10 :'October',
        11 :'November',
        12 :'December',
    }
    return switch.get(month,1)


def tracker(date = 0 ,income =" ", foodDrinks =" ", Transport =" ", lifeEntertainment =" ", miscellaneous =" ", housing= " ", total_expenses =" "):
    data = {
    'Date':date,
    'Income':income,
    'Food & Drinks':foodDrinks,
    'Transport': Transport,
    'Life & Entertainment': lifeEntertainment,
    'Miscellaneous': miscellaneous,
    'Housing': housing, 
    'Total Expenses': total_expenses
    }
    
    database = df.from_dict(data,orient='index')
    database = database.transpose()
    decide = 'a'
    check = False
    datea = str(date)
    year,month,day = map(int,datea.split('-'))
    curr_month = check_month(month)
    if checkIf(curr_month):
        decide = 'w'
        check = True
    database.to_csv(f'{curr_month}.csv',mode = decide,header=check,index=False)

class Monify:
  def add_income():
    date = str(input('Enter Date (YYYY-MM-DD)\n: --> '))
    year,month,day=map(int,date.split('-'))
    date = datetime.date(year,month,day)
    income = int(input("Enter your income for the month \n: --> "))
    tracker(date,income,0,0,0,0,0,0)
    

  def add_expenditure():
    print("\t\t\t\nEXPENSE CATEGORIES: \n1. Food & Drinks\n2. Transport\n 3. Life & Entertainment\n4. Miscellaneous\n5. Housing\n")
    
    while True:
        try:
            response = int(input("\nPlease select a category number: "))
            print("\n")
        except ValueError:
            print("Not a valid option!\n")
            continue
        else:
            break
        
    if response == 1:
        while True:
            try:
                date = str(input('Enter expenditure date (YYYY-MM-DD) (optional) \n: --> '))
                year,month,day=map(int,date.split('-'))
                date = datetime.date(year,month,day)
                
                fd = str(input("\nHow much did you spend on \"Food and Drinks?\" --> "))
                
            except ValueError:
                print("Please enter valid input!\n")
                continue
              
            else:
                tracker(date,0,fd,0,0,0,0,0)
                print("\nExpense recorded successfully!\n")
                break
            
            
    elif response == 2:
        while True:
            try:
                date = str(input('Enter expenditure date (YYYY-MM-DD) (optional) \n: --> '))
                year,month,day=map(int,date.split('-'))
                date = datetime.date(year,month,day)
                
                ht = str(input("\nHow much did you spend on \"Transport?\" --> "))

            except ValueError:
                print("Please enter valid input!\n")
                continue
              
            else:
                tracker(date,0,0,ht,0,0,0,0)
                print("\nExpense recorded successfully!\n")
                break


    elif response == 3:
        while True:
            try:
                date = str(input('Enter expenditure date (YYYY-MM-DD) (optional) \n: --> '))
                year,month,day=map(int,date.split('-'))
                date = datetime.date(year,month,day)
                
                le = str(input("\nHow much did you spend on \"Life & Entertainment?\" --> "))

            except ValueError:
                print("Please enter valid input!\n")
                continue
              
            else:
                tracker(date,0,0,0,le,0,0,0)
                print("\nExpense recorded successfully!\n")
                break


    elif response == 4:
        while True:
            try:
                date = str(input('Enter expenditure date (YYYY-MM-DD) (optional) \n: --> '))
                year,month,day=map(int,date.split('-'))
                date = datetime.date(year,month,day)
                
                misc = str(input("\nHow much did you spend on \"Miscellaneous?\" --> "))
                
            except ValueError:
                print("Please enter valid input!\n")
                continue
            else:
                tracker(date,0,0,0,0,misc,0,0)
                print("\nExpense recorded successfully!\n")
                break


    elif response == 5:
        while True:
            try:
                date = str(input('Enter expenditure date (YYYY-MM-DD) (optional) \n: --> '))
                year,month,day=map(int,date.split('-'))
                date = datetime.date(year,month,day)
                
                house = str(input("\nHow much did you spend on \"Housing?\" --> "))
        
            except ValueError:
                print("Please enter valid input!\n")
                continue
              
            else:
                tracker(date,0,0,0,0,0,house,0)
                print("\nExpense recorded successfully!\n")
                break
    
            
  def add_budget():
    
    
    print("\nYou are about to enter your budget for the CURRENT MONTH")
    
    while True:
      try:
        user_option = str(input("\n Would you like to proceed (yes/no): "))
        user_option.upper()
      except ValueError:
        print("Enter a valid response")
        continue
      else:
        break
      
    


  def emergency_fund():
    emergency_fund_amount = int(input("How much do you want to add to your Emergency fund account: "))
    
  
  
  def view_shopping_list():
    if os.path.exists('./Shopping List.csv'):
      list = pd.read_csv('Shopping List.csv', header=0)
      print("\nThis is your most recent shopping list: --> \n")
      print(list)
    else:
      print("\nYou have not added any shopping list yet!")
    

  def add_shopping_list():
    shopping_list = {}
    ans = True
    while ans:
      print("\nEnter the items in your shopping list and their prices -->")
      item = str(input("\nEnter the item name: --> "))
      value = int(input("\nEnter the price: --> "))
      shopping_list[item] = value
      
      print("Recorded!\n")
      resp = str(input("Add another item? (yes/no) --> "))
      resp = resp.upper()
      if resp == "YES":
        continue
      else:
        ans = False
        df = pd.DataFrame.from_dict(shopping_list, orient = 'index')
        df = df.transpose()
        
        if os.path.exists('./Shopping List.csv'):
          os.remove('Shopping List.csv')
          
        df.to_csv('Shopping List.csv')
        

        

 

def debt_data(date = 0, lender = " ", amount = " ", due = " ",):
  data = {
  'Date':date,
  'Lender':lender,
  'Amount Borrowed':amount,
  'Repayment Date': due
  }

  if os.path.exists('./Debt Records.csv'):
    list = [date,lender,amount,due]
    with open('Debt Records.csv', 'a') as f_object:
      writer_object = writer(f_object)
      writer_object.writerow(list)
      f_object.close() 
  else:
    df = pd.DataFrame.from_dict(data, orient = 'index')
    df = df.transpose()
    df.to_csv('Debt Records.csv', index = False)


class Debt_account(Monify):
  def add_debt_record():
    amount = input("\nHow much did you borrow? --> ")
    date = input("\nWhen did borrow this money? -->  ")
    lender = input("\nEnter the name of the lender who you owe: --> ")
    due = input("\nWhat date do you need to pay back?: --> ")
    
    debt_data(date, lender, amount, due)

  def pay_debt():
    data = pd.read_csv('Debt Records.csv', header=0)
    print(data)
    
    response = int(input("\nWhich loan have you payed back? (Enter row number) --> "))
    data = data.drop(index = response)
  
    if os.path.exists('./Debt Records.csv'):
      os.remove('Debt Records.csv')
      data.to_csv('Debt Records.csv')
    


def menu():
  print("\n\t\t########################### WELCOME TO MONIFY ###########################")
  print("\n\t\tWhat do you want to do?\n\t\t1. Add Income\n\t\t2. Add Expenditure\n\t\t3. Debt Accounting\n\t\t4. Shopping List\n\t\t5. Emergency Funds\n")
  
  while True:
    try:
      ans = int(input("Please enter an option: --> "))
    except ValueError:
      print("\nPlease enter an integer!")
      print("\n\t\t########################### WELCOME TO MONIFY ###########################")
      print("\n\t\tWhat do you want to do?\n\t\t1. Add Income\n\t\t2. Add Expenditure\n\t\t3. Debt Accounting\n\t\t4. Shopping List\n\t\t5. Emergency Funds\n6. Statistics")
      continue
    else:
      break
    
  if ans == 1:
    Monify.add_income()
    
  elif ans == 2:
    Monify.add_expenditure()
    
  elif ans == 3:
    while True:
      try:
        print("\n\t\t1. Add Debt Record\n\t\t2. Pay Debt\n")
        debt = int(input("What do you want to do? --> "))
      except ValueError:
        print("\nPlease enter an integer!\n")
        continue
      else:
        break
    if debt == 1:
      Debt_account.add_debt_record()
    elif debt == 2:
      Debt_account.pay_debt()
      
Monify.add_shopping_list()
Monify.view_shopping_list()
