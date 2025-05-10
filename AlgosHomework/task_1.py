class Node:
    def __init__(self, max_val=float('-inf'), count=0):
        self.max_val = max_val
        self.count = count

class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.tree = [Node() for _ in range(4 * self.n)]
        if self.n > 0:
            self._build(0, 0, self.n - 1)

    def _build(self, node, start, end):
        if start == end:
            self.tree[node] = Node(self.arr[start], 1)
            return
        mid = (start + end) // 2
        self._build(2 * node + 1, start, mid)
        self._build(2 * node + 2, mid + 1, end)
        left = self.tree[2 * node + 1]
        right = self.tree[2 * node + 2]
        if left.max_val == right.max_val:
            self.tree[node] = Node(left.max_val, left.count + right.count)
        else:
            self.tree[node] = left if left.max_val > right.max_val else right

    def query(self, left, right):
        if left < 0 or right >= self.n or left > right:
            raise ValueError('Invalid range')
        return self._query(0, 0, self.n - 1, left, right)
    
    def _query(self, node, start, end, left, right):
        if right < start or left > end:
            return Node(float('-inf'), 0)
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        left_node = self._query(2 * node + 1, start, mid, left, right)
        right_node = self._query(2 * node + 2, mid + 1, end, left, right)
        if left_node.max_val == right_node.max_val and left_node.max_val != float('-inf'):
            return Node(left_node.max_val, left_node.count + right_node.count)
        return left_node if left_node.max_val > right_node.max_val else right_node


N = int(input())
M = list(map(int, input().split()))
K = int(input())

seg_tree = SegmentTree(M)

results = []

for _ in range(K):
    Q = list(map(int, input().split()))
    left, right = Q[0] - 1, Q[1] - 1 
    result = seg_tree.query(left, right) 
    results.append(f"{result.max_val} {result.count}")

print(results)
