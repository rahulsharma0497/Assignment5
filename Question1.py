def convert_to_2d(original, m, n):
    if len(original) != m * n:
        return []  # Return an empty 2D array if it is impossible

    result = []
    for i in range(m):
        row = original[i * n : (i * n) + n]  # Extract elements for each row
        result.append(row)

    return result
