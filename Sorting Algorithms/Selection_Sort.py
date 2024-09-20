'''
@Author: Prathamesh Deshpande
@Date:  2024-09-18
@Last Modified by: Prathamesh Deshpande
@Last Modified time: 2024-09-18
@Title : Python program to implement selection Sort.

'''

def selection_sort(arr):
    """
    Description:
        Perform Selection Sort on a list of elements.
    
    Parameters:
        - arr: 
            A list of numerical elements to be sorted.
    
    Returns:
    -   A sorted list of elements.

    """
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i] > arr[j]):
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp

    return arr


def main():
    sample_list = [7,20,56,5,2,40]
    print(f"The list before sorting is : {sample_list}")

    print(f"The list after sorting is : {selection_sort(sample_list)}")


if __name__ == "__main__":
    main()