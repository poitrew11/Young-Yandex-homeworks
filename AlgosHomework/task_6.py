def time_to_seconds(time_str):
    parts = time_str.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    return hours * 3600 + minutes * 60 + seconds

def find_first_valid_train(trains, target_time):
    left, right = 0, len(trains)
    while left < right:
        mid = (left + right) // 2
        if trains[mid]['dep_time'] >= target_time:
            right = mid
        else:
            left = mid + 1
    return left if left < len(trains) else -1

N = int(input())
trains_1_to_2 = []
for _ in range(N):
    train = input().split()
    trains_1_to_2.append({
        'id': train[0],
        'dep_time': time_to_seconds(train[1]),
        'arr_time': time_to_seconds(train[2]),
        'cost': int(train[3])
    })

M = int(input())
trains_2_to_3 = []
for _ in range(M):
    train = input().split()
    trains_2_to_3.append({
        'id': train[0],
        'dep_time': time_to_seconds(train[1]),
        'arr_time': time_to_seconds(train[2]),
        'cost': int(train[3])
    })

trains_2_to_3.sort(key=lambda x: x['dep_time'])

best_route = None
best_criteria = (float('inf'), float('inf'), float('inf'))
max_wait = 720

for t1 in trains_1_to_2:
    idx = find_first_valid_train(trains_2_to_3, t1['arr_time'] + 900)
    if idx == -1:
        continue
    for i in range(idx, len(trains_2_to_3)):
        t2 = trains_2_to_3[i]
        if t2['dep_time'] > t1['arr_time'] + 900 + max_wait:
            break
        total_cost = t1['cost'] + t2['cost']
        criteria = (total_cost, t2['arr_time'], t1['dep_time'])
        if criteria < best_criteria:
            best_criteria = criteria
            best_route = {'id1': t1['id'], 'id2': t2['id']}

if best_route:
    print(f"{best_route['id1']} {best_route['id2']}")
else:
    print("No valid route")
