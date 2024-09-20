'''
@Author: Prathamesh Deshpande
@Date:  2024-09-18
@Last Modified by: Prathamesh Deshpande
@Last Modified time: 2024-09-18
@Title : Python program to implement stack using Linked List.

'''

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.top = None

    def push(self,data):
        """
        Description:
            Insert a new element at the top of the stack.
        
        Parameters:
            - data: 
                The value to be inserted in the new node.
        
        Returns:
        -   None
        """
        new_node = Node(data)
        
        if self.top is None:  
            self.top = new_node

        else:
            temp = self.top
            self.top = new_node
            self.top.next = temp

    def pop(self):
        """
        Description:
            Delete a top element from the stack.
        
        Parameters:
            None
        
        Returns:
        -   None
        """
        if self.top is None:
            return "Stack is empty can't delete the element"

        elif self.top.next is None:
            deleted_element = self.top.data
            self.top = None
            return deleted_element

        else:
            deleted_element = self.top.data
            self.top = self.top.next
            return deleted_element
        
    def peek(self):
        """
        Description:
            Returns the element at the top of the stack without deleting it.
        
        Parameters:
            None
        
        Returns:
            Returns the element at the top of the stack without deleting it.
        """
        if self.top is None:
            return "Stack is empty!"
        
        else:
            return self.top.data

    def traverse_stack(self):
        """
        Description:
            Print all elements in the stack.

        Parameters:
            None
        
        Returns:
        -   None
        """
        if self.top is None:
            print("Stack is empty")

        else:
            temp = self.top
            while(temp is not None):
                print(temp.data)
                temp = temp.next


def main():
    s = Stack()

    print("Enter 1 to insert the element in stack")
    print("Enter 2 to traverse the stack")
    print("Enter 3 to delete the element from stack")
    print("Enter 4 to find the peek element from stack")
    print("Enter 5 to Exit") 

    while(True):
        choice = int(input("Enter your choice : "))

        match choice:
            case 1:
                element = int(input("Enter an element to insert :\n"))
                s.push(element)

            case 2:
                s.traverse_stack()

            case 3:
                print(f"The deleted elemet is : {s.pop()}")

            case 4:
                print(f"The element at the top of the stack is : {s.peek()}")

            case 5:
                break
        
if __name__ == "__main__":
    main()
