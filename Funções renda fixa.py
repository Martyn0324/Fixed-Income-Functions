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
    '''The monthly deposit, on the other hand, is multiplied by a Geometric Progression that forms the interest over time. That interest begins with a1 = jj, a2 = jj², a3 = jj³ and so on.
    Then, if monthly deposit = 100, we'll have 100 at month 1, 100+100*jj at month 2, 100+100*jj+100*jj² at month 3 and so forth. That can be simplified with 100*(1*jj^0 + 1*jj + 1*jj² + 1*jj³+...),
    making the Geometric Progression quite clear and showing us that we need the summation of that progression.
    The formula to calculate the sum of a geometric progression is Sn = a1*(q**n - 1)/q-1. In this case, n = time-1, q = jj, a1 = monthly_deposit'''
    Sn = monthly_deposit * (jj**(time-1) - 1)/(jj-1)
    final = SC+Sn
    return final


def real_gain(income_rate, inflation_rate):
    '''Extract the real gain from an investment, that is, how much that investment provided considering the inflation during that period.
    income_rate and inflation must be floats.'''
    income_rate = income_rate*100
    inflation_rate = inflation_rate*100
    
    real_gain = (100+income_rate)/(100+inflation_rate)
    
    return real_gain

