from get_input import *
from days_calculator import *

def print_menu():
    print('Menu Options ________________________________________')
    print('1 Calculate age (years) given a birthdate')
    print('2 Calculate days since month/day')
    print('3 Calculate days until month/day')
    print('4 quit')
    print('_____________________________________________________')

keep_using = True
while keep_using:
    print()
    print_menu()
    response = get_int_inrange(1,4)
    print()

    # no longer using - quit
    if response==4:
        keep_using = False

    elif response == 1:
        print('Enter a birth date')
        date = get_date()
        years = age(date)
        print(f'You are {years} years old.')
        
    elif response == 2:
        month,day = get_month_day()
        today = get_today()
        days = days_between_dates([month,day],today)
        print("Given today's date:",end=' ')
        print_date(today)
        print(f'There have been {days} days since',end=' ')
        print_date([month,day])


    elif response == 3:
        date = get_month_day()
        today = get_today()
        days = days_between_dates(today,date)
        print("Given today's date:",end=' ')
        print_date(today)
        print(f'There are {days} days until',end=' ')
        print_date(date)

    else:
        print('Input not recognized')



print('Bye!')
        
