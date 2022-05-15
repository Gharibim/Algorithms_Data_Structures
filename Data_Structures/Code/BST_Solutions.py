class Node:
	'''Node class useful to construct binary tree '''
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

# ========================================================

'''Return the minimum depth for a Binary Search Tree (BST)
The solution is to traverse the BST using Breadth First Search (BFS)
algorithm with a queue

Input: 

          10 
       /     \  
      2       10 
    /  \        \ 
   20   1       -25 
   			   /   \
   		      3     4

Output: 
2
'''

def minDepth(root):
	if root == None:
		return 0

	queue = [{'node': root, 'depth':0}]
	while queue:
		vertex = queue.pop(0)
		node = vertex['node']
		depth = vertex['depth']

		if node.left == None and node.right == None:
			return depth

		if node.left:
			queue.append({'node': node.left, 'depth': depth+1})
		if node.right:
			queue.append({'node': node.right, 'depth': depth+1})


# To test the code, uncomment the following:

# root = Node(1) 
# root.left = Node(2) 
# root.right = Node(3) 
# root.left.left = Node(4) 
# root.left.right = Node(5) 
# root.right.left = Node(10)
# print (minDepth(root))





# ===================================================================
'''Return the maximum sum in a BST. The maximum sum is the longest sequence
of nodes that maximize the total. To solve this qestion we look into the maximum
between 4 different combinations: 1) The root itself. 2) The root + its left child
3) The root + its right child. 4) left child + the root + the right child

Input: 

          10 
       /     \  
      2       10 
    /  \        \ 
   20   1       -25 
   			   /   \
   		      3     4

Output: 
42
Since the maximum path is 20, 2, 10, 10
'''

result = float("-inf")

def _maxSum(root):
	global result
	if root == None:
		return 0

	leftSum = _maxSum(root.left)
	rightSum = _maxSum(root.right)

	signleSum = max(max(leftSum, rightSum) + root.data, root.data)
	topSum = max(signleSum, leftSum + root.data + rightSum)
	result = max(result, topSum)

	return signleSum

def maxSum(root):
	global result
	_maxSum(root)
	print(result)


# root = Node(10) 
# root.left = Node(2) 
# root.right   = Node(10); 
# root.left.left  = Node(20); 
# root.left.right = Node(1); 
# root.right.right = Node(-25); 
# root.right.right.left   = Node(3); 
# root.right.right.right  = Node(4); 

# print ("Max path sum is " ,maxSum(root))



# ===================================================================
'''Given an array, return if this array represent the preorder traversal of a BST
[40 , 30 , 35 , 80 , 100] => True
[40 , 30 , 35 , 20 ,  80 , 100] => False
'''

INT_MIN = float("-inf")

def checkArray(arr):
	root = INT_MIN
	stack = []

	for value in arr:
		if value < root:
			return False

		while stack and stack[-1] < value:
			root = stack.pop()

		stack.append(value)
	return True

# pre1 = [40 , 30 , 35 , 80 , 100] 
# print (checkArray(pre1)) 
# pre2 = [40 , 30 , 35 , 20 ,  80 , 100] 
# print (checkArray(pre2))



# ===================================================================
''' Check if a given Binary Tree is a full BT or not

Input: 

         1 
       /    \  
      2      3 
     / \    / \ 
    4   5  6   7   
    	  

Output: 
True
'''
def checkTree(root):
	if root == None:
		return True

	if root.left == None and root.right == None:
		return True

	if root.left and root.right:
		return checkTree(root.left) and checkTree(root.right)

	return False


# root = Node(10); 
# root.left = Node(20); 
# root.right = Node(30); 
# root.left.right = Node(40); 
# root.left.left = Node(50); 
# root.right.left = Node(60); 
# root.right.right = Node(70); 
# root.left.left.left = Node(80); 
# root.left.left.right = Node(90); 
# root.left.right.left = Node(80); 
# root.left.right.right = Node(90); 
# root.right.left.left = Node(80); 
# root.right.left.right = Node(90); 
# root.right.right.left = Node(80); 
# root.right.right.right = Node(90); 
  
# print(checkTree(root))


# ===================================================================
'''Given a BT, we want to calculate the sum for each vertical level. To understand
vertical level, think about a BT that has been sliced into different columns.
Each column represents a vertical level. For example, level 0 represtens [1,5]
If we go right then add 1. Otherwise, reduce 1
level 1 contains [3, 8]. Level 2 has [6]. Level -1 has [2,7]

Input: 

         1 
       /    \  
      2      3 
            / \ 
           5   6   
    	  /	\
    	 7	 8

Output:
{0: 6, -1: 9, 1: 11, 2: 6}
'''

def _verticalSum(root, dict, dist):
	if root == None:
		return
	if dist in dict:
		dict[dist] += root.data
	else:
		dict[dist] = root.data
	_verticalSum(root.left, dict, dist-1)
	_verticalSum(root.right, dict, dist+1)

def verticalSum(root):
	dict = {}
	_verticalSum(root, dict, 0)
	print(dict)

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.right.left = Node(5)
# root.right.right = Node(6)
# root.right.left.left = Node(7)
# root.right.left.right = Node(8)

# print(verticalSum(root))


# ===================================================================
'''Given a BT, we want to calculate the sum for each horiental level.
In other words, we want the sum for each level in the BT (solution using BFS)

Input: 

         1 
       /    \  
      2      3 
            / \ 
           5   6   
    	  /	\
    	 7	 8

Output: 
{0: 1, 1: 5, 2: 11, 3: 15}
Contains each level and its sum
'''

def horizentalSum(root):
	if root == None:
		return 0
	dict = {}
	queue = [{'node': root, 'data': root.data, 'depth':0}]
	while queue:
		QItem = queue.pop(0)
		node = QItem['node']
		data = QItem['data']
		depth = QItem['depth']

		if depth in dict:
			dict[depth] += data
		else:
			dict[depth] = data

		if node.left:
			queue.append({'node': node.left, 'data': node.left.data, 'depth': depth+1})
		if node.right:
			queue.append({'node': node.right, 'data': node.right.data, 'depth': depth+1})

	print(dict)


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.right.left = Node(5)
# root.right.right = Node(6)
# root.right.left.left = Node(7)
# root.right.left.right = Node(8)

# horizentalSum(root)



# ===================================================================
'''Top level view of a BT is the nodes that you see when you look at a BT from top.
The idea is to start with numbering each vertical level. Vertical 0 contains [0,5]
Since we want top level view then we will print only 1. If we have any nodes in level 0,
then we will ignore them. 
If we go to right child we increase the level by 1. If we decide to go with left child,
then we reduce the level by 1, and so on ...

Input: 

         1 
       /    \  
      2      3 
            / \ 
           5   6   
    	  /	\
    	 7	 8
    	

Output: 
{0: 1, -1: 2, 1: 3, 2: 6}
level 0 contains 1, level -1 contains 2 and so on...
'''

def _topLevel(root, dict, dist):
	if root == None:
		return

	if dist not in dict:
		dict[dist] = root.data

	_topLevel(root.left, dict, dist-1)
	_topLevel(root.right, dict, dist+1)

def topLevel(root):
	dict = {}
	_topLevel(root, dict, 0)
	print(dict)


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.right.left = Node(5)
# root.right.right = Node(6)
# root.right.left.left = Node(7)
# root.right.left.right = Node(8)

# print(topLevel(root))



# ===================================================================
'''Bottom View of a BT is the nodes that you see when you look at a BT from bottom.

Input: 

         1 
       /    \  
      2      3 
            / \ 
           5   6   
    	  /	\
    	 7	 8
    	

Output: 
{0: 5, -1: 7, 1: 8, 2: 6}
The dictionary represents the node that represnts each vertical level.
level 0 has 2 node [1,5], bottom view outputs only 5 and so on
'''

def _bottomLevel(root, dict, dist):
	if root == None:
		return

	dict[dist] = root.data

	_bottomLevel(root.left, dict, dist-1)
	_bottomLevel(root.right, dict, dist+1)

def bottomLevel(root):
	dict = {}
	_bottomLevel(root, dict, 0)
	print(dict)


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.right.left = Node(5)
# root.right.right = Node(6)
# root.right.left.left = Node(7)
# root.right.left.right = Node(8)

# print(bottomLevel(root))



# ===================================================================
'''Right view of a BT is the nodes that you see when you look at a BT from the right
The solution uses a global variable 'maxLevel'. The solution could be done without
the global variable, by using a list[0]. Check left view of BT

Input: 

         1 
       /    \  
      2      3 
            / \ 
           5   6   
    	  /	\
    	 7	 8
    	

Output: 
1, 3, 6, 8
'''

maxLevel = 0

def _rightView(root, level):
	global maxLevel

	if root == None:
		return

	if maxLevel < level:
		print(root.data, end=' ')
		maxLevel = level

	_rightView(root.right, level+1)
	_rightView(root.left, level+1)



def rightView(root):
	_rightView(root, 1)

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.right.left = Node(5)
# root.right.right = Node(6)
# root.right.left.left = Node(7)
# root.right.left.right = Node(8)

# rightView(root)



# ===================================================================
'''Left view of BT is the nodes that you see when you look at a BT from the left
This solution same as right view but here I used a list[0] instead of the global var

Input: 

         1 
       /    \  
      2      3 
            / \ 
           5   6   
    	  /	\
    	 7	 8
    	

Output: 
1, 2, 5, 7
'''

def _leftLevel(root, maxLevel, level):
	if root == None:
		return
	if maxLevel[0] < level:
		print(root.data, end=' ')
		maxLevel[0] = level

	_leftLevel(root.left, maxLevel, level+1)
	_leftLevel(root.right, maxLevel, level+1)

def leftLevel(root):
	maxLevel = [0]
	_leftLevel(root, maxLevel, 1)

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.right.left = Node(5)
# root.right.right = Node(6)
# root.right.left.left = Node(7)
# root.right.left.right = Node(8)

# leftLevel(root)



# ===================================================================
'''Check if a given BT is a Binary Search Tree or not
This question is tricky, since it can be solved using simple recursion function
to check if each node is bigger than its left child and smaller than its right child.
But we will not be able to check if a given node is larger than all its left subtree.
Doing this using recursion will take exponential time. Therefore, we do it using 
recursion function with 2 variables, minumum and maximum and keep updating them

Input: 

          8 
       /    \  
      5      10 
     / \       \
    3   7      15
    		  /
    		13 

Output: 
True

'''
INT_MIN = float("-inf")
INT_MAX = float("inf")

def _isBST(root, mini, maxi):
	if root == None: 
		return True

	if root.data < mini or root.data > maxi:
		return False

	return _isBST(root.left, mini, root.data-1) and _isBST(root.right, root.data+1, maxi)


def isBST(root):
	return _isBST(root, INT_MIN, INT_MAX)


# root = Node(10) 
# root.left = Node(2) 
# root.right = Node(15) 
# root.left.left = Node(1) 
# root.left.right = Node(3) 
# print(isBST(root))



# ===================================================================
'''For each path from root to a leaf node. If the path is less than a given number, k
Then delete that path and remove the nodes on this path. 
Input:
               1
           /      \
         2          3
      /     \         \
    4         5        6
  /                   /
 7                   8 


 Say k = 4. Output:

           1
        /     \
      2          3
     /             \
   4                 6
 /                  /
7                  8
'''

def _removeK(root, k, level):
	if root == None:
		return

	root.left = _removeK(root.left, k, level+1)
	root.right = _removeK(root.right, k, level+1)

	if root.left == None and root.right == None and level < k:
		return None

	return root

def removeK(root, k):
	return _removeK(root, k, 1)

def printTry(root):
	if root:
		printTry(root.left)
		print(root.data, end=' ')
		printTry(root.right)


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.left.left.left = Node(7)
# root.right.right= Node(6)
# root.right.right.left = Node(8)

# printTry(root)
# print()
# root_after = removeK(root, 4)
# printTry(root_after)
# print()




# ===================================================================
'''Print root to leaf path without recursion. 
The idea is to use Depth First Search (DFS) algorithm with a stack
Once you hit a leaf node, call the print function.

Input: 

         8 
       /   \  
      5      4 
     / \      \
    9   7     11
    		 /
    		3 

Output: 
8 -> 5 -> 9
8 -> 5 -> 7
8 -> 4 -> 11 -> 3
'''

def printPath(current, parent):
	stack = []
	while current:
		stack.insert(0, current)
		current = parent.get(current)

	while stack:
		cur = stack.pop(0)
		print(cur.data, end=' ')
	print()

def printoLeaf(root):
	if root == None:
		return

	stack = [root]
	parent = {root: None}

	while stack:
		vertex = stack.pop(0)
		if vertex.left == None and vertex.right == None:
			printPath(vertex, parent)

		if vertex.right:
			stack.insert(0, vertex.right)
			parent[vertex.right] = vertex

		if vertex.left:
			stack.insert(0, vertex.left)
			parent[vertex.left] = vertex


# root = Node(10)
# root.left = Node(8)
# root.right = Node(2)
# root.left.left = Node(3)
# root.left.right = Node(5)
# root.right.right = Node(2)

# printoLeaf(root)



# ===================================================================
'''Print the path from root to leaf using an array

Input: 

         8 
       /   \  
      5      4 
     / \      \
    9   7     11
    		 /
    		3 

Output: 
8 -> 5 -> 9
8 -> 5 -> 7
8 -> 4 -> 11 -> 3
'''

def printArray(arr):
	for i in arr:
		print(i, end='  ')
	print()

def _printUsingArray(root, arr, level):
	if root == None:
		return

	try:
		arr[level] = root.data
	except Exception:
		arr.append(root.data)

	level += 1

	if root.left == None and root.right == None:
		printArray(arr)

	_printUsingArray(root.left, arr, level)
	_printUsingArray(root.right, arr, level)


def printUsingArray(root):
	arr = []
	_printUsingArray(root, arr, 0)



# root = Node(10)
# root.left = Node(8)
# root.right = Node(2)
# root.left.left = Node(3)
# root.left.right = Node(5)
# root.right.right = Node(2)

# printUsingArray(root)




# ===================================================================
'''Print the path from the root to each leaf along with nods position.
         A 
       /   \  
      B      C 
     / \    / \
    D   E   F  G

Output:
_ _ A
_ B
D

_ A
B
_ E

 A
 _ C
 F

A
_ C
_ _ G
'''
def printPath(path):
	minIndent = 0
	for element in path:
		if element[1] < minIndent:
			minIndent = element[1]
	offset = abs(minIndent)
	for element in path:
		print(' - ' * (offset + element[1]), element[0].data )
	print()

def traverse(root, path, indent):
	path.append((root, indent))

	if root.left == None and root.right == None:
		printPath(path)

	if root.left:
		traverse(root.left, path, indent-1)
	if root.right:
		traverse(root.right, path, indent+1)
	del path[-1]

def rootoLeafPsition(root):
	arr = []
	traverse(root, arr, 0)


# root = Node('A')
# root.left = Node('B')
# root.right = Node('C')
# root.left.left = Node('D')
# root.left.right = Node('E')
# root.right.left = Node('F')
# root.right.right = Node('G')

# rootoLeafPsition(root)




# ===================================================================
'''Check if there is a path from root to leaf and its sum equals to s

Input: 

         8 
       /   \  
      5      4 
     / \      \
    9   7     11
    		 /
    		3 

Output: If s = 22 then True. If s = 77 Then false
'''

def hasPathSum(root, s):
    if root == None:
        return False

    subSum = s - root.data

    if subSum == 0 and root.left == None and root.right == None:
        return True

    left = hasPathSum(root.left, subSum)
    right = hasPathSum(root.right, subSum)

    return left or right

# =======

def hasPathSum(root, s):
	if root == None:
		return 0

	answer = 0
	subSum = s - root.data

	if subSum == 0 and root.left == None and root.right == None:
		return True

	if root.left:
		answer = answer or hasPathSum(root.left, subSum)
	if root.right:
		answer = answer or hasPathSum(root.right, subSum)

	return answer

  
# s = 21
# root = Node(10) 
# root.left = Node(8) 
# root.right = Node(2) 
# root.left.right = Node(5) 
# root.left.left = Node(3) 
# root.right.left = Node(2) 
  
# print(hasPathSum(root, s))




# ===================================================================
''' Print the length of each path from root to leaf.
the length of each path means the number of nodes

Input: 

         8 
       /   \  
      5      4 
     / \      \
    9   7     11
    		 /
    		3 

Ouput: 
Dictionary will print {3:2, 4:1} means 2 paths have the length of 3, 
and 1 path of length 4
'''

def _pathlength(root, dict, length):
	if root == None:
		return

	if root.left == None and root.right == None:
		if length in dict:
			dict[length] += 1
		else:
			dict[length] = 1
		return

	_pathlength(root.left, dict, length+1)
	_pathlength(root.right, dict, length+1)


def pathlength(root):
	dict = {}
	_pathlength(root, dict, 1)
	print(dict)


root = Node(8) 
root.left = Node(5) 
root.right = Node(4) 
root.left.left = Node(9) 
root.left.right = Node(7) 
root.right.right = Node(11)
root.right.right.left = Node(3)

# pathlength(root) 



# ===================================================================
''' Print the BT using ZigZag traversal
One level from left to right. The level after from right to left...

Input: 

         8 
       /   \  
      5      4 
     /  \      \
    9    7     11
   / \  / \	   / \
  2  3 0  9   7   4 

Ouput: 
8 4 5 9 7 11 2 3 0 9 7 4
'''

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def zikZak(root):
	if root == None:
		return

	currentLevel = [] 
	nextLevel = [] 
	ltr = True
	currentLevel.append(root) 

	while len(currentLevel) > 0: 
		temp = currentLevel.pop(-1) 
		print(temp.data, " ", end="") 

		if ltr: 
			if temp.left:
				nextLevel.append(temp.left)
			if temp.right:
				nextLevel.append(temp.right)
		else:
			if temp.right:
				nextLevel.append(temp.right)
			if temp.left:
				nextLevel.append(temp.left)

		if len(currentLevel) == 0:
			ltr = not ltr
			currentLevel, nextLevel = nextLevel, currentLevel
  

# root = Node(1) 
# root.left = Node(2) 
# root.right = Node(3) 
# root.left.left = Node(7) 
# root.left.right = Node(6) 
# root.right.left = Node(5) 
# root.right.right = Node(4) 
# print("Zigzag Order traversal of binary tree is") 

# zikZak(root) 
# print()



# ===================================================================
''' Print diagonal by diagonal of a BT

Input: 

         8 
       /    \  
      3      10 
     /      /  \
    1      6   14
          /    / 
         4    13   

Ouput: 
8 10 14
3 6 13
1 4
'''

def _printDiagonal(root, dict, dist):
	if root == None:
		return

	try:
		dict[dist].append(root.data)
	except KeyError:
		dict[dist] = [root.data]

	_printDiagonal(root.left, dict, dist+1)
	_printDiagonal(root.right, dict, dist)

def printDiagonal(root):
	dict = {}
	_printDiagonal(root, dict, 0)
	print(dict)


# root = Node(8) 
# root.left = Node(3) 
# root.right = Node(10) 
# root.left.left = Node(1) 
# root.left.right = Node(6) 
# root.right.right = Node(14) 
# root.right.right.left = Node(13) 
# root.left.right.left = Node(4) 
# root.left.right.right = Node(7)

# printDiagonal(root)





# ===================================================================
''' Print diagonal by diagonal of a BT

Input: 

     1
   /   \
  2     2
 / \   / \
3   4 4   3 

Ouput: 
True. Because if you fold the tree in the middle, then 2 will face 2, 3 will face 3
and 4 will face 4 and so on ...
'''

def isMirrorHelp(root1, root2):
	if root1 == root2 == None:
		return True
	if None in [root1, root2]:
		return False
	return root1.data == root2.data and isMirrorHelp(root1.left, root2.right) and isMirrorHelp(root1.right, root2.left)

def isMirror(root):

	if root == None:
		return True
	return isMirrorHelp(root.left, root.right)


# root = Node(8) 
# root.left = Node(3) 
# root.right = Node(10) 
# root.left.left = Node(1) 
# root.left.right = Node(6) 
# root.right.right = Node(14) 
# root.right.right.left = Node(13) 
# root.left.right.left = Node(4) 
# root.left.right.right = Node(7)

# print(isMirror(root))





