def findOriginalArray(changed):
    if len(changed) % 2 != 0:
        return []  # If the length is odd, it can't be a doubled array

    original = []
    elements = set(changed)
    for num in changed:
        if num * 2 not in elements:
            return []  # If the element's double is not present, it's not a doubled array
        elements.remove(num * 2)
        original.append(num)

    return original
