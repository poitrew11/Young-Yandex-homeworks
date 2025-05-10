class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.tree = [0] * (2 * self.size)

        for i in range(self.n):
            self.tree[self.size + i] = 1 if arr[i] == 0 else 0
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, value):
        index -= 1 
        pos = self.size + index
        self.tree[pos] = 1 if value == 0 else 0
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]

    def range_count(self, l, r):
        l -= 1 
        r -= 1
        l += self.size
        r += self.size + 1
        res = 0
        while l < r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            if r % 2 == 1:
                r -= 1
                res += self.tree[r]
            l //= 2
            r //= 2
        return res

    def find_kth_zero(self, l, r, k):
        if self.range_count(l, r) < k:
            return -1

        l -= 1
        r -= 1
        pos = 1
        left = 0
        right = self.size - 1

        while pos < self.size:
            mid = (left + right) // 2
            left_count = self._count_range(max(left, l), min(mid, r))
            if left_count >= k:
                pos = 2 * pos
                right = mid
            else:
                k -= left_count
                pos = 2 * pos + 1
                left = mid + 1

        return left + 1 if left >= l and left <= r else -1

    def _count_range(self, l, r):
        if l > r:
            return 0
        l += self.size
        r += self.size + 1
        res = 0
        while l < r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            if r % 2 == 1:
                r -= 1
                res += self.tree[r]
            l //= 2
            r //= 2
        return res
    
N = int(input())
M = list(map(int, input().split()))
K = int(input())

seg_tree = SegmentTree(M)
russ = []

for _ in range(K):
    Q = input().split()
    if Q[0] == 's':
        l = int(Q[1])
        r = int(Q[2])
        k = int(Q[3])
        print(seg_tree.find_kth_zero(l, r, k))
    elif Q[0] == 'u':
        i = int(Q[1])
        x = int(Q[2])
        seg_tree.update(i, x)
    else:
        raise ValueError('Invalid ranges')
