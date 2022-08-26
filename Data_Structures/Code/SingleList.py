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
		if cur.val == data:
			self.head = self.head.next
			cur.next = None
			return
		while cur.next:
			if cur.next.val == data:
				temp = cur.next
				cur.next = cur.next.next
				temp.next = None
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


# =============================================

class Node:
	def __init__(self, data):
		self.next = None
		self.data = data

class LinkedList:
	def __init__(self):
		self.head = None

	def addHead(self, data):
		if not self.head:
			self.head = Node(data)
			return
		temp = Node(data)
		temp.next = self.head
		self.head = temp

	def printList(self):
		if not self.head:
			print("nothing to print")
			return
		cur = self.head
		while cur:
			print(cur.data, end=' ')
			cur = cur.next
		print()

	def addAfter(self, aft, data):
		if not self.head:
			self.addHead(data)
			return
		cur = self.head
		while cur:
			if cur.data == aft:
				temp = Node(data)
				temp.next = cur.next
				cur.next = temp
				return
			cur = cur.next

	def addBefore(self, bfr, data):
		if not self.head:
			self.addHead(data)
			return
		if self.head.data == bfr:
			self.addHead(data)
			return
		cur = self.head
		while cur.next:
			if cur.next.data == bfr:
				temp = Node(data)
				temp.next = cur.next
				cur.next = temp
				return
			cur = cur.next

	def delNode(self, data):
		if not self.head:
			return
		if self.head.data == data:
			self.head = self.head.next
			return
		cur = self.head
		while cur.next:
			if cur.next.data == data:
				cur.next = cur.next.next
				return
			cur = cur.next

	def delDuplicates(self):
		if not self.head:
			return
		cur = self.head
		while cur:
			if cur.next and cur.data == cur.next.data:
				cur.next = cur.next.next
				continue
			cur = cur.next

	def addEnd(self, data):
		if not self.head:
			self.addHead(data)
			return
		cur = self.head
		while cur.next:
			cur = cur.next
		temp = Node(data)
		cur.next = temp

	def reverseList(self):
		if not self.head:
			return
		prev = None
		cur = self.head
		while cur:
			Next = cur.next
			cur.next = prev
			prev = cur
			cur = Next
		self.head = prev


	def reverseNumber(self, num):
		if not self.head:
			return
		prev = None
		cur = self.head
		count = 0
		Next = None
		while cur:
			if not (count < num):
				break
			Next = cur.next
			cur.next = prev
			prev = cur
			cur = Next
			count += 1
		self.head.next = Next
		self.head = prev

	def reversely(self, head, num):
		if not head:
			return
		cur = head
		prev = None
		count = 0
		Next = None
		while cur:
			if not (count < num):
				break
			Next = cur.next
			cur.next = prev
			prev = cur
			cur = Next
			count += 1
		head.next = self.reversely(Next, num)
		head = prev
		return head

	def makeCir(self, data):
		if not self.head:
			return
		ptr = None
		cur = self.head
		while cur.next:
			if cur.data == data:
				ptr = cur
			cur = cur.next
		cur.next = ptr

	def detectCir(self):
		if not self.head:
			return
		slow = self.head
		fast = self.head
		while fast.next.next:
			if fast == slow:
				return slow
			slow = slow.next
			fast = fast.next.next
		return False

	def delCir(self, cir_ptr):
		if not self.head:
			return
		cur = self.head
		while True:
			cur = cur.next
			if cir_ptr.next == cur:
				cir_ptr.next = None
				return
			else:
				cir_ptr = cir_ptr.next

	def simpleAdd(self, head2):
		if not self.head and not head2:
			return
		if not self.head:
			return head2
		if not head2:
			return self.head

		result = LinkedList()
		h1 = self.head
		h2 = head2.head
		while h1 or h2:
			temp_sum = 0
			if h1:
				temp_sum += h1.data
				h1 = h1.next
			if h2:
				temp_sum += h2.data
				h2 = h2.next
			result.addEnd(temp_sum)
		return result

	def addHard(self, head2):
		if not self.head and not head2:
			return
		if not self.head:
			return head2
		if not head2:
			return self.head
		h1 = self.head
		h2 = head2.head
		result = LinkedList()
		carry = 0
		while h1 or h2 or carry:
			total_sum = carry
			if h1:
				total_sum += h1.data
				h1 = h1.next
			if h2:
				total_sum += h2.data
				h2 = h2.next
			carry, res = divmod(total_sum, 10)
			result.addEnd(res)
		return result

	def mergeListsInPlace(self, head2):
		if not self.head and not head2:
			return
		if not self.head:
			return head2
		if not head2:
			return self.head
		h1 = self.head
		h2 = head2.head
		h1_next = None
		h2_next = None
		while h1.next and h2.next:
			h1_next = h1.next
			h1.next = h2
			h1 = h1_next

			h2_next = h2.next
			h2.next = h1
			h2 = h2_next
		if h1.next:
			h2.next = h1
		if h2.next:
			h1.next = h2

	def mergeLists(self, head2):
		if not self.head and not head2:
			return
		if not self.head:
			return head2
		if not head2:
			return self.head
		result = LinkedList()
		result.addHead(0)
		cur = result.head
		h1 = self.head
		h2 = head2.head
		h1_next = None
		h2_next = None
		while h1.next and h2.next:
			h1_next = h1.next
			h2_next = h2.next
			cur.next = h1
			cur = cur.next
			cur.next = h2
			cur = cur.next
			h1 = h1_next
			h2 = h2_next
		if h1:
			cur.next = h1
			cur = cur.next
		if h2:
			cur.next = h2
		return result

	def mergeTwoSortedLists(self, head2):
		if not self.head and not head2:
			return
		if not self.head:
			return head2
		if not head2:
			return self.head
		result = LinkedList()
		result.addHead(0)
		cur = result.head
		h1 = self.head
		h2 = head2.head
		h1_next = None
		h2_next = None
		while h1 and h2:
			h1_next = h1.next
			h2_next = h2.next
			if h1.data <= h2.data:
				cur.next = h1
				cur = cur.next
				h1 = h1_next
			else:
				cur.next = h2
				cur = cur.next
				h2 = h2_next

		if h1:
			cur.next = h1
		if h2:
			cur.next = h2
		return result



