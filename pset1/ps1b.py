"""
    How many months till you save for the down payment of your dream home witha semi-annual raises?



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

def main():
    annual_salary = float(input('Enter your annual salary:'))
    portion_saved = float(input('Enter the percent of your salary to save, as a decimal:'))
    total_cost = float(input('Enter the cost of your dream home:'))
    semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal:'))

    monthly_salary = annual_salary/12
    portion_down_payment = 0.25*total_cost
    current_savings = float(0)
    rate = 0.04 #rate of retrun
    months = months_till_downpayment(current_savings,rate,monthly_salary,portion_saved,portion_down_payment,semi_annual_raise)
    print('Number of months: ' + str(months))

if __name__ == "__main__":
    main()
