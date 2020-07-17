class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if self.head is not None:
            if node.get_next() is not None:
                self.reverse_list(node.get_next(), node)
            if node.get_next() is None:
                node.set_next(prev)
                self.head = node
            else:
                node.set_next(prev)
        #base we reached the tail/ the next is none
            #update its next to previous
    


# test = LinkedList()
# test.add_to_head(1)
# test.add_to_head(2)
# test.add_to_head(3)
# test.add_to_head(4)
# test.add_to_head(5)
# print(test.head.value)
# print(test.head.get_next().value)
# print(test.head.get_next().get_next().value)
# print(test.head.get_next().get_next().get_next().value)
# print(test.head.get_next().get_next().get_next().get_next().value)
# test.reverse_list(test.head, None)
# print("Reversed")
# print(test.head.value)
# print(test.head.get_next().value)
# print(test.head.get_next().get_next().value)
# print(test.head.get_next().get_next().get_next().value)
# print(test.head.get_next().get_next().get_next().get_next().value)
