class Node():
  __slots__=['_item','_next']
  def __init__(self,item):
    self.item=item
    self.next=None
  def getItem(self):
    return self.item
  def getNext(self):
    return self.next
  def setItem(self,newitem):
    self.item=newitem

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next
            return item

    def is_empty(self):
        return self.head == None
