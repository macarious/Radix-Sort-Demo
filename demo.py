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
        self.build_button_frame()
        self.build_steps_frame()


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
        self.buttons_frame = tkinter.Frame(self.root, **CONFIG_FRAME)
        self.buttons_frame.grid(column = 0, row = 0, **CONFIG_GRID)

        # Create buttons to generate a new array
        self.button_generate = tkinter.Button(self.buttons_frame,
                                           text = 'GENERATE NEW ARRAY',
                                           command = self.generate_new_array,
                                           state = 'normal')
        self.button_generate.grid(column = 0, row = 0, **CONFIG_GRID)

        # Create buttons to continue to next step
        self.button_next = tkinter.Button(self.buttons_frame,
                                           text = 'NEXT STEP',
                                           command = self.continue_radix_sort,
                                           state = 'normal')
        self.button_next.grid(column = 1, row = 0, **CONFIG_GRID)


    def build_steps_frame(self):
        '''
        Function Name: build_steps_frame
            Build a frame which contains all the steps in the demo
        
        Parameters:
            None
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        # Create a frame for the initial array
        self.steps_frame = tkinter.Frame(self.root, **CONFIG_FRAME)
        self.steps_frame.grid(column = 0, row = (self.step + 1), **CONFIG_GRID)
        self.build_individual_step_frame()


    def build_individual_step_frame(self):
        '''
        Function Name: build_step_frame
            Build a frame which displays the current step
        
        Parameters:
            None
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        # Create a frame for the initial array
        self.individual_step_frame = tkinter.Frame(self.steps_frame, **CONFIG_FRAME)
        self.individual_step_frame.grid(column = 0, row = (self.step + 1), **CONFIG_GRID)

        # Create labels for displaying headers
        label_individual_step = ttk.Label(self.individual_step_frame, text = f"Array at Step {self.step}", **CONFIG_HEADER)
        label_individual_step.grid(column = 0, row = 0, **CONFIG_GRID)

        # Create canvas widget to draw the array
        width = ELEMENT_COUNT * (GAP + ELEMENT_WIDTH) + GAP
        height = ELEMENT_HEIGHT + 2 * GAP
        canvas_individual_step = tkinter.Canvas(self.individual_step_frame, width = width, height = height, **CONFIG_CANVAS)
        canvas_individual_step.grid(column = 0, row = 1, **CONFIG_GRID)

        # Draw the array on the canvas
        self.draw_array(canvas_individual_step)


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
        self.destroy_children(self.steps_frame)
        self.build_steps_frame()
        self.button_next.config('normal')


    def destroy_children(self, parent):
        '''
        Function Name: destroy_children
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

    
    def continue_radix_sort(self):
        power = self.step
        self.step += 1
        place_value = 10 ** power
        self.array = radix_sort.counting_sort(self.array, place_value)
        self.build_steps_frame()
    
        if self.step > self.max_power:
            self.button_next.config(state = 'disabled')


