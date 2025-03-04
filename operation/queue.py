class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(self.items)

    def dequeue(self):
        if self.empty():
            return self.items.pop(0)
        return False

    def front(self):
        if self.empty():
            return self.items[0]
        return False

    def back(self):
        if self.is_empty():
            return self.items[-1]
        return False

    def size(self):
        return len(self.items)

    def is_empty(self):
        if self.items:
            return self.items
        return False



