def digi(num):
    if num < 100:
        return 'Not Str'
    s = str(num)
    if len(set(s)) == 1:
        return 'Tri Str'
    diff = [int(b) - int(a) for a, b in zip(s, s[1:])]
    if len(set(diff)) != 1:
        return 'Not Str'
    return diff[0]
