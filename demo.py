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
TITLE = 'CS 5008 - Radix Sort Demo'
BACKGROUND_COLOUR = 'gray20'
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
        self.root.title(TITLE)
        self.root.configure(bg = BACKGROUND_COLOUR)
        self.root.resizable(False, False)
        self.build_control_frame()
        self.build_display_frame()


    def build_control_frame(self):
        '''
        Function Name: build_control_frame
            Build a frame which contains buttons for navigation
        
        Parameters:
            None
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        # Create a frame for the buttons
        self.control_frame = tkinter.Frame(self.root, **CONFIG_FRAME)
        self.control_frame.grid(column = 0, row = 0, **CONFIG_GRID)

        # Create buttons to generate a new array
        self.button_generate = tkinter.Button(self.control_frame,
                                           text = 'GENERATE NEW ARRAY',
                                           command = self.generate_new_array,
                                           state = 'normal')
        self.button_generate.grid(column = 0, row = 0, **CONFIG_GRID)

        # Create buttons to continue to next step
        self.button_next = tkinter.Button(self.control_frame,
                                           text = 'NEXT STEP',
                                           command = self.continue_radix_sort,
                                           state = 'normal')
        self.button_next.grid(column = 1, row = 0, **CONFIG_GRID)


    def build_display_frame(self):
        '''
        Function Name: build_display_frame
            Build a frame which contains all the steps in the demo
        
        Parameters:
            None
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        # Create a frame for the initial array
        self.display_frame = tkinter.Frame(self.root, **CONFIG_FRAME)
        self.display_frame.grid(column = 0, row = 1, **CONFIG_GRID)
        self.steps_canvas = tkinter.Canvas(self.display_frame, **CONFIG_FRAME)
        self.steps_canvas.pack(side = 'left', fill = 'y')
        self.display_scrollbar = tkinter.Scrollbar(self.display_frame, orient = 'vertical', command = self.steps_canvas.yview)
        self.display_scrollbar.pack(side = 'right', fill = 'y')
        self.build_individual_step_frame()
        width = self.display_frame.winfo_screenwidth()
        height = self.display_frame.winfo_screenheight()
        print(width)
        print(height)
        self.steps_canvas.config(scrollregion = (0, 0, width, height * len(str(VALUE_MAX))), height = height * 5, width = width)
        self.steps_canvas.config(yscrollcommand = self.display_scrollbar.set)


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
        individual_step_frame = tkinter.Frame(self.steps_canvas, **CONFIG_FRAME)
        individual_step_frame.grid(column = 0, row = self.step, **CONFIG_GRID)

        # Create labels for displaying headers
        label_individual_step = ttk.Label(individual_step_frame, text = f"Array at Step {self.step}", **CONFIG_HEADER)
        label_individual_step.grid(column = 0, row = 0, **CONFIG_GRID)

        # Create canvas widget to draw the array
        width = ELEMENT_COUNT * (GAP + ELEMENT_WIDTH) + GAP
        height = ELEMENT_HEIGHT + 2 * GAP
        canvas_individual_step = tkinter.Canvas(individual_step_frame, width = width, height = height, **CONFIG_CANVAS)
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
        for _ in range(ELEMENT_COUNT):
            new_element = Element(randint(VALUE_MIN, VALUE_MAX))
            array.append(new_element)
            
        # Overwrite existing array
        self.array = array
        self.step = 0
        self.display_frame.destroy()
        self.build_display_frame()
        self.button_next.config(state = 'normal')


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
        power = self.step
        self.step += 1
        place_value = 10 ** power
        self.array = radix_sort.counting_sort(self.array, place_value)
        self.build_individual_step_frame()
    
        if self.step > self.max_power:
            self.button_next.config(state = 'disabled')


