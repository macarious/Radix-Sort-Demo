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
import radix_sort

# For array construction and sorting logic
VALUE_MIN = 0
VALUE_MAX = 999999
ELEMENT_COUNT = 10

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
        self.step = 0
        self.running = True
        self.max_power = radix_sort.find_max_power(self.array)
        
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
        self.build_array_frame()


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
        self.button_generate = tkinter.Button(buttons_frame,
                                           text = 'GENERATE NEW ARRAY',
                                           command = self.generate_new_array,
                                           state = 'normal')
        self.button_generate.grid(column = 0, row = 0, **CONFIG_GRID)

        # Create buttons to start radix sort
        self.button_start = tkinter.Button(buttons_frame,
                                           text = 'START RADIX SORT',
                                           command = self.start_radix_sort,
                                           state = 'normal')
        self.button_start.grid(column = 1, row = 0, **CONFIG_GRID)

        # Create buttons to continue to next step
        self.button_next = tkinter.Button(buttons_frame,
                                           text = 'NEXT STEP',
                                           command = self.continue_radix_sort,
                                           state = 'disabled')
        self.button_next.grid(column = 2, row = 0, **CONFIG_GRID)


    def build_array_frame(self):
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
        array_frame.grid(column = 0, row = (self.step + 1), **CONFIG_GRID)

        # Create labels for displaying headers
        label_array = ttk.Label(array_frame, text = f"Array at Step {self.step}", **CONFIG_HEADER)
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
        self.step = 0
        self.build_window()
        self.button_start.config('enabled')
        self.button_next.config('normal')


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
        power = self.step
        self.step += 1
        place_value = 10 ** power
        self.array = radix_sort.counting_sort(self.array, place_value)
        self.build_array_frame()

        self.button_start.config(state = 'disabled')
        self.button_next.config(state = 'normal')

    
    def continue_radix_sort(self):
        if self.step > self.max_power:
            self.button_start.config(state = 'normal')

        else:
            power = self.step
            self.step += 1
            place_value = 10 ** power
            self.array = radix_sort.counting_sort(self.array, place_value)
            self.build_array_frame()


