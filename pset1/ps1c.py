"""
    How much do I need to save to afford down payment in x years?



"""

def savings(sav,r,i,ps):
    sav = sav + sav*r/12 + i*ps
    return sav

def months_till_downpayment(cs,r,i,ps,dp,sa):
    months = 0
    income = i
    while cs<dp:
        cs = savings(cs,r,income,ps)
        months += 1
        if months % 6 == 0 and months != 0:
            income = income + income*sa
    return months

def downpayment_in_months(cs,r,i,ps,months,sa):
    income = i
    for m in range(months):
        if m % 6 == 0 and m != 0:
            income = income + income*sa
        cs = savings(cs,r,income,ps)
    return cs


def bisection(cs,r,i,months,sa,pdp):
    high = float(1)
    low = float(0)
    epsilon = 100
    num_guesses = 0
    guess = (high + low)/2.0
    downpayment = 0
    print('pdp: ' + str(pdp))
    while abs(downpayment-pdp) >= epsilon or downpayment < pdp:
        downpayment = downpayment_in_months(cs,r,i,guess,months,sa)
        if downpayment < pdp:
            low = guess
        else:
            high = guess
        guess = (high + low)/2
        num_guesses += 1
    best_savings_rate = guess + .0001 # round up
    print('Best savings rate: ' + str(best_savings_rate)[0:6] + '\nSteps in bisection search: ' + str(num_guesses))

def main():
    annual_salary = float(input('Enter the starting salary: '))

    months = 36
    total_cost = float(1000000)
    semi_annual_raise = .07
    monthly_salary = annual_salary/12
    portion_down_payment = 0.25*total_cost
    current_savings = float(0)
    rate = 0.04 #rate of retrun
    max_months_till_down_payment = months_till_downpayment(current_savings,rate,monthly_salary,1,portion_down_payment,semi_annual_raise)
    if max_months_till_down_payment > 36:
        print('It is not possible to pay the down payment in three years.')
    else:
        bisection(current_savings, rate, monthly_salary, months, semi_annual_raise, portion_down_payment)

if __name__ == "__main__":
    main()
