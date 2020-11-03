
test_two_loop()  # time cost for two loop: 73980
test_list_comprehension()  # time cost for list comprehension: 77105
test_bin_search()  # time cost for bin search: 56
test_dict_accessing()  # time cost for dict accessing: 22

def test_two_loop():
    data = []
    for i in range(1, 126000):
        data.append(i)
    data1 = []
    for i in range(1, 126000):
        data1.append(i)

    start_time = time.time()
    a = 0
    for item in data:
        if item in data1:
            a += 1
    time_cost = int((time.time() - start_time) * 1000)
    print(f"time cost for two loop: {time_cost}")


def test_list_comprehension():
    data = []
    for i in range(1, 126000):
        data.append(i)
    data1 = []
    for i in range(1, 126000):
        data1.append(i)

    start_time = time.time()
    a = len([item for item in data if item in data1])
    time_cost = int((time.time() - start_time) * 1000)
    print(f"time cost for list comprehension: {time_cost}")


def test_bin_search():
    from bisect import bisect_left

    data = []
    for i in range(1, 126000):
        data.append(i)
    data1 = []
    for i in range(1, 126000):
        data1.append(i)

    start_time = time.time()
    data.sort()
    a = len([item for item in data if bisect_left(data, item) != -1])
    time_cost = int((time.time() - start_time) * 1000)
    print(f"time cost for bin search: {time_cost}")


def test_dict_accessing():
    data = []
    for i in range(1, 126000):
        data.append(i)
    data1 = []
    for i in range(1, 126000):
        data1.append(i)

    start_time = time.time()
    look_up = {i: True for i in data}
    a = len([item for item in data1 if look_up.get(item, False)])
    time_cost = int((time.time() - start_time) * 1000)
    print(f"time cost for dict accessing: {time_cost}")


