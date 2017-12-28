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

    def push(self, data):
    	new_node = Node(data)
    	new_node.next = self.head
    	self.head = new_node


    def insert_after(self, prev_node, data):
    	new_node = Node(data)

    	new_node.next = prev_node.next
    	prev_node.next = new_node


    def append(self, data):
    	new_node = Node(data)

    	if self.head == None:
    		self.head = new_node

    	last = self.head
    	while(last.next):
    		last = last.next

    	last.next = new_node


if __name__ == "__main__":
	# #Create a LinkedList
	ll = LinkedList()
	
	# #Create 3 Nodes
	node_first = Node(42)
	node_second = Node(5)
	node_third = Node(21)

	# #Link the 3 Nodes
	ll.head = node_first
	node_first.next = node_second
	node_second.next = node_third

	# #Print the elements in the LinkedList
	# ll.print_elements()

	# ll.push(1000)
	# ll.insert_after(node_second, 500)
	ll.append(272)
	ll.print_elements()


