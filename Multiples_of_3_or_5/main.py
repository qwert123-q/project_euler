# Initialize the sum
total_sum = 0

# Loop through all numbers below 1000
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        total_sum += i

print(f"The sum is: {total_sum}")