class Deq:
    def __init__(self):
        self.items = []

    def push_front_n(self, n):
        self.items.insert(0, n)
        return 'ok'
    
    def push_back_n(self, n):
        self.items.append(n)
        return 'ok'
    
    def pop_front(self):
        if not self.items:
            return 'error'
        return self.items.pop(0)
    
    def pop_back(self):
        if not self.items:
            return 'error'
        return self.items.pop()
    
    def front(self):
        if not self.items:
            return 'error'
        return self.items[0]
    
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
    deq = Deq()

    while True:
        command = input().strip().split()

        cmd = command[0]

        if cmd == 'push_front':
            n = command[1]
            print(deq.push_front_n(n))
        elif cmd == 'push_back':
            n = command[1]
            print(deq.push_back_n(n))
        elif cmd == 'pop_front':
            print(deq.pop_front())
        elif cmd == 'pop_back':
            print(deq.pop_back())
        elif cmd == 'front':
            print(deq.front())
        elif cmd == 'back':
            print(deq.back())
        elif cmd == 'size':
            print(deq.size())
        elif cmd == 'clear':
            print(deq.clear())
        elif cmd == 'exit':
            print(deq.exit())
            break

if __name__ == "__main__":
    main()
