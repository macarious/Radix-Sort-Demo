'''
CS 5008 - Radix Sort Demonstration
----------------------------------
main -- Driver file running the Radix Sort Demo

HUI, Macarious Kin Fung
LI, Yunke
ZHANG, Yufei
'''

from tkinter import Tk
from controller.demo import Demo

def main():
    '''
    Driver file running the radix sort demo.
    '''

    # Sample array
    array = [900590, 819581, 721572, 638563, 542554, 457545, 363536, 257, 81, 5]
    
    # Run demo
    root = Tk()
    Demo(root, array)
    root.mainloop()

if __name__ == '__main__':
    main()
    