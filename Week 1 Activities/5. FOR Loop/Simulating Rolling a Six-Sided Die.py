import random

# Simulate rolling a six-sided die 20 times
rolls = [random.randint(1, 6) for _ in range(20)]

# Count occurrences of 6 and 1
count_6 = rolls.count(6)
count_1 = rolls.count(1)

# Count occurrences of two 6s in a row
count_two_6s_in_a_row = sum(1 for i in range(len(rolls) - 1) if rolls[i] == 6 and rolls[i + 1] == 6)

# Display results
print("Rolls:", rolls)
print("Number of times 6 was rolled:", count_6)
print("Number of times 1 was rolled:", count_1)
print("Number of times two 6s were rolled in a row:", count_two_6s_in_a_row)
