def find_max_min(arr):

    min_value = arr[0]
    max_value = arr[0]
    for x in arr:
        if x < min_value:
            min_value = x

        if x > max_value:
            max_value = x

    results = [min_value , max_value]
    return results 



print(find_max_min([8 , 9 , 10 ,1, 2]))
