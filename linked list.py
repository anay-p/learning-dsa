class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, *nodes: Node):
        self.start = nodes[0]
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]

    @classmethod
    def from_list(cls, data_list: list):
        return cls(*[Node(i) for i in data_list])

    def __repr__(self) -> str:
        x = self.start
        s = ""
        while True:
            if x.next is not None:
                s += str(x.data) + " -> "
            else:
                s += str(x.data)
                break
            x = x.next
        return s

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
l = LinkedList(n1, n2, n3)

l2 = LinkedList.from_list([1, 5, 9])
print(l2)
