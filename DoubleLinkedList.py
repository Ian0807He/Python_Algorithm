class Node(object):
    __slots__ = ('pr', 'ne', 'it')
    def __init__(self, pr, it, ne):
        self.pr = pr
        self.ne = ne
        self.it = it

    @property
    def item(self):
        return self.it

    @item.setter
    def item(self, newItem):
        self.it = newItem

    @property
    def next(self):
        return self.ne

    @next.setter
    def next(self, newnext):
        self.ne = newnext

    @property
    def prev(self):
        return self.pr

    @prev.setter
    def prev(self, newprev):
        self.pr = newprev


class DoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self.last = None
        self.curr = None
        self.pr = None
        self.size = 0

    def __len__(self):
        return self.size

    def insertHead(self, it):
        new = Node(None, it, self.head)
        self.head.prev = new
        self.head = new

    def insertEnd(self, it):
        # Set First Node
        if not self.head:
            self.head = Node(None, it, None)
            self.pr = self.head
            self.curr = self.head
        # Set Current Node
        else:
            self.curr = Node(self.pr, it, None)
            self.pr.next = self.curr
            self.pr = self.curr
        # Get Last Node
        self.last = self.curr
        self.size += 1

    def remove(self, it):
        # If there is no it in the list, return nothing
        if not self.head:
            print("There is no it in list")
            return
        curr = self.head
        # if it is the first it
        if curr.item is it:
            self.removeHead()
            return
        while curr.next:
            last = curr
            curr = curr.next
            if curr.item is it:
                last.next = curr.next
                if curr.next:
                    curr.next.prev = last
                return
        # if it is the last it
        if self.last.getItem is it:
            self.removeEnd()
            return
        # if there is no such it
        print("There is no such it in list")


    def removeHead(self):
        # if it is an empty list, return
        if self.isEmpty():
            return None
        elif not self.head.next:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def removeEnd(self):
        # if it is an empty list, return
        if self.isEmpty():
            return None
        elif not self.head.next:
            self.head = None
        elif not self.curr.pr.prev:
            self.head.next = None
        else:
            self.curr = self.curr.pr
            self.pr = self.curr.pr.prev
            self.curr.next = None
            self.last = self.curr
            self.size -= 1

    def search(self, it):
        # generator, and it will find all it and print where they are
        num = 1
        find = False
        if self.head.item is it:
            yield num
            find = True
        curr = self.head
        while curr.next:
            num += 1
            curr = curr.next
            if curr.item is it:
                yield num
                find = True
        if not find:
            yield False

    def foreward(self):
        # walk through from first to last
        node = self.head
        data = []
        while node:
            data.append(node.item)
            node = node.ne
        return data

    def backward(self):
        # walk through from last to first
        node = self.last
        data = []
        while node:
            data.append(node.item)
            node = node.pr
        return data


    def isEmpty(self):
        return self.head == None
