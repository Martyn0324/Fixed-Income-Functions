def rate_to_month(indicator):
    '''Converts an economic indicator(interest rate, inflation, etc) from annual to monthly time-scale'''
    ir = indicator/100
    monthly = (ir+1)**(1/12) - 1
    print(str(monthly*100) + '%')

def rate_to_daily(indicator2):
    '''Converts an economic indicator(interest rate, inflation, etc) from monthly to daily time-scale'''
    ir2 = indicator2/100
    daily = (ir2+1)**(1/30) - 1
    print(str(daily*100) + '%')

def back_to_month(indicator3):
    '''Converts an economic indicator(interest rate, inflation, etc) from daily to monthly time-scale'''
    ir3 = indicator3/100
    monthly2 = (ir3+1)**30 - 1
    print(str(monthly2*100) + '%')

def back_to_annual(indicator4):
    '''Converts an economic indicator(interest rate, inflation, etc) from monthly to annual time-scale'''
    ir4 = indicator4/100
    annual = (ir4+1)**12 - 1
    print(str(annual*100) + '%')

def from_day_to_year(indicator5):
    '''Converts an economic indicator(interest rate, inflation, etc) from daily to annual time-scale'''
    ir5 = indicator5/100
    annual2 = (ir5+1)**360 - 1
    print(str(annual2*100) + '%')

def fixed_income(capital,interest,time):
    '''Returns the profit from an investment considering the starting capital, interest rate and application time. Doesn't consider inflation for the period'''
    j = interest/100
    profit = capital*(1+j)**time
    return profit

def fi_conttribution(startcapital, monthly_deposit, interest, time):
    '''Returns the profit from an investment considering the starting capital, monthly deposits, interest rate and application time.
Doesn't consider inflation for the period'''
    jj = (interest/100) + 1
    '''The starting capital acts as an independent deposit, with jj as interest rate multiplying it for t time'''
    SC = startcapital * jj**time
    '''The monthly deposit, on the other hand, behave as a Geometric Progression, beginning with a1 = monthly_deposit and ratio = jj. So, if monthly_deposit=100,
Then, a1=100, a2=100+100*jj, a3=100+100*jj+100*jj**2 and so on. The formula to calculate the sum of a geometric progression is Sn = a1*(q**n - 1)/q-1.
In this case, n = time-1, q = jj, a1 = monthly_deposit'''
    Sn = monthly_deposit * (jj**(time-1) - 1)/(jj-1)
    final = SC+Sn
    return final

