def arr(n):
    ser = [i * '>' for i in range(1, n + 1)]
    return ser + ser[:-1][::-1] if n % 2 else ser + ser[::-1]
