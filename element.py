'''
CS 5008 - Radix Sort Demonstration

Demonstration of Radix Sort
Element Class -- see docstring below

HUI, Macarious Kin Fung
LI, Yunke
ZHANG, Yufei
'''

BASE = 10
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
            pos_initial -- int, initial index in the array
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        self.value = value
        self.current_digit = 0
        self.colour = "black"


    def get_colour(self, place_value):
        digit = (self.value // place_value) % BASE
        self.colour = COLOUR[digit]
        