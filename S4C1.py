class Stack:
    def __init__(self):
        super().__init__()
        self.items = [float]
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item: float | str):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def peek_str(self) -> str:
        return str(self.items[len(self.items)-1])
    
    def size(self) -> int:
        return len(self.items)