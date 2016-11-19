class Node(object):
    def __init__(self, prev, item, next):
        self.prev = prev
        self.next = next
        self.item = item

    def getItem(self):
        return self.item

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setItem(self, newItem):
        self.item = newItem

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def add(self, item):
        self.head = Node(self.last, item, self.head)
        self.last = item

    def remove(self):
        if self.isEmpty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next
            self.last = self.head.prev
            return item

    def isEmpty(self):
        return self.head == None
