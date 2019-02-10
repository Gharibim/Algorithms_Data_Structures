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












