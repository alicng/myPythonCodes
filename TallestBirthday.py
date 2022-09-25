def birthday_cake_candles(candles):

    return len([i for i in candles if max(candles) == i])

a=birthday_cake_candles([82, 49, 82, 82, 41, 82, 15, 63, 38, 25])
print(a)