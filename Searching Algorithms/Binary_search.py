'''
@Author: Prathamesh Deshpande
@Date:  2024-09-18
@Last Modified by: Prathamesh Deshpande
@Last Modified time: 2024-09-18
@Title : Python program to implement Binary search.

'''

def binary_search(arr, target):
    """
    Description:
        Perform binary search to find the target element in a sorted list.
    
    Parameters:
        - arr: 
            A list of sorted numerical elements.

        - target: 
            The element to search for in the list.
    
    Returns:
    -   The index of the target element if found, otherwise -1.
    """

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return -1


def main():
     
    sample_list = [10, 20, 30, 40, 50, 60]
    target = int(input("Enter an element to search: "))

    index = binary_search(sample_list, target)
    
    if index == -1:
        print(f"The element {target} is not present in the given list.")
        
    else:
        print(f"The element {target} is present at index {index}")


if __name__ == "__main__":
    main()
