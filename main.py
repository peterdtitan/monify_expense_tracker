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


def tracker(date = datetime.date.today() ,income =" ", foodDrinks =" ", housingTransport =" ", lifeEntertainment =" ", total_expenses =" "):
    data = {
    'Date':date,
    'Income':income,
    'Food & Drinks':foodDrinks,
    'Housing & Transport': housingTransport,
    'Life & Entertainment': lifeEntertainment,
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
    
    tracker(date,income,0,0,0,0)

add_income()