distance = 120
fuel_price = 35
fuel_consumption = 15

fuel_used = distance/fuel_consumption
cost = fuel_used * fuel_price

print("distance",distance, "km.used",int(cost),"THB")