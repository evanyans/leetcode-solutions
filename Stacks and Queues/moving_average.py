class MovingAverage:
    # Attempted 2/22/2025
    # aha: queues! very basic!
    def __init__(self, size: int):
        self.max_size = size
        self.size = 0
        self.sum = 0
        self.queue = deque()

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.sum += val
        self.size += 1
        if self.queue and self.size > self.max_size:
            self.sum -= self.queue.popleft()
            self.size -= 1

        return self.sum / self.size
            
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
