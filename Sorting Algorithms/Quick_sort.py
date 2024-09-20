'''
@Author: Prathamesh Deshpande
@Date:  2024-09-19
@Last Modified by: Prathamesh Deshpande
@Last Modified time: 2024-09-19
@Title : Python program to implement Quick Sort.

'''

def quick_sort(arr):
    """
    Description:
        Perform Quick Sort on a list of elements.
    
    Parameters:
        - arr: 
            A list of numerical elements to be sorted.
    
    Returns:
    -   A sorted list of elements.

    """
    if len(arr) <= 1:
        return arr
    
    else:
        pivot = arr[len(arr) // 2]

        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]

        return quick_sort(less) + equal + quick_sort(greater)


def main():
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original array :", arr)
    sorted_arr = quick_sort(arr)
    print("Sorted array :", sorted_arr)


if __name__ == "__main__":
    main()
