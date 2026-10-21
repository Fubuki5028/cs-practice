def count_items(values):
    count  = {}
    for i in values:
        count[i] = count.get(i, 0) + 1
    return count

def unique_sorted(values):
    return sorted(set(values))

def common(first, second):
    return sorted(set(first) & set(second))

def only_in_first(first, second):
    return sorted(set(first) - set(second))
