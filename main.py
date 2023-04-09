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
    array = [590, 9581, 1572, 8563, 2554, 7545, 3536, 257, 81, 5]
    
    # Run demo
    root = Tk()
    Demo(root, array)
    root.mainloop()

if __name__ == '__main__':
    main()
    