def find_max_min(arr):

    min_value = arr[0]
    max_value = arr[0]
    for x in arr:
        if x < min_value:
            min_value = x
        elif x == min_value:
            min_value = x


        if x > max_value:
            max_value = x
        elif x == max_value:
            max_value = x

    if max_value == min_value:
        results = [min_value]
    else:
        results = [min_value , max_value]
    return results
