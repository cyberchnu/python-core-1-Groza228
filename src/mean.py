def mean(number):
    sum = 0
    count = 0
    number_str = str(number)
    for i in number_str:
        n = int(i)
        sum += n
        count += 1
        mean = sum / count
    return mean

