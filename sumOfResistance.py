def series_resistance(lst):
    total=sum(lst)
    return '{} ohm'.format(total) if total <= 1 else '{} ohms'.format(total)

a=series_resistance([0.5, 0.5])
print(a)