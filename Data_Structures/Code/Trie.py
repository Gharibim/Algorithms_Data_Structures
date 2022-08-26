class node(object):
    def __init__(self):
        self.children = {}
        self.isword = False

class trie(object):
    def __init__(self):
        self.root = node()

    def insert(self,word):
        current = self.root
        for i in word:
            if i not in current.children:
                current.children[i]=node()
            current = current.children[i]
        current.isword = True

    def search(self,word):
        cur = self.root
        for i in word:
            if i not in cur.children:
                return False
            print(cur.children)
            cur = cur.children[i]
        return cur.isword


    def shortpref(self,word):
        cur = self.root
        s = 0
        t = len(word)-1
        for i in word:
            if i not in cur.children:
                return t
            elif len(cur.children)>1:
                t = s
            s += 1
            cur = cur.children[i]
        return t+1

t = trie()
A = ["Hola", "Hello", "Hoao", "apple"]
for i in A:
    t.insert(i)

ls = []
for i in A:
    ls.apple(i[:t.shortpref(i)])
print(ls)



# ========================================
class Node:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.isEnd = False
        self.counter = 0


class Trie:
    def __init__(self):
        self.root = Node('')

    def addWord(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = Node(char)
                node.children[char] = new_node
                node = new_node
        node.isEnd = True
        node.counter += 1

    def contrsuctTrie(self, list_of_words):
        for i in list_of_words:
            self.addWord(i)

    def _printAllWords(self, node, word, list_of_words):
        if node.children:
            for char in node.children:
                new_word = word + char
                if node.children[char].isEnd:
                    list_of_words.append(new_word)
                self._printAllWords(node.children[char], new_word, list_of_words)

    def printAllWords(self):
        node = self.root
        list_of_words = []
        for char in node.children:
            word = char
            if node.isEnd:
                list_of_words.append(word)
            self._printAllWords(node.children[char], word, list_of_words)
        return list_of_words

    def searchWord(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        if node.isEnd:
            return True
        return False

    def _walkDeep(self, node, partial_word, list_of_words):
        if node.children:
            for char in node.children:
                new_word = partial_word + char
                if node.children[char].isEnd:
                    list_of_words.append(new_word)
                self._walkDeep(node.children[char], new_word, list_of_words)

    def autoComplete(self, partial_word):
        node = self.root
        list_of_words = []
        for char in partial_word:
            if char in node.children:
                node = node.children[char]
            else:
                return list_of_words
        if node.isEnd:
            list_of_words.append(partial_word)
        self._walkDeep(node, partial_word, list_of_words)
        return list_of_words

    def longestCommonPrefix(self):
        node = self.root
        prefix = ''
        while len(node.children) == 1 and not node.isEnd:
            node = node.children[list(node.children.keys())[0]]
            prefix += node.char
        return prefix or -1



========
class Node:
	num_of_words = 0
	def __init__(self, char):
		self.char = char
		self.children = {}
		self.isEnd = False

class Trie:
	def __init__(self):
		self.root = Node('')

	def addWord(self, word):
		cur = self.root
		for char in word:
			if char in cur.children:
				cur = cur.children[char]
			else:
				cur.children[char] = Node(char)
				cur = cur.children[char]
		cur.isEnd = True
		Node.num_of_words += 1

	def _printAllWords(self, cur, partial_word, all_words):
		for char in cur.children:
			new_word = partial_word + char
			if cur.children[char].isEnd:
				all_words.append(new_word)
			self._printAllWords(cur.children[char], new_word, all_words)

	def printAllWords(self):
		cur = self.root
		all_words = []

		for char in cur.children:
			temp = char
			if cur.children[char].isEnd:
				all_words.append(temp)
			self._printAllWords(cur.children[char], temp, all_words)
		return all_words

	def seachTrie(self, word):
		cur = self.root
		for char in word:
			if char in cur.children:
				cur = cur.children[char]
			else:
				return False
		if cur.isEnd:
			return True
		return False

	def _autoComplete(self, cur, partial_word, all_words):
		for char in cur.children:
			new_word = partial_word + char
			if cur.children[char].isEnd:
				all_words.append(new_word)
			self._autoComplete(cur.children[char], new_word, all_words)

	def autoComplete(self, word):
		cur = self.root
		all_words = []
		for char in word:
			if char in cur.children:
				cur = cur.children[char]
			else:
				return all_words
		if cur.isEnd:
			all_words.append(word)
		self._autoComplete(cur, word, all_words)
		print('allword', all_words)
		return all_words

	def longestCommonPrefix(self):
		longestCommonPrefix = ''
		cur = self.root
		while len(cur.children) == 1 and not cur.isEnd:
			cur = cur.children[list(cur.children.keys())[0]]
			longestCommonPrefix += cur.char
		return longestCommonPrefix or -1







