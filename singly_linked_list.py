class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = None

    def add(self, node):
        current = None

        if not self.head:
            self.head = node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = node

        return self.head

    def remove(self, node):
        current = self.head
        previous = None

        while current:
            if current == node:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next

                break

            previous = current
            current = current.next

        return self.head

    def print(self):
        current = self.head

        while current:
            print(current.value)
            current = current.next


if __name__ == "__main__":
    linked_list = LinkedList()
    node1 = Node("a")
    node2 = Node("b")
    node3 = Node("c")
    node4 = Node("d")

    linked_list.add(node1)
    linked_list.add(node2)
    linked_list.add(node3)
    linked_list.add(node4)
    linked_list.print()

    linked_list.remove(node1)
    linked_list.remove(node3)
    linked_list.print()
