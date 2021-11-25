import datetime
from pandas import DataFrame as df
import pandas as pd
from matplotlib import pyplot,style


def tracker(date = datetime.date.today() ,income =" ", foodDrinks =" ", Transport =" ", lifeEntertainment =" ", miscellaneous =" ", housing= " ", total_expenses =" "):
    data = {
    'Date':date,
    'Income':income,
    'Food & Drinks':foodDrinks,
    'Transport': Transport,
    'Life & Entertainment': lifeEntertainment,
    'Miscellaneous': miscellaneous,
    'Housing': housing, 
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

class Monify:
  def __init__ (self, monthly = 0.0, food_drinks = 0.0 , transport = 0.0, housing = 0.0, life_entertainment = 0.0, miscellaneous = 0.0, emergency_fund = 0.0, available_income =" " ):
    global 
    self.available_income = available_income
    self.budget_monthly =   monthly
    self.budget_food_drinks = food_drinks
    self.budget_transport = transport
    self.budget_housing = housing
    self.budget_life_entertainment = life_entertainment
    self.budget_miscellaneous = miscellaneous
    self.budget_emergency_fund = emergency_fund


  def add_income(self):
    date = str(input('Enter Date (YYYY-MM-DD) (optional) \n: --> '))
    year,month,day=map(int,date.split('-'))
    date = datetime.date(year,month,day)
    income = int(input("Enter your income for the month \n: --> "))
    tracker(date,income,0,0,0,0,0,0)
    

  def add_expenditure(self):
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
                
                fd = str(input("\nHow much did you spend on \"Food and Drinks?\""))
                print("\n")
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
                
                ht = str(input("\nHow much did you spend on \"Transport?\""))
                print("\n")
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
                
                le = str(input("\nHow much did you spend on \"Life & Entertainment?\""))
                print("\n")
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
                
                misc = str(input("\nHow much did you spend on \"Miscellaneous?\""))
                print("\n")
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
                
                misc = str(input("\nHow much did you spend on \"Housing?\""))
                print("\n")
            except ValueError:
                print("Please enter valid input!\n")
                continue
            else:
                tracker(date,0,0,0,0,0,house,0)
                print("\nExpense recorded successfully!\n")
                break
            
  def add_budget(self):
    print(f"You have {self.available_income} and cannot budget than it")
    while True:
      try:
        user_option = str(input("\n Would you like to proceed (yes/no): "))
        user_option.upper()
      except ValueError:
        print("Enter a valid response")
        continue
      else:
        break
    if user_option == "YES":
      monthly_budget = float(input("Enter your monthly_budget\n: --> "))
      self.budget_monthly += monthly_budget

      food_drinks_budget = float(input("Enter your budget for food_drink\n: --> "))
      self.budget_food_drinks += food_drinks_budget

      transport_budget = float(input("Enter your budget for transport\n: --> "))
      self.budget_transport += transport_budget

      life_entertainment_budget = float(input("Enter your budget for life_entertainment\n: --> "))
      self.budget_life_entertainment += life_entertainment_budget

      misc_budget = float(input("Enter your budget for miscellaneous\n: --> "))
      self.budget_miscellaneous += misc_budget

      house_budget = float(input("Enter your budget for housing\n: --> "))
      self.budget_housing += house_budget

    else: 
      self.menu()

  def emergency_fund(self):
    emergency_fund_amount = float(input("How much do you want to save in your Emergency fund account\n:--> "))
    while True:
      try: 
        if self.available_income not None and emergency_fund_amount < self.available_income:
          self.budget_emergency_fund += emergency_fund_amount
          print(f"You saved {self.budget_emergency_fund} in your Emergency_fund account")
        else:
          print("Insufficient balance")
      except ValueError:
        print("Please enter valid input!\n")
        continue
      else:
        break 

  def shopping_list(self):
    shopping_details = input("Enter the details for your shopping list, separating each entry by a comma.\n:--> ")
    list_format = list(map(str, shopping_details.split(",")))
    for item in list_format:
      print("Here is your shopping list details:\n{item}")



class Debt_account(Monify):
  def __init__(self,available_income, debt_dictionary = {},):
    super().__init__(available_income)
    self.debt_dictionary = debt_dictionary

  def add_debt_record(self):
    borrowee = input("Enter the Borrowee who you owe\n: --> ")
    loan_amount = float(input("How much did you borrow from this user\n: --> "))
    self.debt_dictionary[borrowee] = loan_amount

  def pay_debt(self):
    print(f"Your debt account: {self.debt_dictionary}")
    user_choice_pay = input("What debt would you like to pay\n : --> ")
    if user_choice_pay in self.debt_dictionary:
      self.available_income -= self.debt_dictionary["user_choice_pay"]
      del self.debt_dictionary["user_choice_pay"]











        









c1 = Monify()
c1.add_income()


