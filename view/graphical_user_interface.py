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
BACKGROUND_COLOUR = 'gray20' # Default background as 'gray20'
ELEMENT_WIDTH_PER_DIGIT = 45
ELEMENT_HEIGHT = 60
GAP_HORIZONTAL = 30
GAP_VERTICAL = 15
DASH_PARAMETER = (6, 6)
CONFIG_CANVAS = {
    'highlightthickness' : 0,
}
THEME_COLOUR = {
    'original' : 'red2',
    'sorted' : 'SeaGreen1',
    'plain' : 'gray50',
    'highlighted' : 'gray90',
}
CONFIG_FRAME = {
    'highlightthickness' : 1,
    'highlightcolor' : 'white',
}
CONFIG_HEADER = {
    'anchor' : 'w',
    'font' : ('Calibri', 18, 'bold'),
}
CONFIG_TEXT = {
    'original' : {'fill' : THEME_COLOUR['original'], 'font' : ('Calibri', 24, 'bold'),},
    'sorted' : {'fill' : THEME_COLOUR['sorted'], 'font' : ('Calibri', 24, 'bold'),},
    'plain' : {'fill' : THEME_COLOUR['plain'], 'font' : ('Calibri', 24, 'bold'),},
    'highlighted' : {'fill' : THEME_COLOUR['highlighted'], 'font' : ('Calibri', 24, 'bold'),},
}
CONFIG_RECT = {
    'original' : {'outline' : THEME_COLOUR['original'], 'fill' : 'gray20', 'width' : '3',},
    'sorted' : {'outline' : THEME_COLOUR['sorted'], 'fill' : 'gray20', 'width' : '3',},
    'plain' : {'outline' : THEME_COLOUR['plain'], 'fill' : 'gray20', 'width' : '2',},
    'highlighted' : {'outline' : THEME_COLOUR['highlighted'], 'width' : '3', 'dash' : DASH_PARAMETER,},
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
    'padx' : 3,
    'pady' : 3,
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
        self.bg_colour = BACKGROUND_COLOUR


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


    def _destroy_individual_frame(self, row):
        '''
        Function Name: destroy_frame_in_row
            Destroy a child frame at specified row.
        
        Parameters:
            row -- int, row number
        
        Raises:
        
        Returns:
        '''
        for child in self.step_counts_canvas.winfo_children():
            # Check if the child widget is a frame and its grid row matches the given row
            if isinstance(child, tkinter.Frame) and child.grid_info()["row"] == row:
                child.destroy()
                break


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
        self.control_container = tkinter.Frame(self.root, **CONFIG_FRAME, background = self.bg_colour)
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

        # Create button to toggle dark/light mode
        self.button_mode = tkinter.Button(self.control_container,
                                          text = "DARK/LIGHT MODE",
                                          command = lambda: self._toggle_dark_light_mode(self.root, "white" if self.root.cget("bg") != "white" else "gray20"))
        self.button_mode.grid(column = 2, row = 0, **CONFIG_GRID)

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
        self.display_container = tkinter.Frame(self.root, **CONFIG_FRAME, background = self.bg_colour)
        self.display_container.grid(column = 0, row = 1, **CONFIG_GRID)
        self.step_counts_canvas = tkinter.Canvas(self.display_container, **CONFIG_FRAME, background = self.bg_colour)
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
        
            
        if self.current_frame == 1 and self.step_count < self.max_power + 1:
                self._destroy_individual_frame(2)

        if self.step_count == self.max_power + 1:
            self.current_frame = 3

        individual_step_frame = tkinter.Frame(self.step_counts_canvas, **CONFIG_FRAME, background = self.bg_colour)
        individual_step_frame.grid(column = 0, row = self.current_frame, **CONFIG_GRID)

        # Create labels for displaying headers
        if self.current_frame == 0:
            header = "Original Array"
            font_colour = THEME_COLOUR['original']
        
        elif self.current_frame == 3:
            header = "Sorted Array"
            font_colour = THEME_COLOUR['sorted']

        else:
            font_colour = 'gray80'
            if self.current_frame == 1:
                header = f"Array at Step {self.step_count + 1} - before"
            
            else:
                header = f"Array at Step {self.step_count + 1} - after"

        label_individual_step = ttk.Label(individual_step_frame, text = header, **CONFIG_HEADER, foreground = font_colour, background = self.bg_colour)
        label_individual_step.grid(column = 0, row = 0, **CONFIG_GRID)

        # Create canvas widget to draw the array
        width = self.element_count * (GAP_HORIZONTAL + ELEMENT_WIDTH_PER_DIGIT * (self.max_power + 1)) + GAP_HORIZONTAL
        height = ELEMENT_HEIGHT + 2 * GAP_VERTICAL
        canvas_individual_step = tkinter.Canvas(individual_step_frame, width = width, height = height, **CONFIG_CANVAS, background = self.bg_colour)
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


    def _toggle_dark_light_mode(self, window, colour):
        '''
        Function Name: _toggle_dark_light_mode
            Change the colour of the window and all its child widgets
        
        Parameters:
            window -- Tk, root node for tkinter
            colour -- String, background colour to be changed
        
        Raises:
            Nothing
        
        Returns:
            Nothing
        '''
        self.bg_colour = colour
        window.configure(bg = colour)

        # Change background colour of all children widgets recursively
        # Similar to traversing a tree
        for child in window.winfo_children():
            
            # Do not change colour of Button
            # Change colour of all other childs using 'bg' or 'background'
            if child.winfo_class() != 'Button':

                if child.winfo_class() == 'Canvas':
                    # Create a new background rectangle "background_rect" item
                    # Move the background rectangle item to the bottom of the canvas
                    # Also, delete any existing background rectangle
                    child.config(background = colour)
                    canvas_items = child.find_all()
                    for item in canvas_items:
                        tags = child.gettags(item)
                        if 'background_rect' in tags:
                            child.delete(item)
                    canvas_width = child.winfo_width()
                    canvas_height = child.winfo_height()
                    bg_rect = child.create_rectangle(-10, -10, canvas_width, canvas_height, fill = colour, tags = 'background_rect')
                    child.tag_lower(bg_rect)

                else:
                    child.configure(background = colour)

            else:
                continue


            if child.winfo_children():
                self._toggle_dark_light_mode(child, colour)


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



