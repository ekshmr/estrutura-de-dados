class StringStack:
    def __init__(self):
        super().__init__()
        self.items: list[str] = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item: str):
        self.items.append(item)
    
    def pop(self) -> str:
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

class FloatStack:
    def __init__(self):
        super().__init__()
        self.items: list[float] = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item: float):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

class IntegerStack:
    def __init__(self):
        super().__init__()
        self.items: list[int] = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item: int):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return int(self.items[len(self.items)-1])
    
    def size(self):
        return len(self.items)