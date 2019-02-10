class Node:

	number = 0

	def __init__(self, data):
		self.data = data
		self.ptr = None
		Node.number += 1

	def setData(self, value):
		self.data = value

	def setPtr(self, pointer):
		self.ptr = pointer

	def getData(self):
		return self.data

	def getPtr(self):
		return self.ptr


class List():


	"""docstring for List"""
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def appTop(self, item):
		temp = Node(item)
		temp.setPtr(self.head)
		self.head = temp


	def addAfter(self, item, value):
		cur = self.head
		while cur:
			if cur.getData() == item:
				temp = Node(value)
				temp.setPtr(cur.getPtr())
				cur.setPtr(temp)
			cur = cur.getPtr()

	def addBefore(self, item, value):
		cur = self.head
		pre = None
		while cur:
			if cur.getData() == item:
				temp = Node(value)
				temp.setPtr(pre.getPtr())
				pre.setPtr(temp)
			pre = cur
			cur = cur.getPtr()


	def size(self):
		return Node.number

	def remove(self,value):
		prev = None
		curr = self.head
		while curr:
			if curr.getData() == value:
				if prev:
					prev.setPtr(curr.getPtr())
				else:
					self.head = curr.getPtr()
				return True
			prev = curr
			curr = curr.getPtr()


	def search(self, item):
		cur = self.head
		while cur != None:
			if cur.getData() == item:
				print("Found it")
				return True
			else:
				cur = cur.getPtr()
		print("Not in the list")


	def display(self):
		cur = self.head
		while cur:
			print(cur.getData())
			cur = cur.getPtr()

