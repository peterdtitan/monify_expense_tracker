import datetime
from pandas import DataFrame as df
import pandas as pd
from matplotlib import pyplot,style
 

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


def tracker(date = datetime.date.today() ,income =" ", foodDrinks =" ", housingTransport =" ", lifeEntertainment =" ", miscellaneous =" ", total_expenses =" "):
    data = {
    'Date':date,
    'Income':income,
    'Food & Drinks':foodDrinks,
    'Housing & Transport': housingTransport,
    'Life & Entertainment': lifeEntertainment,
    'Miscellaneous': miscellaneous,
    'Total Expense': total_expenses
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


def add_income():
    date = str(input('Enter Date (YYYY,MM,DD) (optional) \n: --> '))
    year,month,day=map(int,date.split(','))
    date = datetime.date(year,month,day)
    income = int(input("Enter your income for today if any \n: --> "))
    
    tracker(date,income,0,0,0,0,0)

def add_expense():
    print("\t\t\t\nEXPENSE CATEGORIES: \n1. Food & Drinks\n2. Housing & Transport\n 3. Life & Entertainment\n4. Miscellaneous\n")
    
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
                date = str(input('Enter expenditure date (YYYY,MM,DD) (optional) \n: --> '))
                year,month,day=map(int,date.split(','))
                date = datetime.date(year,month,day)
                
                fd = str(input("\nHow much did you spend on \"Food and Drinks?\""))
                print("\n")
            except ValueError:
                print("Please enter valid input!\n")
                continue
            else:
                tracker(date,0,fd,0,0,0,0)
                print("\nExpense recorded successfully!\n")
                break
            
    elif response == 2:
        while True:
            try:
                date = str(input('Enter expenditure date (YYYY,MM,DD) (optional) \n: --> '))
                year,month,day=map(int,date.split(','))
                date = datetime.date(year,month,day)
                
                ht = str(input("\nHow much did you spend on \"Housing & Transport?\""))
                print("\n")
            except ValueError:
                print("Please enter valid input!\n")
                continue
            else:
                tracker(date,0,0,ht,0,0,0)
                print("\nExpense recorded successfully!\n")
                break

    elif response == 3:
        while True:
            try:
                date = str(input('Enter expenditure date (YYYY,MM,DD) (optional) \n: --> '))
                year,month,day=map(int,date.split(','))
                date = datetime.date(year,month,day)
                
                le = str(input("\nHow much did you spend on \"Life & Entertainment?\""))
                print("\n")
            except ValueError:
                print("Please enter valid input!\n")
                continue
            else:
                tracker(date,0,0,0,le,0,0)
                print("\nExpense recorded successfully!\n")
                break

    elif response == 4:
        while True:
            try:
                date = str(input('Enter expenditure date (YYYY,MM,DD) (optional) \n: --> '))
                year,month,day=map(int,date.split(','))
                date = datetime.date(year,month,day)
                
                misc = str(input("\nHow much did you spend on \"Miscellaneous?\""))
                print("\n")
            except ValueError:
                print("Please enter valid input!\n")
                continue
            else:
                tracker(date,0,0,0,0,misc,0)
                print("\nExpense recorded successfully!\n")
                break
            
add_income()
add_expense()
add_expense()
add_income()