class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class Single:
	def __init__(self):
		self.head = None

	# Add at the beginning of the list
	def addHead(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	# Print the list
	def printList(self):
		cur = self.head
		while cur:
			print(cur.val, end = "  ")
			cur = cur.next
		print()

	# Add the value 'toadd' after the value 'data'
	def addAfter(self, toadd, data):
		cur = self.head
		new_node = Node(toadd)
		while cur:
			if cur.val == data:
				new_node.next = cur.next
				cur.next = new_node
			cur = cur.next

	# Add the value 'toadd' before the value 'data'
	def addBefore(self, toadd, data):
		cur = self.head
		if self.head.val == data:
			self.addHead(toadd)
			return
		new_node = Node(toadd)
		while cur:
			if cur.next and cur.next.val == data:
				new_node.next = cur.next
				cur.next = new_node
				return
			cur = cur.next

	# Add at the end of the list
	def addEnd(self, data):
		if self.head == None:
			new_node = Node(data)
			self.head = new_node
			return
		cur = self.head
		while cur.next:
			cur = cur.next
		new_node = Node(data)
		cur.next = new_node

	# Delete a node
	def delNode(self, data):
		cur = self.head
		if self.head.val == data:
			self.head = self.head.next
			return
		while cur:
			while cur.next and cur.next.val == data:
				cur.next = cur.next.next
				return
			cur = cur.next

	# reverse the linked list completely
	def reverseList(self):
		cur = self.head
		prev = None
		while cur.next:
			Next = cur.next
			cur.next = prev
			prev = cur
			cur = Next
		cur.next = prev
		self.head = cur


	# Reverse the first n'th number of nodes based on the passed value 'num'
	# Input: [1,2,3,4,5,6,7], num=3, Ouput: [3,2,1,4,5,6,7]
	def reverseListNum(self, num):
		cur = self.head
		prev = None
		count = 0
		while cur.next:
			Next = cur.next
			cur.next = prev
			prev = cur
			cur = Next
			count += 1
			if count == num:
				break
		self.head.next = cur
		self.head = prev

	#Reverse a the first k numbers, the call the same function till the end of the list
	# Input: [1,2,3,4,5,6,7,8,9], k=3, Output: [3,2,1,6,5,4,9,8,7]
	def reverse(self, head, k): 
		cur = head
		prev = None
		Next = None
		count = 0
		while cur and count < k:
			Next = cur.next
			cur.next = prev
			prev = cur
			cur = Next
			count += 1
		if Next != None: 
			head.next = self.reverse(Next, k)
		return prev


	# Make a circle linked list at the node 'cir'
	def makeCir(self, cir):
		cur = self.head
		while cur.next:
			cur = cur.next
		cur.next = cir

	# Detect the circle and return the node
	def detectCir(self):
		slow = fast = self.head
		while fast.next.next:
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				return slow
		return None

	# Delete the circle
	def delCir(self, slow):
		start = self.head
		while True:
			start = start.next
			if slow.next == start:
				slow.next = None
				break
			else:
				slow = slow.next

	# Add two lists. A: [1,2,3], B: [4,5,6]. Output: [5,7,9]
	def addTwoLeftRight(self, A, B):
		carry = 0
		l1 = A
		l2 = B
		root = n = Single()

		while l1 or l2 or carry:
			v1 = v2 = 0
			if l1:
				v1 = l1.val
				l1 = l1.next
			if l2:
				v2 = l2.val
				l2 = l2.next
			carry, val = divmod(v1 + v2 + carry, 10)
			n.addEnd(val)
	
		return root


	# Merge two lists. A single node from each	
	# A: [1,2,3], B: [4,5,6]. Output: [1,4,2,5,3,6]
	def merge(self, root):
		cur = self.head
		while cur and root:
			next_cur = cur.next
			next_root = root.next

			cur.next = root
			root.next = next_cur

			cur = next_cur
			root = next_root
		
		self.printList()

		


# ============ Function outside the Linked List class ============


# a function to delete the duplicates. O(n). Iterate once through the list
def delDup(A):
	head = A
	while A:
		while A.next and A.data == A.next.data:
			A.next = A.next.next
		A = A.next
	return head

def printN(A):
	head = A
	while A:
		print(A.data)
		A = A.next


# a function to delete n'th element from the end of a linked list
# Given the list 3 -> 6 -> 8 -> 1 -> 9 -> 3
# and a given number, say 2. Then the second number from the end which is 9
# should be deleted. Otherwise, delete the head
def removeN(A, B):
	if A == None or B < 1:
		return A
	tail = A
	for i in range(B):
		if tail.next == None:
			return A.next
		tail = tail.next
	prev = None
	cur = A
	while tail:
		tail = tail.next
		prev = cur
		cur = cur.next
	prev.next = cur.next
	return A




