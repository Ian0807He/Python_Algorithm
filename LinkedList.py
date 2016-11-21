class Node(object):
    def __init__(self,item,next):
        self.item=item
        self.next=next

    def getItem(self):
        return self.item

    def getNext(self):
        return self.next

    def setNext(self, newitem):
        self.next = newitem

    def setItem(self,newitem):
        self.item=newitem

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.curr = None
        self.last = None

    def addEnd(self, item):
        self.curr = Node(item, None)
        if self.head is None:
            self.head = self.curr
        else:
            self.last.setNext(self.curr)
        self.last = self.curr

    def addHead(self, item):
        if self.head:
            self.head = Node(item, self.head)
        else:
            self.head = Node(item, None)

    def isEmpty(self):
        return self.head == None

    def printList(self):
        data = []
        if self.isEmpty():
            return False
        curr = self.head
        data.append(curr.getItem())
        while curr.getNext():
            curr = curr.getNext()
            data.append(curr.getItem())
        return data

    def search(self, item):
        if self.isEmpty():
            yield False
        else:
            curr = self.head
            find = False
            num = 1
            if curr.getItem() is item:
                yield num
                num += 1
                find = True
            while curr.getNext():
                curr = curr.getNext()
                num += 1
                if curr.getItem() is item:
                    yield num
                    find = True
            if not find:
                yield False
