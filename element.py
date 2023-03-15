'''
CS 5008 - Radix Sort Demonstration

Demonstration of Radix Sort
Element Class -- see docstring below

HUI, Macarious Kin Fung
LI, Yunke
ZHANG, Yufei
'''

BASE = 10 # Sort using base-10 decimal system
COLOUR = {
    'red',
    'pink',
    'orange',
     'yellow',
    'green',
    'blue',
    'cyan',
    'magenta',
    'purple',
    'brown',
}

class Element:
    '''
    This class represents an element in an array which is to be sorted.
    '''
    
    def __init__(self, value):
        '''
        Function Name: __init__
            Constructor for Element class
        
        Parameters:
            value -- int, value of the element
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        self.value = value
        self.place_value = 1
        self.current_digit = 0
        self.colour = "black"


    def get_colour(self, place_value):
        digit = (self.value // place_value) % BASE
        self.colour = COLOUR[digit]


    def get_digit(self, place_value):
        '''
        Function Name: get_digit
            Get the digit of the value, given the place value
        
        Parameters:
            place_value -- int, the place value of a number (1, 10, 100, etc.)
        
        Raises:
        
        Returns:
            int, the digit at the given place value
        '''
        return (self.value // place_value) % BASE


    def get_digit_count(self):
        '''
        Function Name: get_digit_count
            Find the number of digit in the element
        
        Parameters:
            None
        
        Raises:
            Nothing
        
        Returns:
            int, number of digits (1, 2, 3, etc.)
        '''
        digit_count = 1
        temp = self.value
        while temp >= 10:
            temp = temp // 10
            digit_count += 1

        return digit_count
        