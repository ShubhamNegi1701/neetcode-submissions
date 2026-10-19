class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # mapping keys to nodes

        self.head = ListNode() 
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        if node is not self.tail.prev:

            #removal of node
            prev = node.prev
            nxt = node.next
            prev.next = nxt
            nxt.prev = prev

            #adding node before tail
            prev = self.tail.prev
            prev.next = node
            node.prev = prev
            node.next = self.tail
            self.tail.prev = node

        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = ListNode(key, value) 
            self.cache[key] = node

            #adding node before tail
            prev = self.tail.prev
            prev.next = node
            node.prev = prev
            node.next = self.tail
            self.tail.prev = node

            #evict if grown too big
            if len(self.cache) > self.capacity:
                lru = self.head.next

                #remove from map
                del self.cache[lru.key]

                nxt = lru.next
                self.head.next = nxt
                nxt.prev = self.head
 
        else:
            node = self.cache[key]

            if node.value != value:
                node.value = value

            if node is not self.tail.prev:
                #removal of node
                prev = node.prev
                nxt = node.next
                prev.next = nxt
                nxt.prev = prev

                #adding node before tail
                prev = self.tail.prev
                prev.next = node
                node.prev = prev
                node.next = self.tail
                self.tail.prev = node




        
