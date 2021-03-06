from BinaryTree import *

print("\n\nBinaryTree:\n")
r = BinaryTree()
r1 = BinaryTree()
r1.makeTree(1,None,None)
r2 = BinaryTree()
r2.makeTree(2,r1,None)
r3 = BinaryTree()
r3.makeTree(3,None,None)
r4 = BinaryTree()
r4.makeTree(4,r2,r3)
r5 = BinaryTree()
r5.makeTree(5,None,None)
r6 = BinaryTree()
r6.makeTree(6,None,None)
r7 = BinaryTree()
r7.makeTree(7,r5,r6)
r.makeTree(8,r4,r7)
print('PreOrder')
r.preOrder(r)
print('InOrder')
r.inOrder(r)
print('PostOrder')
r.postOrder(r)
print('levelOrder')
r.levelOrder(r)
print('invertOrder')
r.invertOrder(r)
