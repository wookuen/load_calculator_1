monthly_payment = 0
periods = 0
loan_principal = 0
number_of_months = 0
last_payment = 0
result = 0
import math

def one():
    global loan_principal
    print("Enter the loan principal:")
    loan_principal = input()
    two()


def two():
    global user_input2
    print("What do you want to calculate?")
    three()
    user_input2 = input()
    if user_input2 == "p":
        five()
    elif user_input2 == "m":
        four()


def three():
    print('''type "m" for number of monthly payments,
type "p" for the monthly payment''')


def four():
    global number_of_months
    global loan_principal
    global monthly_payment
    print("Enter the monthly payment:")
    monthly_payment = input()
    number_of_months = float(loan_principal) / float(monthly_payment)
    if number_of_months <= 1:
        print("It will take", number_of_months, "month to repay the loan")
    else:
        print("It will take", number_of_months, "months to repay the loan")


def five():
    global number_of_months
    global loan_principal
    global monthly_payment
    global result
    print("Enter the number of months:")
    number_of_months = input()
    monthly_payment = float(loan_principal) / float(number_of_months)
    if monthly_payment.is_integer():
        print("Your monthly payment = ", monthly_payment)
    else:
        result = math.ceil(monthly_payment)
        last_payment = float(loan_principal) - ((float(number_of_months) - 1) * float(result))
        print("Your monthly payment = ", result, "and", "the last payment = ", last_payment)


one()
