# I used getters and setters for Node attributes to make it easier.
# Check Single List implementation to see the implementation without getters and setters
class Node:
    number = 0
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        Node.number += 1

    def setData(self, value):
        self.data = value
    def setPrev(self, pointer):
        self.prev = pointer
    def setNext(self, pointer):
        self.next = pointer

    def getData(self):
        return self.data
    def getPrev(self):
        return self.prev
    def getNext(self):
        return self.next

class DoubleList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    # Add at the beginning of the list
    def addTop(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        temp.setPrev(None)
        self.head = temp

    # add the value 'value' after the value 'item'
    def addAfter(self, item, value):
        cur = self.head
        while cur:
            if cur.getData() == item:
                temp = Node(value)
                temp.setNext(cur.getNext())
                temp.setPrev(cur)
                cur.setNext(temp)
            cur = cur.getNext()


    # Delete a node
    def remove(self, item):
        pre = None
        cur = self.head
        while cur:
            if cur.getData() == item:
                if self.head == cur:
                    self.head = cur.getNext()
                    return

                elif cur.getNext() == None:
                    pre.setNext(None)
                else:
                    pre.setNext(cur.getNext())
                    (cur.getNext()).setPrev(pre)

            pre = cur
            cur = cur.getNext()

    def search(self, item):
        cur = self.head
        found = False
        while cur:
            if cur.getData() == item:
                found = True
            cur = cur.getNext()
        return found

    def size(self):
        return Node.number

    # Print the list
    def display(self):
        cur = self.head
        while cur:
            print(cur.getData())
            cur = cur.getNext()


