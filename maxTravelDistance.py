def total_distance(fuel, fuel_usage, passengers, air_con):

    return round(fuel/(fuel_usage*(1 + 0.05*passengers)*(1 + 0.1*air_con))*100,1)


a=total_distance(36.1, 8.6, 3, True)
print(a)