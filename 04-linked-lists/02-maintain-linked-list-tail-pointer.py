class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class SinglyLinkedList:
	def __init__(self):
		#self.head = None
		#self.tail = None
		tail = Node(2)
		self.head = Node(1, tail)
		self.tail = self.head.next

	def delete(self, elem):
		if not self.head:
			return false
		elif self.head == elem:
			if not self.head.next:
				self.head = None
				return True
			else:
				self.head = self.head.next
				return True
		else:
			prev = self.head
			if not prev.next:
				return False
			elif prev.next != elem:
				while prev.next:
					prev = prev.next
					if not prev.next:
						return False
					elif prev.next == elem:
						break
			if prev.next.next:
				prev.next = prev.next.next
			else:
				prev.next = None
				self.tail = prev
			return True

	def insert_after(self, elem, data):
		if not isinstance(data, int):
			return False
		elif not elem:
			self.head = Node(data, self.head)
			if self.head.next and not self.head.next.next:
				self.tail = self.head.next
			return True
		elif not self.head:
			return False
		elif self.head == elem:
			if not self.head.next:
				self.head.next = Node(data)
				self.tail = self.head.next
				return True
			else:
				next = self.head.next
				self.head.next = Node(data, next)
				return True
		else:
			prev = self.head
			if not prev.next:
				return False
			elif prev.next != elem:
				while prev.next:
					prev = prev.next
					if not prev.next:
						return False
					elif prev.next == elem:
						break
				next = prev.next.next
				prev.next.next = Node(data, next)
				if not next:
					self.tail = prev.next.next
				return True

s_l_l = SinglyLinkedList()
print(s_l_l.delete(s_l_l.tail))
print(s_l_l.insert_after(s_l_l.head, 2))

print(s_l_l.insert_after(None, 0))

print(s_l_l.head.data)
print(s_l_l.head.next.data)
print(s_l_l.tail.data)
