class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


# Прямой обход дерева
def pre_order(node: TreeNode) -> None:
    if node:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)


# Обратный обход дерева
def post_order(node: TreeNode) -> None:
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.value)


# Обратный обход дерева
def in_order(node: TreeNode) -> None:
    if node:
        in_order(node.left)
        print(node.value)
        in_order(node.right)


def main():
    tree = TreeNode(1)
    tree.left = TreeNode(6)
    tree.left.left = TreeNode(5)
    tree.left.right = TreeNode(1)
    tree.right = TreeNode(4)
    tree.right.left = TreeNode(7)
    tree.right.right = TreeNode(9)
    in_order(tree)


if __name__ == "__main__":
    main()
