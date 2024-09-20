'''
@Author: Prathamesh Deshpande
@Date:  2024-09-19
@Last Modified by: Prathamesh Deshpande
@Last Modified time: 2024-09-19
@Title : Python program to implement Merge Sort.

'''

def merge_sort(arr):
    """
    Description:
        Perform Merge Sort on a list of elements.
    
    Parameters:
        - arr: 
            A list of numerical elements to be sorted.
    
    Returns:
    -   A sorted list of elements.

    """
    if len(arr) > 1:
        mid = len(arr) // 2
        
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


def main():
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original array :", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted array :", sorted_arr)


if __name__ == "__main__":
    main()
