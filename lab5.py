class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLeafNodes(root: Node) -> None:
    if (not root):
        return
    if (not root.left and
    not root.right):
        print(root.data,
              end = " ")
        return
    if root.left:
     printLeafNodes(root.left)


    if root.right:
        printLeafNodes(root.right)

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)