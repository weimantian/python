# 堆是一种特殊的树形数据结构。Python中的heapq模块实现的是最小堆，符合以下特征：
# 每个父节点的值都小于或等于其子节点的值。
# 堆在内存中通常通过数组来实现，满足以下关系：
# 对于任意一个节点 k，有 heap[k] <= heap[2*k + 1] 和 heap[k] <= heap[2*k + 2]。这样可以快速找到堆中的最小元素：总是在根节点 heap[0]。
import heapq

# 创建堆
heap = []

# 向堆中添加元素 heappush()
heapq.heappush(heap, 3)
heapq.heappush(heap, 5)
heapq.heappush(heap, 0)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
print(heap)
# heapdec()
print(type(heap))

# 从堆中弹出最小值
print(heapq.heappop(heap))
print(heap)

# 获取堆中的最小值
print(heap[0])
print(heap)

# 将列表转换为堆 heapify()
arr = [3, 5, 0, 1, 2]
heapq.heapify(arr)
print(arr)  # 输出: [0, 1, 5, 3, 2]

# 将堆中的最小值替换为指定值，并返回替换前的最小值 heapreplace()
result = heapq.heappushpop(heap, 4)
print(result)  # 输出: 3
print(heap)  # 输出: [4, 5]