def sort(list):
    if len(list) == 0:
        return list
    pivot = list[0]
    pivots = [x for x in list if x == pivot]
    small = sort([x for x in list if x < pivot])
    large = sort([x for x in list if x > pivot])
    return small + pivots + large
