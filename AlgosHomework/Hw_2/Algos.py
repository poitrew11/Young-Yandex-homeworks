#You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

#There is at least one empty seat, and at least one person sitting.

#Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

#Return that maximum distance to the closest person.


def one(seat):
    people = (ind for ind, val in enumerate(seat) if val)
    ans = 0
    prev = None
    future = next(people)
    for ind, val in enumerate(seat):
        if val:
            prev = ind
        else:
            while future is not None and future < ind:
                future = next(people, None)
            left = float('inf') if prev is None else ind - prev
            right = float('inf') if future is None else future - ind

            ans = max(ans, min(left, right))
    return ans

def two(seat):
    n = len(seat)
    left = [n] * n
    right = [n] * n
    for i in range(len(seat)):
        if seat[i] == 1:
            left[i] = 0
        elif i > 0:
            left[i] = left[i-1] + 1
    for i in range(len(seat) - 1, -1, -1):
        if seat[i] == 1:
            right[i] = 0
        elif i < n - 1:
            right[i] = right[i+1] + 1

    for ind, val in enumerate(seat):
        if not val:
            a = max(min(left[ind], right[ind]))
    return a
