# a person wants to buy a bike "x" , he does not have the amount right now . he can pay the total price for the bike in monthly installment
# equated monthly installment[EMI]
# EMI =(principal * monthly interest rate * (1+r)^no.of months(n)) / [(1+r)^n-1]

# EMI = p*r*(1+r)^n /
#        (1+r)^n-1

# p = principal amount
# r = interest rate 
# n = number of months
# calculate -> 
# monthly payment he needs to pay
# final total amount


def calculate_emi(principal, annual_interest_rate,loan_period):
    #convert annual interest rate to monthly and decimal
    monthly_interest_rate = (annual_interest_rate/100)/12
    #convert loan period from years to months
    loan_period_months = loan_period *12
    # calculate EMI
    emi = (principal * monthly_interest_rate*(1+monthly_interest_rate)**loan_period_months)
    return emi
principal = float(input("Enter the loan amount: "))
annual_interest_rate = float(input("Enter the annual interest rate : "))
loan_period = int(input("Enter the loan period in years: "))

emi = calculate_emi(principal,annual_interest_rate, loan_period)
print(f'the emi for loan is :{emi}')
