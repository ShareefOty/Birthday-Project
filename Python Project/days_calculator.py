from datetime import date
from get_input import *


months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
          'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

days_in_months = [ 31, 28, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31 ]

'''
Dates will be stored as a list in this order: [ month, day, year ]
So,
- date[0] is the month
- date[1] is the day
- date[2] is the year
'''

def get_today():
    '''
    Use the imported date module to get today's date
    then parse into month day year
    '''
    year = date.today().year
    month_no = date.today().month
    month = months[month_no-1]
    day = date.today().day

    return [ month, day, year ]

def print_date(adate):
    '''
    Nicely format the date. Could be month+day or month+day+year
    '''
    month = adate[0].capitalize()
    day = adate[1]
    # include the year too, if it is part of the date
    if len(adate)==3:
        print(f'{month} {day}, {adate[2]}')
    else:
        print(f'{month} {day}')

def get_month_day():
    '''
    From the user, get a month and a day.
    The month must be Jan to Dec
    and the days must be valid for the given month
    '''
    month = get_string_inlist(months)
    
    # determine range of days for given month
    ## (#2) FIX THIS VARIABLE ASSIGNMENT
    month_index=months.index(month)
    max_days =  days_in_months[month_index]
    day = get_int_inrange(1,max_days)

    return month, day
    

def get_date():
    '''
    From the user, get a month, day, and year.
    The called functions check the validity of the user input.
    '''
    month, day = get_month_day()
    year = get_int_inrange(1890,9999)
    return [month, day, year]

### (#3) ___________ PRIMARY BASE LEVEL REQUIREMENT ______________

def age(birthdate):
    '''
    Calculates the age given a birth date. Returns the age in years.
    '''
    today = get_today()
    print(today,birthdate)
    today_month_index=month.index(today[0])
    birthdate_month_index=month.index(birthdate[0])
    if ((today[0]==birthdate[1]) and (today[1]==birthdate[1])):
         print('H a a p p y  B i r t h d a y ! ! !')
         age = today[2]-birthdate[2]
    elif ((today_month_index<birthdate_month_index)):
        age=(today[2]-birthdate[2])
    else:
        age=(today[2]-birthdate[2])
        return years





