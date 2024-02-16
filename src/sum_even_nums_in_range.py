def sum_even_nums_in_range(start, stop):
    sum = 0
    for m in range(start, stop + 1):
        if m % 2 == 0:
            sum += m
    return sum
