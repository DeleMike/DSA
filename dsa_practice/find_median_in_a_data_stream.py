class Median:
    def __init__(self):
        self.nums = []
        
    def addNum(self, num):
       self.nums.append(num)
       
    def median(self):
        
        n = len(self.nums) - 1
        
        
        if n == -1:
            return 0
        mid = 0
        if n%2 == 0:
           mid = n//2
           return self.nums[mid]
        else:
            mid = (n // 2) + 1
            print('part one = ', (self.nums[mid - 1]))
            print('part two = ', (self.nums[mid]))
            
            ave = self.nums[mid - 1] + self.nums[mid]
            return ave / 2
    
    def printOut(self):
        print('Nums is = ', self.nums)
        
n = Median()
# n.addNum(1)
# n.addNum(2)
# n.addNum(3)
# n.addNum(4)
n.printOut()
print(n.median())

# ABOVE IS WRONG APPROACH

def __init__(self):
        # small numbers will be stored in the maxHeap
        # large numbers will be stored in the minHeap
        self.small, self.large = [], []

def addNum(self, num: int) -> None:
    if self.large and num > self.large[0]:
        heapq.heappush(self.large, num)
    else:
        heapq.heappush(self.small, -1 * num)
    
    # check if heaps are almost evenly distributed
    if (len(self.large) > len(self.small) + 1):
        val = heapq.heappop(self.large)
        heapq.heappush(self.small, -1 * val)
    elif (len(self.small) > len(self.large) + 1):
        val = -1 * heapq.heappop(self.small)
        heapq.heappush(self.large, val)

def findMedian(self) -> float:
    if len(self.small) > len(self.large):
        return -self.small[0]
    elif len(self.large) > len(self.small):
        return self.large[0]
    return ((-self.small[0]) + self.large[0])/2.0 

# time complexity for adding a number in a heap is O(log n)
# time complexity for finding median is O(1)
# space complexity for operations O(n)
