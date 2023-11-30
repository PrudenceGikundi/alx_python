def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        result = [0, 1]
        for i in range(2, n):
            result.append(result[i-1] + result[i-2])
        return result