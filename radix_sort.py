'''
CS 5008 - Radix Sort Demonstration

Demonstration of Radix Sort
Logic of radix sort algorithm

HUI, Macarious Kin Fung
LI, Yunke
ZHANG, Yufei
'''

RADIX = 10
from element import get_power

def find_max_power(array):
    '''
    Function Name: find_max_power
        Find the maximum power from the values in the array
    
    Parameters:
        array -- list of Element, list of item to be sorted
    
    Raises:
        Nothing
    
    Returns:
        int, maximum power (0, 1, 2, etc.)
    '''
    max_digit = max(map(lambda element: get_power(element, RADIX), array))
    return (max_digit)
    

def counting_sort(array, place_value):
    '''
    Function Name: counting_sort
        Performs counting sort on a specified digit in the 'value attribute of
        the elements of an array

    Parameters:
        array -- list of Element, to be sorted
        place_value -- int, the place value of a number (1, 10, 100, etc.)

    Raises:
        Nothing

    Returns:
        list of Elements, an array sorted by a specified digit
    '''
    length = len(array)
    list_sorted = [0] * length # List sorted by counting sort by a specified digit
    list_digit_counter = [0] * length # List to count the occurence of each digit

    # Count the number of occurences of each digit
    for element in array:
        digit = (element // place_value) % RADIX
        list_digit_counter[digit] += 1

    # Calculate the cumulative count, which is equivalent to the position of the digit
    # in the sorted array
    for i in range(1, RADIX):
        list_digit_counter[i] += list_digit_counter[i - 1]

    # Construct the sorted array in reverse
    for i in range(length - 1, -1, -1):
        digit = (array[i] // place_value) % RADIX
        list_sorted[list_digit_counter[digit] - 1] = array[i]
        list_digit_counter[digit] -= 1

    return list_sorted