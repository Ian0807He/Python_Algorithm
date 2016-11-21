class Node(object):
  def __init__(self,item,next):
    self.item=item
    self.next=next
  def getItem(self):
    return self.item
  def getNext(self):
    return self.next
  def setItem(self,newitem):
    self.item=newitem

class LinkedList(object):
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

    def isEmpty(self):
        return self.head == None
