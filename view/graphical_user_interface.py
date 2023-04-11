'''
CS 5008 - Radix Sort Demonstration
----------------------------------
GraphicalUserInterface class:
    This class provides a graphical interface for a demonstration of radix sort.

HUI, Macarious Kin Fung
LI, Yunke
ZHANG, Yufei
'''

import tkinter
from tkinter import ttk

from model.element import get_digit

TITLE = 'CS 5008 - Radix Sort Demo'
BACKGROUND_COLOUR = 'gray20'
ELEMENT_WIDTH_PER_DIGIT = 25
ELEMENT_HEIGHT = 40
GAP_HORIZONTAL = 20
GAP_VERTICAL = 10
DASH_PARAMETER = (4, 4)
BACKGROUND_COLOUR = 'gray10'
CONFIG_CANVAS = {
    'highlightthickness' : 0,
    'background' : BACKGROUND_COLOUR,
}
THEME_COLOUR = {
    'original' : 'red2',
    'sorted' : 'SeaGreen1',
    'plain' : 'gray70',
    'highlighted' : 'gray90',
}
CONFIG_FRAME = {
    'background' : BACKGROUND_COLOUR,
    'highlightthickness' : 1,
    'highlightcolor' : 'white',
}
CONFIG_HEADER = {
    'anchor' : 'w',
    'background' : BACKGROUND_COLOUR,
    'font' : ('Calibri', 16, 'bold'),
}
CONFIG_TEXT = {
    'original' : {'fill' : THEME_COLOUR['original'], 'font' : ('Calibri', 14, 'bold'),},
    'sorted' : {'fill' : THEME_COLOUR['sorted'], 'font' : ('Calibri', 14, 'bold'),},
    'plain' : {'fill' : THEME_COLOUR['plain'], 'font' : ('Calibri', 14, 'bold'),},
    'highlighted' : {'fill' : THEME_COLOUR['highlighted'], 'font' : ('Calibri', 14, 'bold'),},
}
CONFIG_RECT = {
    'original' : {'outline' : THEME_COLOUR['original'], 'fill' : 'gray20', 'width' : '2',},
    'sorted' : {'outline' : THEME_COLOUR['sorted'], 'fill' : 'gray20', 'width' : '2',},
    'plain' : {'outline' : THEME_COLOUR['plain'], 'fill' : 'gray20', 'width' : '1',},
    'highlighted' : {'outline' : THEME_COLOUR['highlighted'], 'width' : '2', 'dash' : (4, 4),},
}
DIGIT_HIGHLIGHT = [
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


class GraphicalUserInterface:
    '''
    This class provides a graphical interface for a demonstration of radix sort.
    '''

    def __init__(self, root, controller):
        '''
        Function Name: __init__
            Constructor for the GraphicalUserInterface class.
        
        Parameters:
            root -- Tk, root node for tkinter
            controller -- Controller, the controller of the demo
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        self.root = root
        self.controller = controller
        self.step_display_count = 0
        self.step_display_header = "Original Array"
        self.current_frame = 0


    def set_radix_sort_parameters(self, radix_sort):
        '''
        Function Name: set_radix_sort_parameters
            Set the parameters from the current state of the radix sort algorithm
        
        Parameters:
            radix_sort -- RadixSort, algorithm being demonstrated
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        self.step_count = radix_sort.get_step_count()
        self.max_power = radix_sort.get_max_power()
        self.element_count = radix_sort.get_element_count()
        self.is_sorted = radix_sort.is_sorted()
        self.radix = radix_sort.get_radix()
        self.array = radix_sort.get_array()


    def build_gui_window(self):
        '''
        Function Name: build_gui_window
            Building the GUI window.
        
        Parameters:
            None
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        self.root.title(TITLE)
        self.root.configure(bg = BACKGROUND_COLOUR)
        self.root.resizable(False, False)
        self._build_control_container()
        self._build_display_container()


    def reset_display_container(self):
        '''
        Function Name: reset_display_container
            Resets the display container and display a new array
        
        Parameters:
            None
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        self.display_container.destroy()
        self._build_display_container()
        self.enable_next_button()


    def display_step(self):
        '''
        Function Name: show_intermediate_step
            Display an intermediate step
        
        Parameters:
            current_frame -- int, the current frame number to be displayed in (starts at 0)
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        self._build_individual_step_frame()

    
    def enable_next_button(self):
        '''
        Function Name: disable_next_button
            Enable the 'Next Step' button
        
        Parameters:
            None
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        self.button_next.config(state = 'normal')

    
    def disable_next_button(self):
        '''
        Function Name: disable_next_button
            Disable the 'Next Step' button
        
        Parameters:
            None
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        self.button_next.config(state = 'disabled')


    def get_current_frame(self):
        '''
        Function Name: get_current_frame
            Get the current frame number (starts at 0)
        
        Parameters:
            None
        
        Raises:
            Nothing
        
        Returns:
            int, frame index (row number) of current display frame
        '''
        return self.current_frame


    def set_current_frame(self, frame_index):
        '''
        Function Name: set_current_frame
            Updates the current frame number (starts at 0)
        
        Parameters:
            frame_index -- int, row number of current frame
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        self.current_frame = frame_index


    def _build_control_container(self):
        '''
        Function Name: _build_control_container
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
                                           command = self.controller.generate_new_array,
                                           state = 'normal')
        self.button_generate.grid(column = 0, row = 0, **CONFIG_GRID)

        # Create buttons to continue to next step
        self.button_next = tkinter.Button(self.control_container,
                                           text = 'NEXT STEP',
                                           command = self.controller.continue_radix_sort,
                                           state = 'normal')
        self.button_next.grid(column = 1, row = 0, **CONFIG_GRID)


    def _build_display_container(self):
        '''
        Function Name: _build_display_container
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
        self.step_counts_canvas = tkinter.Canvas(self.display_container, **CONFIG_FRAME)
        self.step_counts_canvas.pack(side = 'left', fill = 'y')
        self._build_individual_step_frame()


    def _build_individual_step_frame(self):
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
        # Create a frame for an individual step
        if self.step_count == self.max_power + 1:
            self.current_frame = 3

        individual_step_frame = tkinter.Frame(self.step_counts_canvas, **CONFIG_FRAME)
        individual_step_frame.grid(column = 0, row = self.current_frame, **CONFIG_GRID)

        # Create labels for displaying headers
        if self.current_frame == 0:
            header = "Original Array"
            font_colour = THEME_COLOUR['original']
        
        elif self.current_frame == 3:
            header = "Sorted Array"
            font_colour = THEME_COLOUR['sorted']

        else:
            font_colour = THEME_COLOUR['plain']
            if self.current_frame == 1:
                header = f"Array at Step {self.step_count} - before"
            
            else:
                header = f"Array at Step {self.step_count} - before"

        label_individual_step = ttk.Label(individual_step_frame, text = header, **CONFIG_HEADER, foreground = font_colour)
        label_individual_step.grid(column = 0, row = 0, **CONFIG_GRID)

        # Create canvas widget to draw the array
        width = self.element_count * (GAP_HORIZONTAL + ELEMENT_WIDTH_PER_DIGIT * (self.max_power + 1)) + GAP_HORIZONTAL
        height = ELEMENT_HEIGHT + 2 * GAP_VERTICAL
        canvas_individual_step = tkinter.Canvas(individual_step_frame, width = width, height = height, **CONFIG_CANVAS)
        canvas_individual_step.grid(column = 0, row = 1, **CONFIG_GRID)

        # Draw the array on the canvas
        if self.current_frame == 0 or self.current_frame == 3:
            self._draw_array(canvas_individual_step)

        else:
            self._draw_array_detail(canvas_individual_step)


    def _draw_array(self, canvas):
        '''
        Function Name: _draw_array
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
            self._draw_rectangle_with_label(
                canvas = canvas,
                horizontal_pos = current_position,
                vertical_pos = GAP_VERTICAL,
                width = width,
                height = ELEMENT_HEIGHT,
                label = label,
                )
            current_position += width + GAP_HORIZONTAL

    
    def _draw_array_detail(self, canvas):
        '''
        Function Name: _draw_array_detail
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
                label = get_digit(element, 10 ** (power), self.radix)
                label_parameters = {'highlighted' : False}
                if (power == self.step_count):
                    label_parameters['highlighted'] = True
                    label_parameters['background_colour'] = DIGIT_HIGHLIGHT[label]
                self._draw_rectangle_with_label(
                    canvas = canvas,
                    horizontal_pos = current_position,
                    vertical_pos = GAP_VERTICAL,
                    width = width,
                    height = ELEMENT_HEIGHT,
                    label = label,
                    **label_parameters
                    )
                current_position += width
            current_position += GAP_HORIZONTAL


    def _draw_rectangle_with_label(self, canvas, horizontal_pos, vertical_pos, width, height, label, **parameters):
        '''
        Function Name: _draw_rectangle_with_label
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
        # List of optional parameters and default value:
        highlighted = False
        if self.current_frame == 0:
            config_rect = CONFIG_RECT['original']
            config_text = CONFIG_TEXT['original']
        elif self.current_frame == 3:
            config_rect = CONFIG_RECT['sorted']
            config_text = CONFIG_TEXT['sorted']
        else:
            config_rect = CONFIG_RECT['plain']
            config_text = CONFIG_TEXT['plain']

        # Set optional parameters
        for parameter, value in parameters.items():
            if parameter == 'highlighted':
                highlighted = value
            elif parameter == 'background_colour':
                background_colour = value
            else:
                raise NameError("Unknown parameter in _draw_rectangle_with_label().")

        if highlighted:
            config_rect = CONFIG_RECT['highlighted'].copy()
            config_rect['fill'] = background_colour
            config_text = CONFIG_TEXT['highlighted']

        # Draw rectangle to represent element or digit
        canvas.create_rectangle(
            horizontal_pos, # pixels, horizontal distance to left edge
            vertical_pos, # pixels, vertical distance to upper edge
            horizontal_pos + width, # pixels, horizontal distance to right edge
            vertical_pos + height, # pixels, vertical distance to lower edge
            **config_rect,
        )

        # Label rectangle with element or digit
        canvas.create_text(
            horizontal_pos + width * 0.5, # pixels, horizontal distance to centre of text
            vertical_pos + height * 0.5, # pixels, vertical distance to centre of text
            text = label,
            **config_text,
        )


    # Fix window size and add scroll bar
    # Does not work; will be implemented in the future
    def _fix_steps_canvas_size(self):
        # width = self.step_counts_canvas.winfo_width()
        # height = self.step_counts_canvas.winfo_height()
        # print(width)
        # print(height)
        # self.step_counts_canvas.config(width = width, height = height)
        # self.step_counts_canvas.update()
        # self.display_scrollbar = tkinter.Scrollbar(self.display_container, orient = 'vertical', command = self.step_counts_canvas.yview)
        # self.display_scrollbar.pack(side = 'right', fill = 'y')
        # self.step_counts_canvas.config(yscrollcommand = self.display_scrollbar.set)
        pass


    # Not used at the moment; will be implemented for displaying finer steps
    def _update_step_display_header(self, step_count, sub_step):
        '''
        Function Name: _update_step_display_header
            _summary_
        
        Parameters:
            step_count -- int, current step number
            sub_step -- str, name of sub-step, (ex. A, B, C, ...)
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        if step_count == 0:
            self.step_display_count = 0
            self.step_display_header = "Original Array"
        else:
            self.step_display_count += 1
            self.step_display_header = f"Step: {step_count}-{sub_step}"



