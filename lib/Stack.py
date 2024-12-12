class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items if items else[]
        self.limit = limit

    def isEmpty(self):
        return len(self.items)==0

    def push(self, item):
        if len(self.items) >=self.limit:
            return OverflowError("The Stack is full")
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            raise IndexError("Peeked from the empty stack")
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        try:
            index = len(self.items) - 1 - self.items[::-1].index(target)
            return len(self.items) - 1 -index
        except:
            return -1