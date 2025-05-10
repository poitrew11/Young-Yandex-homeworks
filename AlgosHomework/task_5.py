class SegmentTreeNode:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.left = None
        self.right = None
        self.max_zeros = 0
        self.prefix_zeros = 0
        self.suffix_zeros = 0
        self.full_zeros = False


class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.root = self.build(0, self.n - 1)

    def build(self, l, r):
        node = SegmentTreeNode(l, r)
        if l == r:
            if self.arr[l] == 0:
                node.max_zeros = node.prefix_zeros = node.suffix_zeros = 1
                node.full_zeros = True
            return node
        mid = (l + r) // 2
        node.left = self.build(l, mid)
        node.right = self.build(mid + 1, r)
        self.pull_up(node)
        return node

    def pull_up(self, node):
        left = node.left
        right = node.right

        node.prefix_zeros = left.prefix_zeros
        if left.full_zeros:
            node.prefix_zeros += right.prefix_zeros

        node.suffix_zeros = right.suffix_zeros
        if right.full_zeros:
            node.suffix_zeros += left.suffix_zeros

        node.max_zeros = max(
            left.max_zeros,
            right.max_zeros,
            left.suffix_zeros + right.prefix_zeros
        )
        node.full_zeros = left.full_zeros and right.full_zeros

    def update(self, index, value):
        self._update(self.root, index, value)

    def _update(self, node, index, value):
        if node.l == node.r:
            if value == 0:
                node.max_zeros = node.prefix_zeros = node.suffix_zeros = 1
                node.full_zeros = True
            else:
                node.max_zeros = node.prefix_zeros = node.suffix_zeros = 0
                node.full_zeros = False
            return
        if index <= node.left.r:
            self._update(node.left, index, value)
        else:
            self._update(node.right, index, value)
        self.pull_up(node)

    def query(self, l, r):
        return self._query(self.root, l, r)[0]

    def _query(self, node, l, r):
        if node.r < l or node.l > r:
            return (0, 0, 0, True)

        if l <= node.l and node.r <= r:
            return (node.max_zeros, node.prefix_zeros, node.suffix_zeros, node.full_zeros)

        left_res = self._query(node.left, l, r)
        right_res = self._query(node.right, l, r)

        prefix = left_res[1]
        if left_res[3]:
            prefix += right_res[1]

        suffix = right_res[2]
        if right_res[3]:
            suffix += left_res[2]

        max_zeros = max(
            left_res[0],
            right_res[0],
            left_res[2] + right_res[1]
        )

        full = left_res[3] and right_res[3]

        return (max_zeros, prefix, suffix, full)

N = int(input())
M = list(map(int, input().split()))
st = SegmentTree(M)

res = []
Q = int(input())
for _ in range(Q):
    parts = input().split()
    if parts[0] == 'UPDATE':
        index = int(parts[1]) - 1
        value = int(parts[2])
        st.update(index, value)
    elif parts[0] == 'QUERY':
        l = int(parts[1]) - 1
        r = int(parts[2]) - 1
        res.append(st.query(l, r))

for val in res:
    print(val)
