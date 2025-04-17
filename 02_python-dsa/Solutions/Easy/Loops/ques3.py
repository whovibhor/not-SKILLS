# Calculate the sum of numbers from 1 to 100 using a loop also it should show each sum individually to check progress.

number = 1
sum_of_numbers = 0
while number <= 10000000:
    sum_of_numbers += number
    print(f"Sum after adding {number} is {sum_of_numbers}")
    number += 1