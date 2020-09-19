"""
How many months till you save the down payment needed for your dream home?

    1. savings() calculates the savings after one month given the current_savings, rate, monthly income and portions of income portion_saved
    2. months_till_downpayment() calculates number of months till savings is above the portion_down_payment
    3. main() user enters in annual_salary, portion_saved and total_cost

"""

def savings(sav,r,i,ps):
    sav = sav + sav*r/12 + i*ps
    return sav

def months_till_downpayment(cs,r,i,ps,dp):
    months = 0
    while cs<dp:
        cs = savings(cs,r,i,ps)
        months += 1
    return months

def main():
    annual_salary = float(input('Enter your annual salary:'))
    portion_saved = float(input('Enter the percent of your salary to save, as a decimal:'))
    total_cost = float(input('Enter the cost of your dream home:'))

    monthly_salary = annual_salary/12
    portion_down_payment = 0.25*total_cost
    current_savings = float(0)
    rate = 0.04 #rate of retrun
    months = months_till_downpayment(current_savings,rate,monthly_salary,portion_saved,portion_down_payment)
    print('Number of months: ' + str(months))

if __name__ == "__main__":
    main()
