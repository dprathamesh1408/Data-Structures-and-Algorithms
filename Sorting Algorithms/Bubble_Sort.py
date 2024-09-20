'''
@Author: Prathamesh Deshpande
@Date:  2024-09-18
@Last Modified by: Prathamesh Deshpande
@Last Modified time: 2024-09-18
@Title : Python program to implement Bubble Sort.

'''

def bubble_sort(arr):
    """
    Description:
        Perform Bubble Sort to sort a list of elements in ascending order.
    
    Parameters:
        - arr: 
            A list of numerical elements to be sorted.
    
    Returns:
    -   The sorted list of elements.
    """

    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr


def main():

    sample_list = [7, 20, 56, 5, 2, 40]
    print(f"The list before sorting is: {sample_list}")
    print(f"The list after sorting is: {bubble_sort(sample_list)}")


if __name__ == "__main__":
    main()
