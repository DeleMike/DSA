class Stack:
    size = 0
    def __init__(self, size: int):
        self.size = size
        self.stack = [0] * size
        self.top = -1
    
    def print_array(self):
        print(self.stack)
        
    def push(self, data: int):
        if self.top < (self.size - 1):
            self.top += 1
            self.stack[self.top] = data
    
    def pop(self):
        if self.top != -1:    
            self.stack[self.top] = 0
            self.top -= 1
    
    def peek(self) -> int:
        return self.stack[self.top]

    def is_empty(self):
        for item in self.stack:
            if item != 0:
                return False
        return True
        
stack = Stack(4)
stack.print_array()
stack.push(23)
stack.push(33)
stack.push(53)
stack.push(53)
stack.push(53)

stack.print_array()
stack.pop()
stack.print_array()
stack.push(63)
stack.print_array()
print(stack.peek())
print(stack.is_empty())
stack.pop()
stack.pop()
stack.print_array()
print(stack.is_empty())



        
        