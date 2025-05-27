class Stack:
    def __init__(self):
        self.items = []

    def push(self, n):
        self.items.append(n)
        return 'ok'
    
    def pop(self):
        if not self.items:
            return 'error'
        a = self.items[-1]
        self.items.pop()
        return a
    
    def back(self):
        if not self.items:
            return 'error'
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def clear(self):
        self.items.clear()
        return 'ok'
    
    def exit(self):
        return 'bye'
    
def main():
    stack = Stack()

    while True:
        cmd = input().strip().split()

        cm = cmd[0]

        if cm == 'push':
            n = int(cmd[1])
            print(stack.push(n))
        elif cm == 'pop':
            print(stack.pop())
        elif cm == 'back':
            print(stack.back())
        elif cm == 'size':
            print(stack.size())
        elif cm == 'clear':
            print(stack.clear())
        elif cm == 'exit':
            print(stack.exit())
            break
        else:
            print("Error")

if __name__ == "__main__":
    main()
