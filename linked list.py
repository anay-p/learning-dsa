class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, *data):
        last_node = Node(data[-1])
        for i in data[-2::-1]:
            last_node = Node(i, last_node)
        self.start = last_node

    @classmethod
    def from_list(cls, data_list: list):
        return cls(*data_list)

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

    def print_in_reverse(self):
        def reverse(node):
            if node is not None:
                reverse(node.next)
                print(node.data, end=' -> ')
        reverse(self.start)

if __name__ == '__main__':
    l = LinkedList('Hello', 1, True, {1, 2, 7, 5})
    m = LinkedList.from_list([0, 1, 1, 2, 3, 5, 8, 13])
    print(l, m, sep="\n")
    m.print_in_reverse()
