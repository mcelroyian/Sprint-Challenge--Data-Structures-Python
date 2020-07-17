class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.store = []
        self.index = 0

    def append(self, item):
        if self.size < self.capacity:
            self.store.append(item)
            self.size += 1
        else:
            self.store[self.index] = item
            self.move_index()

    def move_index(self):
        if self.index < self.capacity - 1:
            self.index += 1
        else:
            self.index = 0

    def get(self):
        return self.store