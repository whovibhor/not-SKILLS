# Given three numbers, find the largest one using if-elif-else.

input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))
input3 = int(input("Enter third number: "))

if input1 >= input2 and input1 >= input3:
    largest = input1
elif input2 >= input1 and input2 >= input3:
    largest = input2
else:
    largest = input3
print("The largest number is:", largest)
