class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.length = 0

    def __str__(self):
        pass

    def add_to_tail(self, value):
        if self.tail is None:
            new_tail = Node(value, None)
            self.head = new_tail
            self.tail = new_tail
        else:
            new_tail = Node(value, None)
            old_tail = self.tail
            old_tail.next = new_tail
            self.tail = new_tail
        self.length += 1

    def remove_head(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return current_head.value
        else:
            current_head = self.head
            self.head = current_head.next
            self.length = self.length - 1
            return current_head.value

    def remove_tail(self):
        pass
        # Remove Tail:
        # Check if it's there
        # General case:
        # Start at head and iterate to the next-to-last node
        # Stop when current_node.next == self.tail
        # Save the current_tail value
        # Set self.tail to current_node
        # Set current_node.next to None
        #
        # List of 1 element:
        # Save the current_tail.value
        # Set self.tail to None
        # Set self.head to None
