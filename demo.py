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
from radix_sort import counting_sort
from radix_sort import find_max_power

# For array construction and sorting logic
VALUE_MIN = 0
VALUE_MAX = 999999
ELEMENT_COUNT = 10

# For graphical demonstration
TITLE = 'CS 5008 - Radix Sort Demo'
BACKGROUND_COLOUR = 'gray20'
ELEMENT_WIDTH_PER_DIGIT = 15
ELEMENT_HEIGHT = 40
GAP_HORIZONTAL = 20
GAP_VERTICAL = 10
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
        self.max_power = find_max_power(self.array)
        
        # Set properties of demo window
        self.root.title(TITLE)
        self.root.configure(bg = BACKGROUND_COLOUR)
        self.root.resizable(False, False)
        self.build_control_container()
        self.build_display_container()


    def build_control_container(self):
        '''
        Function Name: build_control_container
            Build a container which contains buttons for navigation
        
        Parameters:
            None
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        # Create a frame for the buttons
        self.control_container = tkinter.Frame(self.root, **CONFIG_FRAME)
        self.control_container.grid(column = 0, row = 0, **CONFIG_GRID)

        # Create buttons to generate a new array
        self.button_generate = tkinter.Button(self.control_container,
                                           text = 'GENERATE NEW ARRAY',
                                           command = self.generate_new_array,
                                           state = 'normal')
        self.button_generate.grid(column = 0, row = 0, **CONFIG_GRID)

        # Create buttons to continue to next step
        self.button_next = tkinter.Button(self.control_container,
                                           text = 'NEXT STEP',
                                           command = self.continue_radix_sort,
                                           state = 'normal')
        self.button_next.grid(column = 1, row = 0, **CONFIG_GRID)


    def build_display_container(self):
        '''
        Function Name: build_display_container
            Build a container which contains all the steps in the demo
        
        Parameters:
            None
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        # Create a frame for the initial array
        self.display_container = tkinter.Frame(self.root, **CONFIG_FRAME)
        self.display_container.grid(column = 0, row = 1, **CONFIG_GRID)
        self.steps_canvas = tkinter.Canvas(self.display_container, **CONFIG_FRAME)
        self.steps_canvas.pack(side = 'left', fill = 'y')
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

        # Fix size of steps_canvas and add scrollbar
        # Currently doesn't work
        if self.step == 4:
            self.fix_steps_canvas_size()


        # Create a frame for an individual step
        individual_step_frame = tkinter.Frame(self.steps_canvas, **CONFIG_FRAME)
        individual_step_frame.grid(column = 0, row = self.step, **CONFIG_GRID)

        # Create labels for displaying headers
        label_individual_step = ttk.Label(individual_step_frame, text = f"Array at Step {self.step}", **CONFIG_HEADER)
        label_individual_step.grid(column = 0, row = 0, **CONFIG_GRID)

        # Create canvas widget to draw the array
        width = ELEMENT_COUNT * (GAP_HORIZONTAL + ELEMENT_WIDTH_PER_DIGIT * (self.max_power + 1)) + GAP_HORIZONTAL
        height = ELEMENT_HEIGHT + 2 * GAP_VERTICAL
        canvas_individual_step = tkinter.Canvas(individual_step_frame, width = width, height = height, **CONFIG_CANVAS)
        canvas_individual_step.grid(column = 0, row = 1, **CONFIG_GRID)

        # Draw the array on the canvas
        if (self.step == 0):
            self.display_array(canvas_individual_step)

        else:
            self.display_array_detail(canvas_individual_step)


    def fix_steps_canvas_size(self):
        # width = self.steps_canvas.winfo_width()
        # height = self.steps_canvas.winfo_height()
        # print(width)
        # print(height)
        # self.steps_canvas.config(width = width, height = height)
        # self.steps_canvas.update()
        # self.display_scrollbar = tkinter.Scrollbar(self.display_container, orient = 'vertical', command = self.steps_canvas.yview)
        # self.display_scrollbar.pack(side = 'right', fill = 'y')
        # self.steps_canvas.config(yscrollcommand = self.display_scrollbar.set)
        pass


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
        self.display_container.destroy()
        self.build_display_container()
        self.button_next.config(state = 'normal')


    def display_array(self, canvas):
        '''
        Function Name: display_array
            Display the array on canvas
        
        Parameters:
            array -- list of Elements
            canvas -- Canvas, widget in tkinter use to display the array
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        current_position = GAP_HORIZONTAL # pixels, horizontal distance to left edge
        for element in self.array:
            width = ELEMENT_WIDTH_PER_DIGIT * (self.max_power + 1)
            label = element.get_value()
            self.draw_rectangle_with_label(canvas, current_position, GAP_VERTICAL, width, ELEMENT_HEIGHT, label)
            current_position += width + GAP_HORIZONTAL

    
    def display_array_detail(self, canvas):
        current_position = GAP_HORIZONTAL # pixels, horizontal distance to left edge
        for element in self.array:
            for power in range(self.max_power + 1):
                width = ELEMENT_WIDTH_PER_DIGIT
                label = element.get_digit(10 ** power)
                self.draw_rectangle_with_label(canvas, current_position, GAP_VERTICAL, width, ELEMENT_HEIGHT, label)
                current_position += width
            current_position += GAP_HORIZONTAL
            

    def draw_rectangle_with_label(self, canvas, horizontal_pos, vertical_pos, width, height, label):
        # Draw rectangle to represent element
        canvas.create_rectangle(
            horizontal_pos, # pixels, horizontal distance to left edge
            vertical_pos, # pixels, vertical distance to upper edge
            horizontal_pos + width, # pixels, horizontal distance to right edge
            vertical_pos + height, # pixels, vertical distance to lower edge
            **CONFIG_ELEMENT_RECT,
        )
        # Label rectangle with element value
        canvas.create_text(
            horizontal_pos + width * 0.5, # pixels, horizontal distance to centre of text
            vertical_pos + height * 0.5, # pixels, vertical distance to centre of text
            text = label,
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
        self.array = counting_sort(self.array, place_value)
        self.build_individual_step_frame()
    
        if self.step > self.max_power:
            self.button_next.config(state = 'disabled')


