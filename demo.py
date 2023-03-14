'''
CS 5008 - Radix Sort Demonstration

Demonstration of Radix Sort
Demo class -- see docstring below

HUI, Macarious Kin Fung
LI, Yunke
ZHANG, Yufei
'''

import tkinter
from tkinter import ttk
from random import randint
from element import Element

# For array construction and sorting logic
VALUE_MIN = 0
VALUE_MAX = 1000000
ELEMENT_COUNT = 10
BASE = 10

# For demonstration
ELEMENT_WIDTH = 80
ELEMENT_HEIGHT = 40
GAP = 0.20 * ELEMENT_WIDTH
CONFIG_CANVAS = {
    'highlightthickness' : 0,
    'background' : 'gray40',
}
CONFIG_ELEMENT_TEXT = {
    'fill' : 'gray20',
    'font' : ('Calibri', 12),
}
CONFIG_ELEMENT_RECT = {
    'fill' : 'white',
    'outline' : 'black',
    'width' : 1,
}
CONFIG_GRID = {
    'sticky' : 'nsew',
    'padx' : 2,
    'pady' : 2,
}
CONFIG_FRAME = {
    'background' : 'gray40',
    'highlightthickness' : 1,
    'highlightcolor' : 'white',
}
CONFIG_HEADER = {
    'anchor' : 'w',
    'background' : 'gray40',
    'font' : ('Calibri', 16),
    'foreground' : 'white',
}
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

class Demo:
    '''
    This class provides a graphical interface for a demonstration of radix sort.
    '''

    def __init__(self, root, array):
        '''
        Function Name: __init__
            Constructor for the Demo class.
        
        Parameters:
            root -- Tk, root node for tkinter
            array -- list of Element, a list to be sorted
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        self.root = root
        self.array = array
        self.running = True
        
        # Set properties of demo window
        self.root.title('CS 5008 - Radix Sort Demo')
        self.root.configure(bg = 'gray20')
        self.build_window()


    def build_window(self):
        '''
        Function Name: build_window
            Build the application window for a graphical user interface
        
        Parameters:
            Nothing
        
        Raises:
            Nothing
        
        Returns:
            None
        '''
        self.destroy_all(self.root)
        self.build_button_frame()
        self.build_array_frame(0)


    def build_button_frame(self):
        '''
        Function Name: build_button_frame
            Build a frame which contains buttons for navigation
        
        Parameters:
            None
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        # Create a frame for the buttons
        buttons_frame = tkinter.Frame(self.root, **CONFIG_FRAME)
        buttons_frame.grid(column = 0, row = 0, **CONFIG_GRID)

        # Create buttons to generate a new array
        button_generate = tkinter.Button(buttons_frame,
                                           text = 'GENERATE NEW ARRAY',
                                           command = self.generate_new_array,
                                           state = 'normal')
        button_generate.grid(column = 0, row = 0, **CONFIG_GRID)

        # Create buttons to start radix sort
        button_generate = tkinter.Button(buttons_frame,
                                           text = 'START RADIX SORT',
                                           command = self.start_radix_sort,
                                           state = 'normal')
        button_generate.grid(column = 1, row = 0, **CONFIG_GRID)

        # Create buttons to continue to next step
        self.button_next = tkinter.Button(buttons_frame,
                                           text = 'NEXT STEP',
                                           command = self.continue_to_next,
                                           state = 'disabled')
        self.button_next.grid(column = 2, row = 0, **CONFIG_GRID)


    def build_array_frame(self, step):
        '''
        Function Name: build_array_frame
            Build a frame which displays the initial array
        
        Parameters:
            step -- int, current step number
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        # Create a frame for the initial array
        array_frame = tkinter.Frame(self.root, **CONFIG_FRAME)
        array_frame.grid(column = 0, row = (step + 1), **CONFIG_GRID)

        # Create labels for displaying headers
        label_array = ttk.Label(array_frame, text = f"Array at Step {step}", **CONFIG_HEADER)
        label_array.grid(column = 0, row = 0, **CONFIG_GRID)

        # Create canvas widget to draw the array
        width = ELEMENT_COUNT * (GAP + ELEMENT_WIDTH) + GAP
        height = ELEMENT_HEIGHT + 2 * GAP
        canvas_array = tkinter.Canvas(array_frame, width = width, height = height, **CONFIG_CANVAS)
        canvas_array.grid(column = 0, row = 1, **CONFIG_GRID)

        # Draw the array on the canvas
        self.draw_array(canvas_array)


    def generate_new_array(self):
        '''
        Function Name: generate_array
            Generate a randomized array
        
        Parameters:
            size -- int, the number of elements in the array
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        array = []
        for i in range(ELEMENT_COUNT):
            new_element = Element(randint(VALUE_MIN, VALUE_MAX))
            array.append(new_element)
            
        # Overwrite existing array
        self.array = array
        self.build_window()


    def destroy_all(self, parent):
        '''
        Function Name: destroy_all
            Destroy all child widgets from parent
        
        Parameters:
        
        Raises:
        
        Returns:
        '''
        for child in parent.winfo_children():
            child.destroy()


    def pause(self):
        '''
        Function Name: pause
            Pauses the demo until "next" is triggered
        
        Parameters:
            None
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        self.running = False
        self.button_next.config(state = 'normal')


    def continue_to_next(self):
        '''
        Function Name: continue_to_next
            Continues to run after the demo is paused at predetermined points
        
        Parameters:
            None
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        self.running = True
        self.button_next.config(state = 'disabled')


    def draw_array(self, canvas):
        '''
        Function Name: draw_array
            Draws the array on canvas
        
        Parameters:
            array -- list of Elements
            canvas -- Canvas, widget in tkinter use to display the array
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        for i in range(len(self.array)):
            canvas.create_rectangle(
                GAP + i * (GAP + ELEMENT_WIDTH), # pixels, horizontal distance to left edge
                GAP, # pixels, vertical distance to upper edge
                GAP + i * (GAP + ELEMENT_WIDTH) + ELEMENT_WIDTH, # pixels, horizontal distance to right edge
                GAP + ELEMENT_HEIGHT, # pixels, vertical distance to lower edge
                **CONFIG_ELEMENT_RECT,
            )
            canvas.create_text(
                GAP + i * (GAP + ELEMENT_WIDTH) + ELEMENT_WIDTH * 0.5, # pixels, horizontal distance to centre of text
                GAP + ELEMENT_HEIGHT * 0.5, # pixels, vertical distance to centre of text
                text = self.array[i].value,
                **CONFIG_ELEMENT_TEXT,
            )


    def start_radix_sort(self):
        '''
        Function Name: start_bfs
            Starts the radix sort algorithm
        
        Parameters:
            Nothing
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        # Find highest place value
        max_value = max(self.array, key = lambda element: element.value).value
        max_place_power = 0
        while max_value >= 10:
            max_value = max_value // 10
            max_place_power += 1
        
        for power in range(max_place_power + 1):
            place_value = 10 ** power
            self.array = counting_sort(self.array, place_value)
            self.build_array_frame(power + 1)
      

def counting_sort(array, place_value):
    '''
    Function Name: counting_sort
        Performs counting sort on a specified digit in the elements of an array
    
    Parameters:
        array -- list of Element, the items to be sorted
        digit -- int, the n place of a number (1, 10, 100, etc.)
    
    Raises:
        Nothing
    
    Returns:
        list of Elements, an array sorted by a specified digit
    '''
    length = len(array)
    list_sorted = [0] * length # List sorted by counting sort by a specified digit
    list_digit_counter = [0] * length # List to count the occurence of each digit

    # Count the number of occurences of each digit
    for i in range(length):
        digit = (array[i].value // place_value) % BASE
        list_digit_counter[digit] += 1

    # Calculate the cumulative count, which is equivalent to the position of the digit
    # in the sorted array
    for i in range(1, BASE):
        list_digit_counter[i] += list_digit_counter[i - 1]

    # Construct the sorted array in reverse
    for i in range(length - 1, -1, -1):
        digit = (array[i].value // place_value) % BASE
        list_sorted[list_digit_counter[digit] - 1] = array[i]
        list_digit_counter[digit] -= 1

    return list_sorted