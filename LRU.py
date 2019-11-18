class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = {}
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def promote(self, node):
        temp = self.head.next
        node.next = temp
        temp.prev = node
        self.head.next = node
        node.prev = self.head

    def get(self, value):
        if value in self.dic:
            node = self.dic[value]
            self.remove(node)
            self.promote(node)
            return True
        return False

    def put(self, value):
        if value in self.dic:
            self.remove(self.dic[value])
        node = Node(value)
        self.promote(node)
        self.dic[value] = node

        if len(self.dic) > self.capacity:
            del self.dic[self.tail.prev.value]
            self.remove(self.tail.prev)

lru = LRUCache(6)
lru.put(1)
lru.put(2)
lru.put(4)
lru.put(3)
lru.put(1)
lru.put(1)
lru.put(1)
lru.put(1)
lru.put(6)
lru.put(6)
lru.put(6)
lru.put(3)
lru.put(5)
lru.put(7)
lru.put(1)
lru.put(2)
lru.put(4)
lru.put(1)
lru.put(3)

print lru.get(6)
print lru.get(1)

for value in lru.dic:
    print value