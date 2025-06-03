def one(nums, k):
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n+1):
            current_sum = sum(nums[i:j])
            if current_sum == k:
                count += 1
    return count

def two(nums, k):
    n = len(nums)
    count = 0
    prefix = [0] * (n+1)
    for i in range(1, n+1):
        prefix[i] = prefix[i-1] + nums[i-1]

    for i in range(n):
        for j in range(i+1,n+1):
            if prefix[j] - prefix[i] == k:
                count += 1
    return count

def three(nums, k):
    prefix = {0:1}
    count = 0
    current_sum = 0
    for i in range(len(nums)):
        current_sum += nums[i]
        if current_sum not in prefix:
            prefix[current_sum] = 1
        else:
            prefix[current_sum] += 1

        if current_sum - k in prefix:
            count += prefix[current_sum-k]

    return count
