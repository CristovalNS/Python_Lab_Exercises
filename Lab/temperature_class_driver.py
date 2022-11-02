from temperature_class import Temperature

print()

absolute_zero = Temperature(-273.15)

print(absolute_zero.to_celsius())
print(absolute_zero.to_fahrenheit())
print(absolute_zero.to_kelvin())
print(absolute_zero)

print()

water_boiling_point = Temperature(100)

print(water_boiling_point.to_celsius())
print(water_boiling_point.to_fahrenheit())
print(water_boiling_point.to_kelvin())
print(water_boiling_point)

print()

# Can't yet run, as there is no set_temperature function yet.

# room_temperature = Temperature(20)
# room_temperature.set_temperature(-300) # This shouldn't overwrite
#
# room_temperature.set_temperature(16)
# print(room_temperature.to_celsius()) # Output: 16
# print(room_temperature.to_fahrenheit()) # Output: 60.8
# print(room_temperature.to_kelvin())