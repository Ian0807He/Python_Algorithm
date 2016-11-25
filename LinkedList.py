class Node(object):
    __slots__ = ('it', 'ne')
    def __init__(self,it,ne):
        self.it=it
        self.ne=ne

    @property
    def item(self):
        return self.it

    @item.setter
    def item(self,newitem):
        self.it=newitem

    @property
    def next(self):
        return self.ne

    @next.setter
    def next(self, newitem):
        self.ne = newitem

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.curr = None
        self.last = None

    def addEnd(self, it):
        self.curr = Node(it, None)
        if self.head is None:
            self.head = self.curr
        else:
            self.last.next = self.curr
        self.last = self.curr

    def addHead(self, it):
        if self.head:
            self.head = Node(it, self.head)
        else:
            self.head = Node(it, None)

    def isEmpty(self):
        return self.head == None

    def printList(self):
        data = []
        if self.isEmpty():
            return False
        curr = self.head
        data.append(curr.item)
        while curr.next:
            curr = curr.next
            data.append(curr.item)
        return data

    def remove(self, it):
        if self.isEmpty():
            return False
        else:
            curr = self.head
            if curr.it is it:
                self.head = curr.next
            while curr.next:
                last = curr
                curr = curr.next
                if curr.it is it:
                    last.next = curr.next
                    return
            if curr.item is it:
                last.next = None
            else:
                return False

    def search(self, it):
        if self.isEmpty():
            yield False
        else:
            curr = self.head
            find = False
            num = 1
            if curr.item is it:
                yield num
                num += 1
                find = True
            while curr.next:
                curr = curr.next
                num += 1
                if curr.item is it:
                    yield num
                    find = True
            if not find:
                yield False
