class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
# 1.1
l = []
for i in range(1, 6):
    l.append(i)

# 1.2
d = {}
d["one"] = 1
d["two"] = 2
d["three"] = 3
d["four"] = 4
d["five"] = 5

# 1.3
st = Stack()
for i in range(1, 6):
    st.push(i)

# 1.4
que = Queue()
for i in range(1, 6):
    que.enqueue(i)
    
# 2.1
s1 = 0
for i in range(len(l)):
    s1 += l[i]
    
print(s1)

# 2.2
s2 = 0
for key in d.keys():
    s2 += d[key]

print(s2)

# 2.3
for i in range(1, 3):
    que.dequeue()
    
for item in que.items:
    print(item)

# 2.4
for i in range(1, 3):
    st.pop()
    
for item in st.items:
    print(item)

# 3.2
n = 129
hundreds = n // 100
tens = (n // 10) % 10
ones = n % 10

print(max(hundreds, tens, ones))

# 3.3
print(min(hundreds, tens, ones))
