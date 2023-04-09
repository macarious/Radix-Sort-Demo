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
RADIX = 10 # Default to base 10

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
        # 0 -- Original array (not used in counting_sort())
        # 1 -- Unsorted array of current step
        # 2 -- Counting array used for current step
        # 3 -- Sorted array of current step
        # 4 -- Final sorted array
        self.current_frame_step = 0

        # Substeps in frame 2 (from 0 to array length + 1)
        self.current_substep = 0

        self.radix_sort = RadixSort(array, RADIX)
        self.gui = GraphicalUserInterface(root, self)
        self.initialize_gui()


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

    
    def get_current_frame_step(self):
        '''
        Function Name: get_current_substep
            Returns the current frame step count
        
        Parameters:
            None
        
        Raises:
            Nothing
        
        Returns:
            int, current frame step
        '''
        return self.current_frame_step

    
    def get_current_substep(self):
        '''
        Function Name: get_current_substep
            Returns the current substep count
        
        Parameters:
            None
        
        Raises:
            Nothing
        
        Returns:
            int, current substep
        '''
        return self.current_substep


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
        self.current_frame_step = 0
        self.current_substep = 0
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
        # Automatically goes to frame_step 1 if it is in frame_step 0
        if self.current_frame_step == 0:
            self.current_frame_step = 1

        # Display unsorted array.
        if self.current_frame_step == 1:
            self.radix_sort.increment_step_count()
            self.gui.set_radix_sort_parameters(self.radix_sort)
            print(f"step count {self.radix_sort.get_step_count()}")
            print(f"max power {self.radix_sort.get_max_power()}")

            self.gui.display_step()

            # Perform counting sort.
            step = self.radix_sort.get_step_count()
            place_value = RADIX ** step # Step count corresponds to the current power
            self.radix_sort.counting_sort(place_value)

            # Update parameters.
            self.gui.set_radix_sort_parameters(self.radix_sort)
            self.current_frame_step = 2
        
        # Display counting array.
        elif self.current_frame_step == 2:
            self.gui.display_step()
            self.current_frame_step = 3
            self.gui.display_step()

            # Goes back to frame_step 1 when all substeps are displayed
            if self.current_substep > len(self.radix_sort.get_array()):
                self.current_frame_step = 1
                self.current_substep = 0

            else: # Continue displaying the counting arrays
                self.current_frame_step = 2
                self.current_substep += 1
    
            if self.radix_sort.is_sorted():
                self.current_frame_step = 4 # current_frame_step == 4
                self.gui.display_step()
                self.gui.disable_next_button()


