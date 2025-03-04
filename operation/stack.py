class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        if self.items:
            return self.items
        return False

    def full(self):
        return len(self.items)

    def top(self):
        if self.items:
            return self.items.index(-1)
        return False

    def push(self, item):
        self.items.append(item)
        return item

    def pop(self):
        if self.items:
            return self.items.pop(-1)
        return False
