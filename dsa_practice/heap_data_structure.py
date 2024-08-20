import heapq

min_heap = []

# Add elements to the heap
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 2)
heapq.heappush(min_heap, 7)

print(min_heap[0])

# max heap
max_heap = []

heapq.heappush(max_heap, -1 * 10)
heapq.heappush(max_heap, -1 * 5)
heapq.heappush(max_heap,-1 *  3)
heapq.heappush(max_heap, -1 * 2)
heapq.heappush(max_heap, -1 * 7)

# largest element in heap is
print(-max_heap[0])