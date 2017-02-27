class Tree:
    def __init__(self, value, root=None):
        self.lchild = None
        self.rchild = None
        self.value = value
        self.root = root

    def add(self, value):
        curent_node = self
        last_node = None

        while curent_node:
            last_node = curent_node
            if value > curent_node.value:
                curent_node = curent_node.rchild
            elif value < curent_node.value:
                curent_node = curent_node.lchild
            else:
                return False
        new_node = Tree(value, last_node)
        if value > last_node.value:
            last_node.rchild = new_node
        else:
            last_node.lchild = new_node
        return True

    def find(self, value):
        curent_node = self
        while curent_node:
            if value > curent_node.value:
                curent_node = curent_node.rchild
            elif value < curent_node.value:
                curent_node = curent_node.lchild
            elif value == curent_node.value:
                return True
        return False


root = Tree(10)
root.add(9)
root.add(8)
root.add(11)
root.add(15)
root.add(16)
root.add(12)
root.add(2)
root.find(16)
