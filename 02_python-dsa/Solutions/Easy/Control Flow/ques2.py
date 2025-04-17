# Take a user's age and print whether they are a child, teenager, or adult.

input_age = int(input("Enter your age: "))
if input_age < 13:
    print("You are a child.")
elif 13 <= input_age < 20:
    print("You are a teenager.")
elif 20 <= input_age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")