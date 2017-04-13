class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class SinglyLinkedList:
	def __init__(self):
		self.head = None

	def prepend(self, data):
		self.head = Node(data, self.head)

	def append(self, data):
		if not self.head:
			self.head = Node(data)
		else:
			curr_node = self.head
			while curr_node.next:
				curr_node = curr_node.next
			curr_node.next = Node(data, None)

	def insert(self, data, pos):
		c = 0
		prev = self.head
		while prev.next:
			prev = prev.next
			c += 1
			if c == (pos - 1):
				break
			if prev.next is None:
				raise KeyError(pos)
			prev.next = Node(data, prev.next)

	def delete(self, pos):
		if not self.head:
			raise KeyError(pos)
		if pos == 0:
			if not self.head.next:
				self.head = None
			else:
				self.head = self.head.next
		else:
			c = 0
			prev = self.head
			if c != (pos - 1):
				while prev.next:
					prev = prev.next
					c += 1
					if c == (pos - 1):
						break
			if prev.next is None:
				raise KeyError(pos)
			prev.next = prev.next.next

	def get(self, pos):
		if not self.head:
			raise KeyError(pos)
		c = 0
		curr = self.head
		if c != pos:
			while curr.next:
				curr = curr.next
				c += 1
				if c == pos:
					break
		if c != pos:
			raise KeyError(pos)
		return curr.data


class Stack:
	def __init__(self):
		self.s_l_l = SinglyLinkedList()

	def push(self, data):
		self.s_l_l.prepend(data)

	def pop(self):
		data = self.s_l_l.get(0)
		self.s_l_l.delete(0)
		return data

stack = Stack()
stack.push('Hello World!')
print(stack.pop())
