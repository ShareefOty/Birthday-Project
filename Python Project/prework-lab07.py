
months = ['jan','feb','mar','apr','may','jun',
          'jul','aug','sep','oct','nov','dec']

days_in_months = [ 31, 28, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31 ]


def get_input_month():
    user_input = input(f'Enter a month ').lower()
    while user_input not in months:
        user_input = input('Invalid month, please try again')
        return user_input
    

def days_in(month):
  month = months
  user_input=input(f'Enter a month ')
  position = month.index(user_input)
  days = days_in_months[position]
  return month[position]

def print_months(start,end):
    start_position = months.index(start)
    end_position = months.index(end)
    while True:
        print(months[start_position].capitalize(),end=' ')
        if start_position == end_position:
            break
        start_position=(start_position + 1)%12
          
    pass

def print_months_days(start,end):
    start_position = months.index(start)
    end_position = months.index(end)
    while True:
        print(months[start_position].capitalize(),end=' ')
        if start_position == end_position:
            break
        start_position=(start_position + 1)%12
    pass

if __name__ == '__main__':
    m = get_input_month()
    d = days_in(m)
    print_months('sep','apr')
    print_months_days('nov','feb')
    



