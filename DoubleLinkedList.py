class Node(object):
    __slots__ = ('prev', 'next', 'item')
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


class DoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self.last = None
        self.curr = None
        self.prev = None
        self.size = 0

    def __len__(self):
        return self.size

    def insertHead(self, item):
        new = Node(None, item, self.head)
        self.head.setPrev(new)
        self.head = new

    def insertEnd(self, item):
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
        self.size += 1

    def remove(self, item):
        # If there is no item in the list, return nothing
        if not self.head:
            print("There is no item in list")
            return
        curr = self.head
        # if it is the first item
        if curr.getItem() is item:
            self.removeHead()
            return
        while curr.getNext():
            last = curr
            curr = curr.getNext()
            if curr.getItem() is item:
                last.setNext(curr.getNext())
                if curr.getNext():
                    curr.getNext().setPrev(last)
                return
        # if it is the last item
        if self.last.getItem is item:
            self.removeEnd()
            return
        # if there is no such item
        print("There is no such item in list")


    def removeHead(self):
        # if it is an empty list, return
        if self.isEmpty():
            return None
        elif not self.head.getNext():
            self.head = None
        else:
            self.head = self.head.getNext()
            self.head.setPrev(None)

    def removeEnd(self):
        # if it is an empty list, return
        if self.isEmpty():
            return None
        elif not self.head.getNext():
            self.head = None
        elif not self.curr.prev.getPrev():
            self.head.setNext(None)
        else:
            self.curr = self.curr.prev
            self.prev = self.curr.prev.getPrev()
            self.curr.setNext(None)
            self.last = self.curr
            self.size -= 1

    def search(self, item):
        # generator, and it will find all item and print where they are
        num = 1
        find = False
        if self.head.getItem() is item:
            yield num
            find = True
        curr = self.head
        while curr.getNext():
            num += 1
            curr = curr.getNext()
            if curr.getItem() is item:
                yield num
                find = True
        if not find:
            yield False

    def foreward(self):
        # walk through from first to last
        node = self.head
        data = []
        while node:
            data.append(node.getItem())
            node = node.next
        return data

    def backward(self):
        # walk through from last to first
        node = self.last
        data = []
        while node:
            data.append(node.getItem())
            node = node.prev
        return data


    def isEmpty(self):
        return self.head == None
