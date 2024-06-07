'''
You'll need three pieces of information:

the loan amount
the Annual Percentage Rate (APR)
the loan duration
From the above, you'll need to calculate the following two things:

monthly interest rate (APR / 12)
loan duration in months
'''
def prompt(message):
    print(f'==> {message}')

def invalid_number(num):
    try:
        float(num)
    except ValueError:
        return True
    return False

def validate_numeric_entry(num, message):
    while invalid_number(num) or num < 0:
        prompt(message)
        num = input()

prompt('Welcome to Loan Calculator')

prompt('Enter the loan amount.')
loan_amount = round(int(input()), 2)


prompt('Enter the Annual Percentage Rate (APR)')
apr = float(input()) 
percentage_apr = apr / 100

monthly_interest_rate = round((percentage_apr / 12), 4)


prompt('Enter the Loan Term in years and months')
prompt('Years')
years = int(input())
prompt('Months')
months = int(input())


loan_duration_in_months = (years * 12) + months

monthly_payment = loan_amount * (monthly_interest_rate / 
                                 (1 - (1 + monthly_interest_rate) ** 
                                  (-loan_duration_in_months)))



print(f'loan_amount = {loan_amount}')
print(f'apr = {apr}')
print(f'percentage_apr = {percentage_apr}')
print(f'monthly_interest_rate = {monthly_interest_rate}')
print(f'years = {years}')
print(f'months = {months}')
print(f'loan_duration = {loan_duration_in_months}')
print(f'monthly_payment = {round(monthly_payment, 2)}')