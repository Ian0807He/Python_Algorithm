class Node(object):
    def __init__(self, prev, item, next):
        self.prev = prev
        self.next = next
        self.item = item

    def getItem(self):
        return self.item

    def setItem(self, newItem):
        self.item = newItem

    def getNext(self):
        return self.next

    def setNext(self, newnext):
        self.next = newnext

    def getPrev(self):
        return self.prev

    def setPrev(self, newprev):
        self.prev = newprev


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        self.curr = None
        self.prev = None

    def add(self, item):
        # Set First Node
        if not self.head:
            self.head = Node(None, item, None)
            self.prev = self.head
            self.curr = self.head

        # Set Current Node
        else:
            self.curr = Node(self.prev, item, None)
            self.prev.setNext(self.curr)
            self.prev = self.curr

        # Get Last Node
        self.last = self.curr

    def remove(self):
        if self.isEmpty():
            return None
        else:
            self.curr = self.curr.prev
            self.prev = self.curr.prev.getPrev()
            self.curr.setNext(None)

        self.last = self.curr


    def foreward(self):
        node = self.head
        data = []
        while node:
            data.append(node.getItem())
            node = node.next
        return data

    def backward(self):
        node = self.last
        data = []
        while node:
            data.append(node.getItem())
            node = node.prev
        return data

    def isEmpty(self):
        return self.head == None
