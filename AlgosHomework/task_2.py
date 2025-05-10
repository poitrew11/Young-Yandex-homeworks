class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.tree = [(float('-inf'), -1)] * (2*self.n)

        for i in range(self.n):
            self.tree[self.n + i] = (arr[i], i)

        for i in range(self.n - 1, 0, -1):
            left = self.tree[2*i]
            right = self.tree[2*i+1]
            if left[0] == right[0]:
                self.tree[i] = (left[0], min(left[1], right[1]))
            else:
                self.tree[i] = max(left, right)

    def query(self, l, r):
        l += self.n
        r += self.n + 1
        res = (float('-inf'), -1)
        if l > r or l < 0 or r < 0:
            raise ValueError('Invalid Range')
        while l < r:
            if l % 2 == 1:
                res = self._combine(res, self.tree[l])
                l += 1
            if r % 2 ==1:
                r -=1
                res = self._combine(res, self.tree[r])
            l //=2
            r //=2
        return res

    def _combine(self, a, b):
        if a[0] == b[0]:
            return(a[0], min(a[1], b[1]))
        return max(a, b)
    
N = int(input())
M = list(map(int, input().split()))
K = int(input())

seg_tree = SegmentTree(M)
russ = []

for _ in range(K):
    Q = list(map(int, input().split()))
    left, right = Q[0] - 1, Q[1] - 1 
    result = seg_tree.query(left, right)
    russ.append((result[0], result[1] + 1))

for max_val, index in russ:
    print(f"{max_val} {index}")
