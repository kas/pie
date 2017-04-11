class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class SinglyLinkedList:
	def __init__(self):
		next = Node(2)
		self.head = Node(1, next)

def remove_head(head):
	if head:
		next = head.next
		del head
		head = next

# this code does not work in python3 :(

