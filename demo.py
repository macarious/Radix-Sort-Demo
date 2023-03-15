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
from element import get_digit
from radix_sort import RADIX
from radix_sort import counting_sort
from radix_sort import find_max_power

# For array construction and sorting logic
VALUE_MIN = 0
VALUE_MAX = 99999
ELEMENT_COUNT = 10

# For graphical demonstration
TITLE = 'CS 5008 - Radix Sort Demo'
BACKGROUND_COLOUR = 'gray20'
ELEMENT_WIDTH_PER_DIGIT = 15
ELEMENT_HEIGHT = 40
GAP_HORIZONTAL = 20
GAP_VERTICAL = 10
DASH_PARAMETER = (4, 4)
CONFIG_CANVAS = {
    'highlightthickness' : 0,
    'background' : 'gray40',
}
ELEMENT_BACKGROUND_COLOUR = 'grey20'
CONFIG_DIGIT_TEXT_PLAIN = {
    'fill' : 'grey20',
    'font' : ('Calibri', 12),
}
CONFIG_DIGIT_TEXT_HIGHLIGHT = {
    'fill' : 'white',
    'font' : ('Calibri', 12, 'bold'),
}
CONFIG_DIGIT_RECT_PLAIN = {
    'fill' : 'grey50',
    'outline' : 'black',
    'width' : 1,
}
CONFIG_DIGIT_RECT_HIGHLIGHT = {
    'fill' : 'grey60',
    'outline' : 'blue',
    'width' : 1,
}
DIGIT_COLOUR = [
    'red2',
    'azure4',
    'magenta4',
    'dark orange',
    'SpringGreen4',
    'blue4',
    'red4',
    'cyan4',
    'purple4',
    'RoyalBlue4',
]
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
            array -- list of integers
        
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
        if (self.step == 0) or (self.step > self.max_power + 1):
            self.display_array(canvas_individual_step)

        else:
            self.display_array_detail(canvas_individual_step)
            if (self.step == (self.max_power + 1)):
                self.step += 1
                self.build_individual_step_frame()


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
        new_array = []
        for _ in range(ELEMENT_COUNT):
            new_element = randint(VALUE_MIN, VALUE_MAX)
            new_array.append(new_element)
            
        # Overwrite existing array
        self.array = new_array
        self.step = 0
        self.max_power = find_max_power(self.array)
        self.display_container.destroy()
        self.build_display_container()
        self.button_next.config(state = 'normal')


    def display_array(self, canvas):
        '''
        Function Name: display_array
            Display the array on canvas
        
        Parameters:
            canvas -- Canvas, widget in tkinter use to display the array
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        current_position = GAP_HORIZONTAL # pixels, horizontal distance to left edge
        for element in self.array:
            width = ELEMENT_WIDTH_PER_DIGIT * (self.max_power + 1)
            label = element
            self.draw_rectangle_with_label(
                canvas = canvas,
                horizontal_pos = current_position,
                vertical_pos = GAP_VERTICAL,
                width = width,
                height = ELEMENT_HEIGHT,
                label = label,
                dash = False,
                highlighted = True,
                )
            current_position += width + GAP_HORIZONTAL

    
    def display_array_detail(self, canvas):
        '''
        Function Name: display_array_detail
            Display the array with highlighed digits on canvas
        
        Parameters:
            canvas -- Canvas, widget in tkinter use to display the array
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        current_position = GAP_HORIZONTAL # pixels, horizontal distance to left edge
        for element in self.array:
            for power in range(self.max_power, -1, -1):
                width = ELEMENT_WIDTH_PER_DIGIT
                label = get_digit(element, 10 ** (power), RADIX)
                label_parameters = {'highlighted' : False}
                if (power + 1 == self.step):
                    label_parameters['highlighted'] = True
                    label_parameters['background_colour'] = DIGIT_COLOUR[label]
                self.draw_rectangle_with_label(
                    canvas = canvas, 
                    horizontal_pos = current_position,
                    vertical_pos = GAP_VERTICAL,
                    width = width,
                    height = ELEMENT_HEIGHT,
                    label = label,
                    dash = True,
                    **label_parameters
                    )
                current_position += width
            current_position += GAP_HORIZONTAL
            

    def draw_rectangle_with_label(self, canvas, horizontal_pos, vertical_pos, width, height, label, **parameters):
        '''
        Function Name: draw_rectangle_with_label
            Draw a rectangle with a label on a given canvas with various parameters
        
        Parameters:
            canvas -- canvas, the canvas on which the rectangle to be drawn
            horizontal_pos -- int, horizontal position of the top-left corner of rectangle
            vertical_pos -- int, vertical position of the top-left corner of rectangle
            width -- int, width of rectangle
            height -- int, heigh of rectangle
            label -- int, number to be printed within the rectangle
        
        Raises:
            Exception -- if name of optional parameter is not valid
        
        Returns:
            Nothing
        '''
        # List of ptional parameters and default value:
        dash = False
        highlighted = False
        background_colour = ELEMENT_BACKGROUND_COLOUR

        # Set optional parameters
        for parameter, value in parameters.items():
            if parameter == 'dash':
                dash = value
            elif parameter == 'highlighted':
                highlighted = value
            elif parameter == 'background_colour':
                background_colour = value
            else:
                 raise Exception("Unknown parameter in draw_rectangle_with_label().")

        if highlighted:
            config_digit_rect = CONFIG_DIGIT_RECT_HIGHLIGHT.copy()
            config_digit_rect['fill'] = background_colour
            config_digit_text = CONFIG_DIGIT_TEXT_HIGHLIGHT.copy()
        else:
            config_digit_rect = CONFIG_DIGIT_RECT_PLAIN.copy()
            config_digit_text = CONFIG_DIGIT_TEXT_PLAIN.copy()
        if dash:
            config_digit_rect['dash'] = DASH_PARAMETER

        # Draw rectangle to represent element
        canvas.create_rectangle(
            horizontal_pos, # pixels, horizontal distance to left edge
            vertical_pos, # pixels, vertical distance to upper edge
            horizontal_pos + width, # pixels, horizontal distance to right edge
            vertical_pos + height, # pixels, vertical distance to lower edge
            **config_digit_rect,
        )

        # Label rectangle with element value
        canvas.create_text(
            horizontal_pos + width * 0.5, # pixels, horizontal distance to centre of text
            vertical_pos + height * 0.5, # pixels, vertical distance to centre of text
            text = label,
            **config_digit_text,
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


