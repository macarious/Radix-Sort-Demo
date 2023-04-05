'''
CS 5008 - Radix Sort Demonstration
----------------------------------
Demo class:
    This class acts as the controller of the radix sort demonstration.

HUI, Macarious Kin Fung
LI, Yunke
ZHANG, Yufei
'''

from model.element import get_digit
from view.graphical_user_interface import GraphicalUserInterface
from model.radix_sort import RadixSort


ARRAY_SIZE = 10 # FUTURE: implement sliders in gui for customization
MAX_DIGIT = 4 # FUTURE: implement sliders in gui for customization
MAX_SUBSTEP = 2

class Demo:
    '''
    This class provides a graphical interface for a demonstration of radix sort.
    '''

    def __init__(self, root, array):
        '''
        Function Name: __init__
            Constructor for the Controller class.
        
        Parameters:
            root -- Tk, root node for tkinter
            array -- list of integers
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        self.radix_sort = RadixSort(array, 10)
        self.gui = GraphicalUserInterface(root, self)
        self.initialize_gui()
        self.substep = 0


    def initialize_gui(self):
        '''
        Function Name: initialize_gui
            Pass current state of radix sort to gui, and build initial display
        
        Parameters:
            None
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        self.gui.set_radix_sort_parameters(self.radix_sort)
        self.gui.build_gui_window()


    def generate_new_array(self):
        '''
        Function Name: generate_array
            Generate a randomized array and display it in gui
        
        Parameters:
            size -- int, the number of elements in the array
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        array_size = ARRAY_SIZE # FUTURE: implement sliders in gui for customization
        max_digit = MAX_DIGIT # FUTURE: implement sliders in gui for customization
        self.radix_sort.generate_new_array(array_size, max_digit)

        # Pass current state of radix sort to view, and display current step.
        self.gui.set_radix_sort_parameters(self.radix_sort)
        self.gui.reset_display_container()

    
    def continue_radix_sort(self):
        '''
        Function Name: continue_radix_sort
            Execute and display one more step of radix sort
        
        Parameters:
            None
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        power = self.radix_sort.get_step_count()
        place_value = 10 ** power
        if (self.substep > MAX_SUBSTEP + 1):
            self.substep = 0
            self.radix_sort.increment_step_count()

        # Display state of radix sort before counting sort.
        if (self.substep == 0):
            self.gui.set_radix_sort_parameters(self.radix_sort)
            self.gui.display_step(self.substep)
            self.radix_sort.counting_sort(place_value)

        # Pass current state of radix sort to view, and display current step.
        self.substep += 1
        self.gui.set_radix_sort_parameters(self.radix_sort)
        self.gui.display_step(self.substep)

        if self.radix_sort.is_sorted():
            self.gui.disable_next_button()
            self.substep = 0


