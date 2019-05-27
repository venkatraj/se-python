def binary_search(target, given_list):
    low = 0
    high = len(given_list)
    while low <= high:
        midpoint = (high - low) // 2 + low
        if target == given_list[midpoint]:
            return midpoint
        elif target > given_list[midpoint]:
            low = midpoint + 1
        else:
            high = midpoint - 1
