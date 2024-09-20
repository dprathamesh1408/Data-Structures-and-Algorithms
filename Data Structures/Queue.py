'''
@Author: Prathamesh Deshpande
@Date:  2024-09-18
@Last Modified by: Prathamesh Deshpande
@Last Modified time: 2024-09-18
@Title : Python program to implement queue using Linked List.

'''

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None

    def enqueue(self,data):
        """
        Description:
            Insert a new element at the beginning of the queue.
        
        Parameters:
            - data: 
                The value to be inserted in the new node.
        
        Returns:
        -   None
        """
        new_node = Node(data)
        if self.front is None and self.rear is None:  
            self.front = self.rear = new_node

        else:
            while self.rear.next is not None:
                self.rear = self.rear.next

            self.rear.next =  new_node

    def dequeue(self):
        """
        Description:
            Delete a front element from the queue.
        
        Parameters:
            None
        
        Returns:
        -   None
        """
        if self.front is None:
            return "Queue is empty can't delete the element"
        
        else:
            deleted_element = self.front.data
            self.front = self.front.next

            return deleted_element
        
    def front_element(self):
        """
        Description:
            Returns the element at the front of the queue without deleting it.
        
        Parameters:
            None
        
        Returns:
            Returns the element at the front of the queue without deleting it.
        """
        if self.front is None:
            return "Queue is empty"
        
        else:
            return self.front.data
           
    def traverse_queue(self):
        """
        Description:
            Print all elements in the queue.

        Parameters:
            None
        
        Returns:
        -   None
        """
        if self.front is None:
            print("Queue is empty")
        
        else:
            temp = self.front
            while(temp!= None):
                print(temp.data)
                temp = temp.next

def main():
    q = Queue()

    print("Enter 1 to insert the element in Queue")
    print("Enter 2 to traverse the Queue")
    print("Enter 3 to delete the element from Queue")
    print("Enter 4 to find the front element from the queue")
    print("Enter 5 to Exit") 

    while(True):
        choice = int(input("Enter your choice : "))

        match choice:
            case 1:
                element = int(input("Enter an element to insert :\n"))
                q.enqueue(element)

            case 2:
                q.traverse_queue()

            case 3:
                print(f"The deleted elemet is : {q.dequeue()}")

            case 4:
                print(f"The element at the front of the queue is : {q.front_element()}")

            case 5:
                break
        
if __name__ == "__main__":
    main()
