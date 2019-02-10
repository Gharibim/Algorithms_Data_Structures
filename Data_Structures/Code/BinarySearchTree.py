'''
Binary Search Tree implementation. Each function has 2 version. First the simple
function call that the user will use to call a function. Second, a recursive call
the will be called internally. If a function name starts with '_' it means this 
function suppose to be a private one. So do not call it from the main. 
'''

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.parent = None  # Extra, you need it only if you want (delete node) function

class BinaryTree:
	def __init__(self):
		self.root = None

	# Recursive function to add a node contains the value 'data' 
	def _addNode(self, root, data):
		if data < root.data:
			if root.left == None:
				root.left = Node(data)
				root.left.parent = root
			else:
				self._addNode(root.left, data)
		elif data > root.data:
			if root.right == None:
				root.right = Node(data)
				root.right.parent = root
			else:
				self._addNode(root.right, data)
		else:
			if root.left == None:
				root.left = Node(data)
				root.left.parent = root
			else:
				self._addNode(root.left, data)

	# add a node function 
	def addNode(self, data):
		if self.root == None:
			self.root = Node(data)
		else:
			self._addNode(self.root, data)


	# Recursive function to print the BST
	def _printTree(self, root):
		if root:
			self._printTree(root.left)
			print(root.data, end='  ')
			self._printTree(root.right)

	# print the BST function
	def printTree(self):
		if self.root == None:
			print("NoneThing")
		else:
			self._printTree(self.root)
			print()


	# Recursive function to search 
	def _search(self, root, data):
		if data == root.data:
			return True
		elif data < root.data and root.left:
			return self._search(root.left, data)
		elif data > root.data and root.right:
			return self._search(root.right, data)
		else:
			return False

	# the search function 
	def search(self, data):
		if self.root == None:
			return None
		else:
			return self._search(self.root, data)


	# Recursive function to return the height of a current node
	# the function accepts current node and its height
	def _tree_Height(self, root, cur_height):
		if root == None or (root.left == None and root.right == None):
			return cur_height
		return max(self._tree_Height(root.left, cur_height+1), self._tree_Height(root.right, cur_height +1))

	# a function to return the tree hieght
	def tree_Height(self):
		if self.root == None:
			return 0
		else:
			return self._tree_Height(self.root, 0)


	# Recursive function to return a node
	def _returnNode(self, root, data):
		if data == root.data:
			return root
		elif data < root.data and root.left:
			return self._returnNode(root.left, data)
		elif data > root.data and root.right:
			return self._returnNode(root.right, data)
		else:
			return None

	# return function, that return the node itself
	def returnNode(self, data):
		if self.root == None:
			return None
		else:
			return self._returnNode(self.root, data)


	# a fnction to return a node hegith, the recursive part of this function is
	# exactly the same as '_tree_Heigt' so I did not repeat the function
	def node_Height(self, data):
		node = self.returnNode(data)
		if node != None:
			return self._tree_Height(node, 0)
		else:
			return 0


	# Delete a node. Two types of this function. First: the function that accepts
	# a value. User will call this function mostly
	def delalue(self, data):
		self.delNode(self.returnNode(data))


	# Second verion that accepts a node, rather than a node value. This function 
	# will be called internally.
	def delNode(self, node):

		# This function will be used only here to return the number of child nodes
		def num_children(node):
			num = 0
			if node.left:
				num += 1
			if node.right:
				num += 1
			return num

		# return the successor of node (which is the first node before or after)
		# Since we are using preorder traversal then will return its left child.
		# if no left child then return check right child after their root
		def return_scuccessor(node):
			if node.left:
				return node.left
			cur = node
			while cur.parent and cur.parent.right == cur:
				cur = cur.parent
			if cur.parent == None:
				return None
			return cur.parent.right

		children = num_children(node)
		parent_node = node.parent

		# 3 cases to delete a node. If the node has no children then just change pointers
		if children == 0:
			if parent_node.left == node:
				parent_node.left = None
			else:
				parent_node.right = None

		# case 2 if only 1 child
		if children == 1:
			if node.left:
				child = node.left
			else:
				child = node.right

			if parent_node.left == node:
				parent_node.left = child
			else:
				parent_node.right = child
			
			child.parent = parent_node

		# case 3 if there are 2 children
		if children == 2:
			successor = return_scuccessor(node)
			node.data = successor.data
			self.delNode(successor)

			