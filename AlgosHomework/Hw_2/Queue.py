class Queue:
    def __init__(self):
        self.items = []

    def push(self, n):
        self.items.append(n)
        return 'ok'
    def pop(self):
        if len(self.items) < 1:
            return "error"
        return self.items.pop(0)
    
    def front(self):
        if len(self.items) < 1:
            return "error"
        return self.items[0]
    
    def size(self):
        return len(self.items)
    
    def clear(self):
        self.items.clear()
        return 'ok'
    
    def exit(self):
        return 'bye'
    

def main():
    dec = Queue()

    while True:
        command = input().strip().split()

        cmd = command[0]

        if cmd == 'push':
            n = command[1]
            print(dec.push(n))
        elif cmd == 'pop':
            print(dec.pop())
        elif cmd == 'front':
            print(dec.front())
        elif cmd == 'size':
            print(dec.size())
        elif cmd == 'clear':
            print(dec.clear())
        elif cmd == 'exit':
            print(dec.exit())
            break

if __name__ == "__main__":
    main()
