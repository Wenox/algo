# Follow-up: what if no strictly increasing values guarantee?
# Hint: Use SortedList, bisect_left and bisect_right to compute window size.
from collections import deque


class RecentCounter:

    def __init__(self):
        self.timestamps = deque()

    def ping(self, t: int) -> int:
        self.timestamps.append(t)

        bound = t - 3000
        while self.timestamps[0] < bound:
            self.timestamps.popleft()

        return len(self.timestamps)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)