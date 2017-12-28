__author__ = "Kartik Kannapur"

# #Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class LinkedList:
    def __init__(self):
        self.head = None

    def print_elements(self):
    	current = self.head

    	while(current):
    		print(current.data)
    		current = current.next

    def make_number(self):
        num = ""
        current = self.head

        while(current):
            # print(current.data)
            num += str(current.data)
            current = current.next

        return(int(num))

if __name__ == "__main__":
    l1 = LinkedList()
    l2 = LinkedList()

    N11 = Node(9)
    N12 = Node(8)
    # N13 = Node(3)

    N21 = Node(1)
    # N22 = Node(6)
    # N23 = Node(4)

    l1.head = N11
    N11.next = N12
    # N12.next = N13

    l2.head = N21
    # N21.next = N22
    # N22.next = N23

    ##############

    val1 = l1.make_number()
    val2 = l2.make_number()
    print(val1, val2)
    print(val1 + val2)