import heapq

arr = [4, 7, 2, 9, 1, 8]
k = 3   

heap = []

for x in arr:
    heapq.heappush(heap, x)

    if len(heap) > k:
        heapq.heappop(heap)

print("Kth largest element:", heap[0])
