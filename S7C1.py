class StringQueue:
    def __init__(self):
        super().__init__()
        self.items: list[str] = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item: str):
        self.items.insert(0, item)
    
    def dequeue(self) -> str:
        return self.items.pop()

    def size(self):
        return len(self.items)

class FloatQueue:
    def __init__(self):
        super().__init__()
        self.items: list[float] = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item: float):
        self.items.insert(0, item)
    
    def dequeue(self) -> float:
        return self.items.pop()

    def size(self):
        return len(self.items)

class IntegerQueue:
    def __init__(self):
        super().__init__()
        self.items: list[int] = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item: int):
        self.items.insert(0, item)
    
    def dequeue(self) -> int:
        return self.items.pop()

    def size(self):
        return len(self.items)