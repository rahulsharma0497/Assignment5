def findTheDistanceValue(arr1, arr2, d):
    distance_value = 0
    for num1 in arr1:
        found = False
        for num2 in arr2:
            if abs(num1 - num2) <= d:
                found = True
                break
        if not found:
            distance_value += 1

    return distance_value
