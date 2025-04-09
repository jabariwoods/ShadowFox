# Given values
distance = 490  # meters
time_minutes = 7  # minutes

# Convert time from minutes to seconds
time_seconds = time_minutes * 60

# Calculate speed
speed = distance / time_seconds

# Print the speed without decimal points
print(f"Speed: {int(speed)} meters per second")
