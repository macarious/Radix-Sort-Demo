# Radix Sort Demo<br>

## 1. About/Overview

![Progarm Overview](https://github.com/macarious/Radix-Sort-Demo/blob/main/screenshots/02-program-final-step.png "Program Overview")
<br>

The Radix Sort demonstration showcases a comprehensive illustration of the Radix Sort algorithm. The demonstration provides a visual guide on each step involved in the sorting process. Additionally, the tool allows users to customize the number of integers generated in the random array, as well as the maximum number of digits that each integer can have. Users can make changes to these variables by modifying the code directly.<br>

In the program, Counting Sort is used as the subroutine. Radix Sort algorithm sorts the elements by processing their digits from the least significant digit to the most significant digit. At each step, the elements are sorted using Counting Sort, which counts the occurrences of each digit and determines the correct position of each element in the sorted sequence. This process is repeated for each digit, and at the end, the elements are sorted in the correct order. Radix Sort using Counting Sort has a time complexity of O(d*(n+k)), where d is the number of digits, n is the number of elements, and k is the range of the input elements. This makes it a linear time algorithm when the number of digits is constant, and it can be more efficient than other comparison-based sorting algorithms for large datasets with a small range of values.

## 2. Technologies

This project was built using:

- Python 3.5 or higher
- Tkinter module for Python

## 3. System Requirements

This program should work on any system that has Python 3.5 or higher installed.

## 4. Installation

1. Clone or download the repository to your local machine.
2. Install the Tkinter module if it is not already installed on your system.

## 5. Usage

1. Open the terminal or command prompt and navigate to the directory where the program, including the subdirectories, is located.
2. A default array can be manually typed in in main() under `#Sample array`.
3. Run the program using the command:
> python main.py.
4. The program will display a window with the sample array and three buttons: `GENERATE NEW ARRAY`, `NEXT STEP`, and `DARK/LIGHT MODE`.

![Initial Array](https://github.com/macarious/Radix-Sort-Demo/blob/main/screenshots/01-program-overview.png "Initial Array")

5. `GENERATE NEW ARRAY` will randomly generate a new array of size 6, and each element is an integer has a maximum of 3 digits.
6. `NEXT STEP` will show the next step in the radix sort. It highlights which digit it is currently sorting. It always starts with the least significant digit.

![Step 1](https://github.com/macarious/Radix-Sort-Demo/blob/main/screenshots/03-program-step-one.png "Step 1")

7. The `NEXT STEP` button can be clicked again until the array is completely sorted. At that point, the `NEXT STEP` button will be disabled until a new array is generated using the `GENERATE NEW ARRAY` button.

8. `DARK/LIGHT MODE` will toggle between dark and light mode. This only affects the colour used in the grpahical user interface.

## 6. Known Issues and Limitations

- The number of elements in the array and the maximum number of digits in each element is not customizable from the GUI. This can only be done by editing the constants in the code.
- The detail of the Counting Sort subroutine used in the Radix Sort is not presented visually. This is planned for a future version, and when it is available, this will greatly enhance the ability for user to understand the algorithm.

## 7. Takeaway from Demo

__Usage:__
- Radix Sort is an efficient sorting algorithm for large datasets with a small range of values, especially when the number of digits is constant.
- It can be used to sort various data types such as integers and strings.
- Radix Sort can be implemented using different subroutines such as Counting Sort and Bucket Sort.

__Pros:__
- Radix Sort has a linear time complexity, which means its runtime increases linearly with the size of the input data.
- It does not require any comparisons between elements, making it faster than comparison-based sorting algorithms for large datasets.
- It is a stable sorting algorithm, which means it maintains the relative order of equal elements in the sorted output.

__Cons:__
- Radix Sort requires additional memory to store the temporary arrays used for sorting, which can be a problem for large datasets.
- The speed of Radix Sort depends on the length of the input data, which can cause performance issues for data with varying lengths.
- Radix Sort may not be the best choice for small datasets or datasets with a large range of values.

__Big-O:__
- The time complexity of Radix Sort is O(d*(n+k)), where d is the number of digits, n is the number of elements, and k is the range of the input elements.
- When the number of digits is constant, the time complexity of Radix Sort becomes linear, making it faster than comparison-based sorting algorithms such as QuickSort and MergeSort.
- The space complexity of Radix Sort is O(n+k), where n is the number of elements and k is the range of the input elements.

## 8. Citation
1. Cormen, Thomas H., et al. Introduction to Algorithms. Mit Press, 2009.
2. “Radix Sort Algorithm in Data Structure: Overview, Time Complexity & More | Simplilearn,” Simplilearn.com. [Online]Available: https://www.simplilearn.com/. (accessed Apr. 03, 2023).
3. “Radix Sort Revisited,” codercorner.com. [Online]. Available: http://codercorner.com/RadixSortRevisited.htm (accessed Apr. 03, 2023).
4. “Learn the Radix Sort Algorithm.” Radix Sort Algorithm, Examples & Problems. [Online]. Available:https://www.interviewkickstart.com/learn/radix-sort-algorithm. (accessed Apr. 03, 2023)
5. “Radix Sort.” GeeksforGeeks. [Online]. Available: https://www.geeksforgeeks.org/radix-sort/. (accessed Apr. 01, 2023)
‌6. “Radix Sort - Programiz.” [Online]. Available: https://www.programiz.com/dsa/radix-sort. (accessed Apr. 01, 2023)
7. “Python Program for Radix Sort - GeeksforGeeks.” [Online]. Available: https://www.geeksforgeeks.org/python-program-for-radix-sort/. (accessed Apr. 01, 2023).
8. “Radix Sort in Python | Examples | Educba.” [Online]. Available: https://www.educba.com/radix-sort-in-python/. (accessed Apr. 01, 2023).
9. “Pushing Radix Sort and Python to its limits - Stack Overflow.” [Online]. Available: https://stackoverflow.com/questions/20207791/pushing-radix-sort-and-python-to-its-limits. (accessed Apr. 01, 2023).

## 9. Contributing

If you encounter any issues or have any suggestions for improving the program, please submit an issue or pull request on the GitHub repository.

