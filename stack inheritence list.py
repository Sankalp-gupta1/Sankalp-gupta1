class Stack(list):
    def is_empty(self):
        return len(self) == 0
    
    def push(self, data):
        self.append(data)
    
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is empty")
    
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is empty")
    
    def size(self):
        return len(self)

    def insert(self, index, data):
        # Custom insert method for the Stack class
        super().insert(index, data)

s1 = Stack()
s1.insert(0, 10)  # This line is now valid
s1.push(10)
s1.push(20)
s1.push(30)
print("Top value =", s1.peek())






   

        