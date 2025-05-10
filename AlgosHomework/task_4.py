def build_segment_tree(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
        return
    mid = (start + end) // 2
    build_segment_tree(arr, tree, 2 * node + 1, start, mid)
    build_segment_tree(arr, tree, 2 * node + 2, mid + 1, end)
    tree[node] = max(tree[2 * node + 1], tree[2 * node + 2])

def update_segment_tree(tree, node, start, end, index, value):
    if start == end:
        tree[node] = value
        return
    mid = (start + end) // 2
    if index <= mid:
        update_segment_tree(tree, 2 * node + 1, start, mid, index, value)
    else:
        update_segment_tree(tree, 2 * node + 2, mid + 1, end, index, value)
    tree[node] = max(tree[2 * node + 1], tree[2 * node + 2])

def query_segment_tree(tree, node, start, end, index, x):
    if start >= index and tree[node] >= x:
        if start == end:
            return start + 1
        mid = (start + end) // 2
        if tree[2 * node + 1] >= x:
            result = query_segment_tree(tree, 2 * node + 1, start, mid, index, x)
            if result != -1:
                return result
        return query_segment_tree(tree, 2 * node + 2, mid + 1, end, index, x)
    return -1

def get(M, index, x, first, tree, n):
    if index < 0 or index >= len(M):
        return -1
    return query_segment_tree(tree, 0, 0, n - 1, index, x)

def update(M, index, value, tree, n):
    if index <= len(M) and value >= 0:
        M[index] = value
        update_segment_tree(tree, 0, 0, n - 1, index, value)

N = list(map(int, input().split()))
n = N[0]
M = list(map(int, input().split()))

tree = [0] * (4 * n)
build_segment_tree(M, tree, 0, 0, n - 1)

for _ in range(N[1]):
    Q = input().split()
    if Q[0] == '0':
        index = int(Q[1]) - 1
        value = int(Q[2])
        update(M, index, value, tree, n)
    if Q[0] == '1':
        index = int(Q[1]) - 1
        x = int(Q[2])
        first = index - 1 
        print(get(M, index, x, first, tree, n))
