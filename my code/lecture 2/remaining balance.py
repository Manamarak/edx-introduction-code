balance = int (input("What is the outstanding balance? "))
annualInterestRate = int (input("What is the annual interest rate in as a fraction? "))
monthlyPaymentRate = int (input("What is the monthly repayment rate as a fraction? "))


def monthly_rate (annual_rate):
   month_rate = annual_rate/12.0
   return month_rate

def minimum_monthly_payment (p, b):
   return p*b
   
def monthly_unpaid_balance (p, m):
   return p-m
   
def updated_balance_each_month (u, i):
   return u+(u*i)

month = 1
rate = monthly_rate (annualInterestRate)

while month < 13:
   payment = minimum_monthly_payment (monthlyPaymentRate,balance)
   unpaid_balance = monthly_unpaid_balance (balance, payment)
   balance = updated_balance_each_month (unpaid_balance, rate)
   balance_round = balance
   round(balance_round,2)
   month +=1
print ("Remaining balance:", round(balance,2))
