from heapq import heapify, heappush, heappop
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) <= len(self.minHeap):
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        if len(self.minHeap) == 0 or len(self.maxHeap) == 0:
            return

        if self.minHeap[0] < -self.maxHeap[0]:
                sm = -heappop(self.minHeap)
                lg = -heappop(self.maxHeap)
                heappush(self.minHeap, lg)
                heappush(self.maxHeap, sm)
        

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2 
        return -self.maxHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
