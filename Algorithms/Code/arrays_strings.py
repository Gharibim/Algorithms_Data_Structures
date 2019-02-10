# ==================print greatest common divisor (GCD) ============
# Recursive function
def GCD(A, B):
	if B == 0:
		return A
	else:
		return GCD(B, A%B)
# print(GCD(10,20))

# Iterative function
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
# print(gcd(10, 20))



# ================== Majority element ============
# Given a function return the majority element that appears more than n/2 times
# where n is the size of the array
# This solution assumes the majority elements always exists. Otherwise use a dictionary
def maj(arr):
	maj_index = 0
	count = 1
	for i in range(1, len(arr)):
		if arr[maj_index] == arr[i]:
			count += 1
		else:
			count -= 1
		if count == 0:
			maj_index = i
			count = 1
	return arr[maj_index]



# ================== count last word ============
# Without using any predefined functions, write a function to count the last word
# characters. Input could be differe, for example: (Ignore spaces)
# "Hello"  -> 5
# "Hello hi"  -> 2
# "Hello hi  " -> 2

def countLast(sen):
	count = 0
	for i in range(len(sen)):
		if sen[i] == " ":
			if i + 1 < len(sen) and sen[i+1] != " ":
				count = 0
		else:
			count += 1
	return count


# ================== Wave sort ============
# Wave sort is a sort where we start with large number, then smaller, then larger, smaller,..
# Input: 10, 5, 6, 3, 2, 20, 100, 80

# Output: could be one of many formats:
# 10, 5, 6, 2, 20, 3, 100, 80
# 20, 5, 10, 2, 80, 6, 100, 3

# This solution sort the array first so it takes O(n log n)
def Wave(arr):
	arr.sort()
	for i in range(0, len(arr)-1, 2):
		arr[i], arr[i+1] = arr[i+1], arr[i]
	print(arr)

# this solution iterate once through the array, O(n)
def Wave(arr):
	for i in range(0, len(arr), 2):
		if i > 0 and arr[i] < arr[i-1]:
			arr[i], arr[i-1] = arr[i-1], arr[i]
		if i < len(arr)-1 and arr[i] < arr[i+1]:
			arr[i], arr[i+1] = arr[i+1], arr[i]
	print(arr)



# ================== remove all instances of a num ============
# Given an array and a number, remove all the instances of that number from the array
# The idea is to do this without deleting, since each delete takes O(n).
# So we do it by swapping the instances to the right, then return the count
# of how many instances or we return from the beginning of the array to size - count
# Note input array here is not sorted

def removeIns(arr, num):
	count = 0
	for i in range(len(arr)):
		if arr[i] == num:
			continue
		else:
			arr[count] = arr[i]
			count += 1
	return count



# ================== remove all instances from sorted array ============
# Same as above but the input array is sorted

def removeInstances(arr):
	count = 0
	for i in range(len(arr)):
		if i < len(arr) - 1 and arr[i] == arr[i+1]:
			continue
		else:
			arr[count] = arr[i]
			count += 1
	return count


# ================== check if A[i]-A[j] == B  array sorted============
# Given an array we want to check if there exist 2 numbers where A[i] - A[j] == B
# and i < j and i != j
# Input array is sorted
def check(arr, B):
	i = 0
	j = 1
	while i < len(arr) and j < len(arr):
		if i != j and arr[j] - arr[i] == B:
			return True
		elif arr[j] - arr[i] < B:
			j += 1
		else:
			i += 1
	return False



# ================== check if A[i]-A[j] == B array not sorted============
# Same as above but the given array is not sorted and i could be equal to j
def check2(arr, B):
	dict = {}
	for i in arr:
		if i in dict:
			dict[i] += 1
		else:
			dict[i] = 1
	for i in range(len(arr)):
		temp = arr[i]
		if (temp - B >= 0) and (temp - B) in dict:
			if B == 0:
				if dict[temp] >= 2:
					return True
			else:
				return True
	return False




# ================== count number of trailing 0's in n! ============
# Given a number, say 5. We want to count how many 0's are in n!
# So given 5, we want number of 0's in 5!. Since 5! = 120 then
# return 1, since 120 has only one 0
def countZero(num):
	count = 0
	i = 5
	while (num/i >= 1):
		count += int(num/i)
		i *= 5
	return count


# ================== print excel sheet  A -> 1 B -> 2  AA -> 27 ============
# Given a similar sequence to Excel where:
# A -> 1
# B -> 2
# ...
# AA -> 27
# AB -> 28

# Write a function to take a list of charachters and return their value
def Excel(chars):
	result = 0
	for i in chars:
		result *= 26
		result += ord(i) - ord('A') + 1
	return result


# ================== print Pascal triangle ============
# Printing Pascal tringale is an easy job using this function. 
# Instead of 'zipp' function you can simple use the builtin function 'zip'
# but in case the interviewer said no builtin functions, then here is 'zip' implementation
def zipp(a, b):
	return [(a[i],b[i]) for i in range(len(a))]

def Pascal(rows):
	trow = [1]
	y = [0]
	result = []
	for i in range(rows):
		result.append(trow)
		trow = [l+r for l,r in zipp(trow+y, y+trow)]
	return result


# ================== return n'th pascal row ============
# Return any index from Pascal trinagle. The solution is to print all Pascal triangle
# up to that index, then return a given index
def PascalRow(num):
	trow = [1]
	y = [0]
	result = []
	for i in range(num+1):
		result.append(trow)
		trow = [l+r for l,r in zip(trow+y, y+trow)]
	return result[num]



# ======= grid you want to reach to mn with obstacles ============
# Given a grid, matrix, contains 0's and 1's and the starting point is (0,0), 
# you need to reach the end. If the number is 1 means it is an obstacle.
# Count the shortest path to reach to the end

def reach(A):
	row = len(A)
	col = len(A[0])
	path = [[0 for i in range(col)] for j in range(row)]
	for i in range(row):
		for j in range(col):
			if A[i][j]:
				continue
			if i == 0 and j == 0:
				path[i][j] = 1
			if i > 0:
				path[i][j] += path[i-1][j]
			if j > 0:
				path[i][j] += path[i][j-1]
	return path[row-1][col-1]



# ======= search number in semi-sorted array ============
# Semi sorted array is two sorted arrays where added to each other as follows:
# [5,6,7,8,9,1,2,3,4]
# The idea is to do binary search but before check if the half is sorted or not
# Then check if the target in this half or not
def search(arr, left, right, target):
	if left > right:
		return -1
	mid = (left + right) // 2
	if arr[mid] == target:
		return mid

	if arr[left] <= arr[mid]:
		if arr[left] <= target and target <= arr[mid]:
			return search(arr, left, mid, target)
		return search(arr, mid+1, right, target)

	if target >= arr[mid] and target <= arr[right]:
		return search(arr, mid+1, right, target)
	return search(arr, left, mid-1, target)




# ======= spiral array display ============
# Print the array in a spiral way

def Spiral(arr):
	row_length = len(arr)
	col_length = len(arr[0])

	starting_row = starting_col = 0

	while starting_row < row_length and starting_col < col_length:

		for i in range(starting_row, col_length):
			print(arr[starting_row][i], end=' ')

		starting_row += 1

		for i in range(starting_row, row_length):
			print(arr[i][col_length-1], end=' ')

		col_length -= 1


		if starting_row < row_length:
			for i in range(col_length-1, starting_col-1, -1):
				print(arr[row_length-1][i], end=' ')

			row_length -= 1


		if starting_col < col_length:
			for i in range(row_length-1, starting_row-1, -1):
				print(arr[i][starting_col], end=' ')

			starting_col += 1
	print()


arr = [ [1, 2, 3, 4, 5, 6], 
      [7, 8, 9, 10, 11, 12], 
      [13, 14, 15, 16, 17, 18]] 

# Spiral(arr)




# ======= rotate array 90 degress inplace ============
def reverseCols(arr):
	for i in range(len(arr[0])):
		j = 0
		k = len(arr[0]) - 1

		while j < k:
			temp = arr[j][i]
			arr[j][i] = arr[k][i]
			arr[k][i] = temp
			j += 1
			k -= 1

def transpose(arr):
	for i in range(len(arr)):
		for j in range(i, len(arr[0])):
			temp = arr[i][j]
			arr[i][j] = arr[j][i]
			arr[j][i] = temp

def rotateArray(arr):
	transpose(arr)
	reverseCols(arr)



def printArray(arr):
	for i in range(len(arr)):
		for j in range(len(arr[0])):
			print(arr[i][j], end=' ')
		print()
	print()



arr = [ [1, 2, 3], 
      [7, 8, 9], 
      [13, 14, 15]] 


# printArray(arr)
# rotateArray(arr)
# printArray(arr)



# ======= if 2 + 2 = 4 both prime ============
# Given a number, say 4. Check if there exist to prime number that their sum
# equals to the given number

class Solution:
    def primesum(self, A):
        for i in xrange(2, A):
            if self.isPrime(i) and self.isPrime(A-i):
                return i, A-i
        
    def isPrime(self, A):
        if A < 2:
            return False
        for i in xrange(2, int(A**0.5) + 1):
            if A % i  == 0:
                return False
        return True



# ======= A = r ^ p ============
# Given a number ,A, check if this number can be represented using two number r, p
# where r^p = A
def isPower(self, A):
        if A == 1:
            return True
        for i in xrange(2, int(A**0.5)+1):
            temp = A
            while(temp % i == 0):
                temp = int(temp/i)
            if temp == 1:
                return True
        return False



# ======= Grid and shortest number of steps ============
# Given a grid contains 0's and 1's. Where you can move in all 8 different ways.
# Calculate the shortest number of moves to reach a distination from the source X
    def coverPoints(self, X, Y):
        steps = 0
        curX = X[0]
        curY = Y[0]
        for i in range(1, len(X)):
            steps += max(abs(curX - X[i]), abs(curY - Y[i]))
            curX = X[i]
            curY = Y[i]
        return steps



# ======= Check all combinations for a^2 + b^2 = A ============
# Given a number A, check all the combinations for a and b where
# a^2 + b^2 = A
	def squareSum(self, A):
		answer = []
		a = 1
		while a*a < A:
		    b = 1
		    while b*b < A:
		        if a <= b and (a*a) + (b*b) == A:
		            temp = [a,b]
		            answer.append(temp)
		        b += 1
		    a += 1
		return answer


# ======= Print the diagonals of a matrix ============

	def diagonal(self, a):
	    arr = []
	    dia = []
	    n = len(a)
	    for d in range(2 * n -1):
	        for i in range(d + 1):
	            j = d - i
	            if i >= n or j >= n:
	                continue
	            dia.append(a[i][j])
	        arr.append(dia)
	        dia = []
	    return arr




# ================ Power of 2 ============
# Given a number, check if this number is power of 2 or not
def checkPower(A):
	A = int(A)
	return 1 if (A > 1 and A & (A - 1) == 0) else 0




# ======= Give all different combinations ============
# Print all different combinations of a given array.
# The array may have duplicates 

class Solution:
    def subsetsWithDup(self, A):
        n = 2**len(A)
        subsets = set()

        A = sorted(A)

        for i in xrange(n):
            subset = []
            for j, v in enumerate(A):
                if i & (1 << j):
                    subset.append(v)
            subsets.add(tuple(subset))

        return sorted(subsets)




# ======= permutations ============
# Print all permutations for a given array
def permute(self, A):
	if len(A) < 2:
	    return [A]
	output = []
	for i in xrange(len(A)):
	    output += [[A[i]] + permut_rest for permut_rest in self.permute(A[:i] + A[i+1:])]
	return output




# =================== Longest Common Subsequence (LCS) ========
def lcs(X, Y, L):
    for i in range(len(X)+1):
        for j in range(len(Y)+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = 1 + L[i-1][j-1]
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    return L[len(X)][len(Y)]



# X = "AGGTAB"
# Y = "GXTXAYB"
# m = len(X) 
# n = len(Y) 
# L = [[0 for x in range(n+1)] for x in range(m+1)] 

# print ("Length of LCS is ", lcs(X, Y, L))








