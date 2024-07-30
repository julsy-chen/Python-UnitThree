class Stack:
    def __init__(self):
        self.__container = []

    @property
    def length(self):
        return len(self.__container)
    
    # make Stack objects comaptible with len()
    def __len__(self):
        return self.length
    
    def isEmpty(self):
        return self.length == 0
    
    def push(self, val):
        self.__container.append(val)

    def pop(self):
        return self.__container.pop()
    
    def peek(self):
        if self.length > 0:
            return self.__container[-1]
        else:
            return None
        
    def __str__(self):
        if self.length == 0:
            return "<>"
        elif self.length == 1:
            return f"<{self.__container[-1]}>"
        else:
            inner_text = ", ".join(map(str, self.__container))
            return f"<{inner_text}>"

# end of stack
test = Stack()
test.push("hello")
test.push("world")
test.push("my 0/10 yasuo")

print(test.peek())
test.pop()
print(test)