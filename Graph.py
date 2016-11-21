class GraphNode(object):
    def __init__(self, item, nextNodes=[]):
        self.item = item
        self.to = []
        for x in nextNodes:
            self.to.append(GraphNode(x))

    def getItem(self):
        return self.item

    def getNextNodes(self):
        return self.to
