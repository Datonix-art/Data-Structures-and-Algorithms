class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)
    
    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def pop(self):
        if self.items:
            return self.items.pop()
        return None
    

def is_balanced(input_str):
    stack = Stack()

    for char in input_str:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.size() == 0:
                return False
            stack.pop()
    
    return stack.size() == 0 

print(is_balanced('(()((()(()))))'))
print(is_balanced('(()'))