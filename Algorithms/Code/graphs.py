# defaul dictionary useful to return dict[key] without error
from collections import defaultdict 

# Graph example represted using linked list
graph1 = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A" ,"B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}

# second graph example represented using linked list to test different cases
g = {
    "A": ["C", "D"],
    "B": ["A"],
    "C": ["B"],
    "D": ["E"],
    "E": []
}

# A graph represtend using an adjacency matrix 
#         0 1 2 3 4 5 
graph2 = [[0,1,1,0,0,0],
         [1,0,1,1,0,0],
         [1,1,0,1,1,0],
         [0,1,1,0,1,1],
         [0,0,1,1,0,0],
         [0,0,0,1,0,0]]



#================ BFS algorithm Using Queue =============
def BFS(graph, source):
	queue = []
	queue.append(source)
	visited = set()
	visited.add(source)
	while queue:
		vertex = queue.pop(0)
		print(vertex)
		for v in graph[vertex]:
			if v not in visited:
				visited.add(v)
				queue.append(v)

# BFS(graph1, 'A')



#================ BFS using a queue To detect a cycle =============
def BFS(graph, source):
	queue = [source]
	visited = set()
	visited.add(source)
	parent = {}
	parent[source] = -1
	while queue:
		vertex = queue.pop(0)
		print(vertex)
		for v in graph[vertex]:
			if v not in visited:
				visited.add(v)
				queue.append(v)
				parent[v] = vertex
			elif v in visited and parent[vertex] != v:
				print("cycle")

# BFS(graph1, 'A')



#================ DFS using recursion =============
def DFSUtil(graph, u, visited):
	visited.add(u)
	print(u)
	for v in graph[u]:
		if v not in visited:
			visited.add(v)
			DFSUtil(graph, v, visited)

def DFS(graph, source):
	visited = set()
	DFSUtil(graph, source, visited)

# DFS(g, 'A')



#===== DFS using recursion to detect a cycle =============
def DFSUtil(graph, u, visited, parent):
	visited.add(u)
	print(u)
	for v in graph[u]:
		if v not in visited:
			visited.add(v)
			parent[v] = u
			DFSUtil(graph, v, visited, parent)
		elif v in visited and parent[u] != v:
			print("Cycle")

def DFS(graph, source):
	visited = set()
	parent = {}
	parent[source] = -1
	DFSUtil(graph, source, visited, parent)

# DFS(g, 'A')



#=============== DFS using a stack =============
def DFS(graph, source):
	stack = [source]
	visited = set()
	visited.add(source)
	while stack:
		vertex = stack.pop(0)
		print(vertex)
		for v in graph[vertex]:
			if v not in visited:
				visited.add(v)
				stack.insert(0, v)

# DFS(graph1, 'A')


#=============== DFS using a stack + detect a cycle =============
def DFS(graph, source):
	stack = [source]
	visited = set()
	parent = {source: -1}
	while stack:
		vertex = stack.pop(0)
		print(vertex)
		for v in graph[vertex]:
			if v not in visited:
				visited.add(v)
				stack.insert(0, v)
				parent[v] = vertex
			elif v in visited and parent[vertex] != v:
				print("Cycle")

# DFS(graph1, 'A')



#=============== BFS shortest path =============
# returnt the shortest path between source and dist
def BFSHortestPAth(graph, source, dist):
	queue = [[source]]
	visited = set()
	visited.add(source)
	while queue:
		path = queue.pop(0)
		vertex = path[-1]
		if vertex == dist:
			return path
		for v in graph[vertex]:
			if v not in visited:
				visited.add(v)
				new_path = list(path)
				new_path.append(v)
				queue.append(new_path)

# print(BFSHortestPAth(graph1, 'A', 'E'))


#=============== DFS using a adjacency matrix =============
def DFSMat(mat):
	stack = [0]
	visited = [0] * len(mat)
	visited[0] = 1
	while stack:
		vertex = stack.pop(0)
		print(vertex)
		for v in range(len(visited)):
			if mat[vertex][v] == 1 and visited[v] == 0:
				visited[v] = 1
				stack.insert(0, v)

# DFSMat(graph2)



#=============== BFS using a adjacency matrix =============
def BFSMat(mat):
	queue = [0]
	visited = [0] * len(mat)
	visited[0] = 1
	while queue:
		vertex = queue.pop(0)
		print(vertex)
		for v in range(len(visited)):
			if mat[vertex][v] == 1 and visited[v] == 0:
				visited[v] = 1
				queue.append(v)
# BFSMat(graph2)



#=============== Topological Sorting =============
def TSUtil(graph, visited, stack, u):
	visited.add(u)
	for v in graph[u]:
		if v not in visited:
			visited.add(v)
			TSUtil(graph, visited, stack, v)
	stack.insert(0, u)


def TS(graph):
	stack = []
	visited = set()
	for v in graph:
		if v not in visited:
			TSUtil(graph, visited, stack, v)
	print(stack)

# TS(g)


#=============== Strongly Connected Components =============
def tran(graph):
	tran_Graph = defaultdict(list)
	for v in graph:
		for i in graph[v]:
			tran_Graph[i].append(v)
	return tran_Graph

def SCCUtil(u, visited, tran_Graph):
	visited.add(u)
	print(u, end=' ')
	for v in tran_Graph[u]:
		if v not in visited:
			SCCUtil(v, visited, tran_Graph)

def fillStack(u, visited, stack, graph):
	visited.add(u)
	for v in graph[u]:
		if v not in visited:
			fillStack(v, visited, stack, graph)
	stack.insert(0, u)

def SCC(graph):
	stack = []
	visited = set()

	for v in graph:
		if v not in visited:
			fillStack(v, visited, stack, graph)

	tran_Graph = tran(graph)

	visited = set()

	while stack:
		vertex = stack.pop(0)
		if vertex not in visited:
			SCCUtil(vertex, visited, tran_Graph)
			print()

# SCC(g)



#=============== Count the connected islands =============
def isSafe(i, j, visited):
	return i >= 0 and i < row and j >= 0 and j < col and visited[i][j] == False and mat[i][j] == 1

def DFSI(i, j, visited):
	visited[i][j] = True
	row = [-1, -1, -1, 0, 0, 1, 1, 1]
	col = [-1, 0, 1, -1, 1, -1, 0, 1]

	for k in range(8):
		if isSafe(i+row[k], j+col[k], visited):
			DFSI(i+row[k], j+col[k], visited)

def countIslands(mat, row, col):
	visited = [[False for j in range(col)] for i in range(row)]

	count = 0
	for i in range(row):
		for j in range(col):
			if mat[i][j] == 1 and visited[i][j] == False:
				DFSI(i, j, visited)
				count += 1
	print(count)


# mat = [[1, 1, 0, 0, 0], 
# 		[0, 1, 0, 0, 1], 
# 		[1, 0, 0, 1, 1], 
# 		[0, 0, 0, 0, 0], 
# 		[1, 0, 1, 0, 1]] 
# row = len(mat)
# col = len(mat[0])
# countIslands(mat, row, col)




#=========== return all paths from a source to distination using DFS ========
def allPathsUtil(u, d, graph, visited, path):
	visited.add(u)
	path.append(u)

	if u == d:
		print(path)

	else:
		for v in graph[u]:
			if v not in visited:
				allPathsUtil(i, d, graph, visited, path)

	path.pop()
	visited.remove(u)


def allPaths(graph, u, v):
	path = []
	visited = set()
	allPathsUtil(u, v, graph, visited, path)







