class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
  def inorder(self, tree):
    if tree !=None:
      self.inorder(tree.left)
      print(tree.data)
      self.inorder(tree.right)
  def postorder(self, tree):
    if tree !=None:
      self.inorder(tree.left)
      self.inorder(tree.right)
      print(tree.data)
  def preorder(self, tree):
    if tree !=None:
      print(tree.data)
      self.inorder(tree.left)
      self.inorder(tree.right)
b = Node(2)
b.left = Node(4)
b.right = Node(10)
b.left.left = Node(19)
b.left.right = Node(13)
b.right.left = Node(12)
b.right.right = Node(11)
print(b.inorder(b))
print(b.postorder(b))
print(b.preorder(b))