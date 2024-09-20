'''
@Author: Prathamesh Deshpande
@Date:  2024-09-18
@Last Modified by: Prathamesh Deshpande
@Last Modified time: 2024-09-18
@Title : Python program to implement Linked List.

'''
class Node:
    
    def __init__(self, data) -> None:
        """
        Description:
            A method to initialize the data.
    
        Parameters:
            - data: 
                The value of the node.
    
        Return:
            None 
    """
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self) -> None:
        self.head = None

    def insert_at_end(self, data):
        """
        Description:
            Insert a new node at the end of the linked list.
        
        Parameters:
            - data: 
                The value to be inserted in the new node.
        
        Returns:
        -   None
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node


    def insert_at_beginning(self, data):
        """
        Description:
            Insert a new node at the beginning of the linked list.
        
        Parameters:
            - data: 
                The value to be inserted in the new node.
        
        Returns:
        -   None
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node


    def insert_at_middle(self, data_to_insert, item):
        """
        Description:
            Insert a new node after a specified node in the linked list.
        
        Parameters:
            - data_to_insert: 
                The value to be inserted in the new node.

            - item: 
                The value of the node after which the new node will be inserted.
        
        Returns:
        -   None
        """
        new_node = Node(data_to_insert)
        temp = self.head
        while temp is not None:
            if temp.data == item:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        print("The given element does not exist")


    def delete_from_beginning(self):
        """
        Description:
            Delete the node at the beginning of the linked list.

        Parameters:
            None
        
        Returns:
        -   The value of the deleted node, or a message if the list is empty.
        """
        if self.head is None:
            return "Linked list is empty, can't delete the element"
        
        else:
            deleted_element = self.head.data
            self.head = self.head.next
            return deleted_element

    def delete_from_end(self):
        """
        Description:
            Delete the node at the end of the linked list.

        Parameters:
            None
        
        Returns:
        -   The value of the deleted node, or a message if the list is empty.
        """

        if self.head is None:
            return "Linked list is empty, can't delete the element"
        
        elif self.head.next is None:
            deleted_element = self.head.data
            self.head = None
            return deleted_element
        
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            deleted_element = temp.next.data
            temp.next = None

            return deleted_element
        

    def delete_element(self, element):
        """
        Description:
            Delete a specific element from the linked list.
        
        Parameters:
            - element: 
                The value of the node to be deleted.
        
        Returns:
        -   None
        """
         
        if self.head is None:
            print("Linked list is empty, can't delete the element")
            return
             
        if self.head.data == element:
            self.head = self.head.next
            return

        temp = self.head
        found = False   

        while temp is not None and temp.next is not None:
            if temp.next.data == element:
                temp.next = temp.next.next
                found = True
            else:
                temp = temp.next

        if not found:
            print(f"The given element {element} does not exist")


    def traverse_list(self):
        """
        Description:
            Print all elements in the linked list.

        Parameters:
            None
        
        Returns:
        -   None
        """
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next


def main():
    L = LinkedList()

    print("Enter 1 to insert at the beginning")
    print("Enter 2 to insert at the end")
    print("Enter 3 to insert after a particular element")
    print("Enter 4 to traverse the linked list")
    print("Enter 5 to delete from the beginning")
    print("Enter 6 to delete from the end")
    print("Enter 7 to delete a particular element")
    print("Enter 8 to Exit")

    while True:
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                element = int(input("Enter an element to insert:\n"))
                L.insert_at_beginning(element)

            case 2:
                element = int(input("Enter an element to insert:\n"))
                L.insert_at_end(element)

            case 3:
                element = int(input("Enter an element to insert:\n"))
                ele = int(input("Enter an element after which you want to insert an element:\n"))
                L.insert_at_middle(element, ele)

            case 4:
                L.traverse_list()

            case 5:
                print(f"The deleted element is: {L.delete_from_beginning()}")

            case 6:
                print(f"The deleted element is: {L.delete_from_end()}")

            case 7:
                element = int(input("Enter an element to delete:\n"))
                L.delete_element(element)

            case 8:
                break


if __name__ == "__main__":
    main()
