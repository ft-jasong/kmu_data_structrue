class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        if self is other or self.item == other.item:
            return True
        return False
    def __str__(self):
        return f"{self.item}"

class SinglyLinkedList:
    def __init__(self):
        self.head = self.next_ = None
    def __iter__(self):
        self.next_ = self.head
        return self
    def __next__(self):
        if self.next_ is None:
            raise StopIteration
        n = self.next_
        self.next_ = self.next_.next
        return n
    def add_head(self, node_new):
        if self.head is None:
            self.head = node_new
        else:
            node_new.next = self.head
            self.head = node_new
    def add_tail(self, node_new):
        if self.head is None:
            self.add_head(node_new)
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node_new
    def delete_tail(self):
        current = self.head
        if self.head is None:
            raise Exception("Linked list is empty")
        elif self.head.next is None:
            self.head = self.next_ = None
        else:
            while current.next.next is not None:
                current = current.next
            current.next = None
    def delete_head(self):
        if self.head is None:
            raise Exception("No head")
        new_head = self.head.next
        self.head.next = None
        self.head = new_head
    def insert_after(self, node, node_new):
        if self.head is None:
            raise Exception("Linked list is empty")
        current = self.head
        while current != node and current is not None:
            current = current.next
        if current is None:
            raise Exception(f"Cannot find {node}")
        node_new.next = current.next
        current.next = node_new
    def insert_before(self, node, node_new):
        if self.head is None:
            raise Exception("Linked list is empty")
        elif self.head == node:
            self.add_head(node_new)
        elif self.head != node and self.head.next is None:
            raise Exception(f"Cannot find {node}")
        else:
            current = self.head
            while current.next.next != node and current.next.next is not None:
                print(current)
                current = current.next
            if current.next.next is None:
                raise Exception(f"Cannot find {node}")
            node_new.next = current.next.next
            current.next = node_new
    def delete(self, node):
        cur = self.head
        while cur.next != node and cur.next is not None:
            cur = cur.next
        if cur.next is None:
            raise Exception("Node doesn't exist")
        cur.next = node.next
    def __str__(self):
        ret = "["
        cur = self.head
        while cur is not None:
            ret += str(cur)
            cur = cur.next
            if cur is not None:
                ret += ", "
        ret += "]"
        return ret
