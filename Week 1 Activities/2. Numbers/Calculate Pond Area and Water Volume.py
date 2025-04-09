import math

# Given values
radius = 84  # meters
pi = 3.14
water_per_square_meter = 1.4  # liters

# Calculate the area of the pond
pond_area = pi * (radius ** 2)

# Calculate the total amount of water in the pond
total_water = pond_area * water_per_square_meter

# Print the results
print(f"Pond Area: {pond_area} square meters")
print(f"Total Water in the Pond: {int(total_water)} liters")
