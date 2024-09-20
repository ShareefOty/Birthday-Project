'''
This file holds various functions to get input from the user,
making sure they are entering in valid input.
'''

def get_int_inrange(min_value, max_value):
    '''
    Return a value that the user has entered that is in the
    specified range (inclusive of both min and max).
    '''
    value = int(input(f'Enter an integer between {min_value} and {max_value}: '))
    # as long as the input is not in valid range, keep asking
    while not (min_value <= value <= max_value):
        value = int(input(f'   In range {min_value} to {max_value}: '))

    return value

def get_float_inrange(min_value, max_value):
    '''
    Return a value that the user has entered that is in the
    specified range (inclusive of both min and max).
    '''
    value = float(input(f'Enter a float between {min_value} and {max_value}: '))
    # as long as the input is not in valid range, keep asking
    while not (min_value <= value <= max_value):
        value = float(input(f'   In range {min_value} to {max_value}: '))

    return value

def get_string_inlist(list_options):
    '''
    Return a value that the user has entered that is in the
    specified list.
    '''
    value = input(f'Enter value from {list_options}: ')
    # as long as the input is not in the list, keep asking
    while value not in list_options:
        value = input(f'   From {list_options}: ')

    return value

def get_number_inlist(list_options):
    '''
    Return a number (as float) that the user has entered that is in the
    specified list.
    '''
    value = float(input(f'Enter number from {list_options}: '))
    # as long as the input is not in the list, keep asking
    while value not in list_options:
        value = float(input(f'   From {list_options}: '))

    return value

if __name__ == '__main__':
    print('ENTERED',get_int_inrange(1,10))
    print('ENTERED',get_float_inrange(1,10))
    print('ENTERED',get_string_inlist(['a','an','the','this','that','other']))
    print('ENTERED',get_number_inlist([5,23,54.5,46,17.2]))
    
    
