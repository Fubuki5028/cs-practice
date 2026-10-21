def count_times(values):
    count  = {}
    for i in values:
        count[i] = count.get(item, 0) + 1
    return count

def unique_sorted(values):
    return sorted(set(values))
    
