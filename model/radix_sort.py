'''
Radix Sort Demonstration
----------------------------------
RadixSort class:
    This class represents the Radix Sort algorithm.

HUI, Macarious Kin Fung
'''

from random import randint

from model.element import get_power


class RadixSort:
    '''
    This class represents the Radix Sort algorithm.
    '''

    def __init__(self, array, radix):
        '''
        Function Name: __init__
            Constructor for the RadixSortArray class.
        
        Parameters:
            array -- list of int, an array to be sorted
            radix -- int, radix used in the RadixSort
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        self.array = array
        self.radix = radix
        self.step_count = 0
        self.max_power = self._find_max_power()
        self.element_count = len(array)
    

    def get_array(self):
        '''
        Function Name: get_array
            Get the list of elements
        
        Parameters:
        
        Raises:
        
        Returns:
            list of int, an array
        '''
        return self.array
    

    def get_radix(self):
        '''
        Function Name: get_radix
            Get the radix used in radix sort
        
        Parameters:
        
        Raises:
        
        Returns:
            int, radix used in the radix sort
        '''
        return self.radix


    def get_step_count(self):
        '''
        Function Name: get_step_count
            Get the step count of the algorithm
        
        Parameters:
            None
        
        Raises:
            Nothing
        
        Returns:
            int, step count
        '''
        return self.step_count
    

    def increment_step_count(self):
        '''
        Function Name: increment_step_count
            Increase step count by 1
        
        Parameters:
            Nothing
        
        Raises:
            None
        
        Returns:
            None
        '''
        self.step_count += 1
    

    def get_max_power(self):
        '''
        Function Name: get_max_power
            Get the maximum power of the array
        
        Parameters:
            None
        
        Raises:
            Nothing
        
        Returns:
            int, maximum power of array
        '''
        return self.max_power
    

    def get_element_count(self):
        '''
        Function Name: get_element_count
            Get the number of elements in the array
        
        Parameters:
            None
        
        Raises:
            Nothing
        
        Returns:
            int, number of element
        '''
        return self.element_count


    def is_sorted(self):
        '''
        Function Name: is_sorted
            Check if the array is sorted according to the step count
        
        Parameters:
            step_count -- the number of steps 
        
        Raises:
            Nothing
        
        Returns:
            bool, True if sorting is complete; False otherwise
        '''
        # Step count after final step implies array is sorted
        max_power = self._find_max_power()
        return self.step_count > (max_power + 1)

    
    def generate_new_array(self, array_size, max_digit):
        '''
        Function Name: generate_new_array
            Generate a new array (list of integers)
        
        Parameters:
            array_size -- int, the number of elements in the array
            max_digit -- int, max number of digits in each elements
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        new_array = []
        for _ in range(array_size):
            new_element = randint(0, (10 ** max_digit - 1))
            new_array.append(new_element)
        self.array = new_array
        self.step_count = 0
        self.max_power = self._find_max_power()
        

    def counting_sort(self, place_value):
        '''
        Function Name: counting_sort
            Performs counting sort on a specified digit in the 'value attribute of
            the elements of an array

        Parameters:
            place_value -- int, the place value of a number (1, 10, 100, etc.)

        Raises:
            Nothing

        Returns:
            list of int, an array sorted by a specified digit
        '''
        length = len(self.array)
        list_sorted = [0] * length # List sorted by counting sort by a specified digit
        list_digit_counter = [0] * self.radix # List to count the occurence of each digit

        # Count the number of occurences of each digit
        for element in self.array:
            digit = (element // place_value) % self.radix
            list_digit_counter[digit] += 1

        # Calculate the cumulative count, which is equivalent to the position of the digit
        # in the sorted array
        for i in range(1, self.radix):
            list_digit_counter[i] += list_digit_counter[i - 1]

        # Construct the sorted array in reverse
        for i in range(length - 1, -1, -1):
            digit = (self.array[i] // place_value) % self.radix
            list_sorted[list_digit_counter[digit] - 1] = self.array[i]
            list_digit_counter[digit] -= 1

        self.array = list_sorted


    def _find_max_power(self):
        '''
        Function Name: _find_max_power
            Find the maximum power from the values in the array
        
        Parameters:
            None
        
        Raises:
            Nothing
        
        Returns:
            int, maximum power (0, 1, 2, etc.)
        '''
        return max(map(lambda element: get_power(element, self.radix), self.array))