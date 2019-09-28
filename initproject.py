# Developer: Moiseenko V.
# To count: the weight of U235 (kg), the weight of deuterium (kg), the cost of U235 ($)
#           the weight of U238 (kg), the cost of U238 ($), the weight of U235 after the half period of time
daily_energy_take_mvt = int(input())
daily_energy_take_kvt = daily_energy_take_mvt / (1000)
weight_u235_kg = daily_energy_take_kvt / 20
weight_deuterium_kg = daily_energy_take_kvt / 150
cost_u235 = weight_u235_kg * 2360
weight_u238_kg = (weight_u235_kg / 0.7) * 100
cost_u238 = weight_u238_kg * 17.3
population = int(input())
costs_per_person = cost_u238 / population
time = int(input())
weight_u235_half_life = weight_u235_kg * (2**(-((time)/ 70000000)))
print("Масса U235:", weight_u235_kg)
print("Масса U238:", weight_u238_kg)
print('Стоимость U235:', cost_u235)
print('Стоимость U238:', cost_u238)
print('Масса 235 после', time, ':', weight_u235_half_life)




