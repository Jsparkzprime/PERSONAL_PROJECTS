#input to find out what type of calculation needs to be done
while True:
    
    calculation_type = input("What calculation would you like us to run. Investment or Bond? ")
    calculation_type = calculation_type.lower()

    if calculation_type == 'investment':
        break
    elif calculation_type == 'bond':
        break
    else:
        print("Please choose 'investment' or 'bond'")


#function to run investment calculation
def investment_calc(investment_type):

        #code for simple interest
        if investment_type.lower() == 'simple':
            while True:
                #variable for annual rate as a percentage
                annual_rate = input("What is the annual rate on your interest as a percentage? ")
                #variable for initial amount deposited
                initial_deposit = input('How much did you initially deposit in the bank? ')
                #variable for the amount of years since interest was deposited in years
                time_in_years = input('How many years since your initial deposit? ')
                #changing all variables to integers
                try:            
                    annual_rate = float(annual_rate)
                    time_in_years = int(time_in_years)
                    initial_deposit = float(initial_deposit)
                except: 
                    print('Please make sure all values are in digits')
                else:
                    break

            #calculation to find out the new amount plus the simple interest
            new_amount   = initial_deposit + ((initial_deposit * annual_rate * time_in_years)/100)
            return (new_amount)
      
        #code for compound interest
        elif investment_type.lower() == 'compound':          
            while True:
                #variable for annual rate as a percentage
                annual_rate = input("What is the rate on your interest as a percentage? ")
                #variable for initial amount deposited
                initial_deposit = input('How much did you initially deposit in the bank? ')
                #variable for the amount of years since interest was deposited in years
                time_in_years = input('How many years since your initial deposit? ')
                #changing all variables to integers
                try:
                    annual_rate = float(annual_rate)
                    time_in_years = int(time_in_years)
                    initial_deposit = float(initial_deposit)
                except: 
                    print('Please make sure all values are in digits')
                else:
                    break

            #calculation to find out the new amount plus the compounded interest
            new_amount = initial_deposit * (( 1 +(annual_rate/100)) ** time_in_years)
            return (new_amount)  

#function to run bond calculation
def bond_calc():
    #variable for the initial value of the house
    while True:
        initial_value = input("What is the present value of your house? ")
        #variable for the annual interest rate on bond as a percentage
        annual_rate = input("What is the annual interest rate on your loan? ")
        #variable for how many months loan is payed over
        time_in_months = input("How many months would you like to repay the loan over? ")
        
        
        try:
            #changing all variables to integers
            initial_value = float(initial_value)
            annual_rate = float(annual_rate)
            #changing annual interest rate to monthly interest rate as a decimal
            monthly_rate = (annual_rate/100)/12
            #changing all variables to integers
            time_in_months = int(time_in_months)
        except: 
            print('Please make sure all values are in digits')
        else:
            break


    #calculation to calculate monthly repayment
    repayment = (monthly_rate * initial_value)/(1 - ((1 + monthly_rate)** (-time_in_months)) )
    return(repayment)

#code to print result of investment calculation
if calculation_type == 'investment':
    
    while True:

        investment_type = input("What kind of interest do you have on your investment ? ")
        investment_type = investment_type.lower()

        if investment_type == 'simple':
            break
        elif investment_type == 'compound':
            break
        else:
            print("Choose either 'simple' or 'compound' as your interest type")

    Amount = investment_calc(investment_type)
    Amount = float(Amount)
    print(f'Thanks for your time, your new investment in addition to your {investment_type} interest amounts to £{Amount:.2f} ')

#code to print result of bond calculation
if calculation_type == 'bond':
    repayment = bond_calc()
    repayment = float(repayment)
    print(f'Thanks for your time, your monthly repayment on the loan is £{repayment:.2f} ')