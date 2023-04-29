'''
Radix Sort Demonstration
----------------------------------
element module:
    This module contains logic associated with the elements to be sorted

HUI, Macarious Kin Fung
'''

def get_digit(element, place_value, radix):
    '''
    Function Name: get_digit
        Get the digit of the value, given the place value
    
    Parameters:
        place_value -- int, the place value of a number (1, 10, 100, etc.)
    
    Raises:
    
    Returns:
        int, the digit at the given place value
    '''
    return (element // place_value) % radix


def get_power(element, radix):
    '''
    Function Name: get_digit_count
        Find the number of digit in the element
    
    Parameters:
        None
    
    Raises:
        Nothing
    
    Returns:
        int, the power of given radix (0, 1, 2, etc.)
    '''
    power = 0
    temp = element
    while temp >= radix:
        temp = temp // radix
        power += 1

    return power
    