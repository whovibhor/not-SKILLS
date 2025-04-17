#numbers = [1, -2, 3, -4, -5, 6, 7, -8, 9, 10]

#new = [i for i in numbers if i > 0] 
#print(len(new))

# number = int(input("Enter a number: "))
# sum = 0
# for i in range(1, number + 1):
#     if i % 2 == 0:
#         sum += i
# print("Sum of even numbers from 1 to", number, "is:", sum)

# number = int(input("Enter a number: "))
# count = 1
# for i in range(1, 11):
#     i = number * count
#     count += 1
#     if count == 6 :
#         continue
#     print (i)
# your_name = input("Enter your name: ")
# rev = ""
# for i in your_name:
#     rev = i + rev
# print(rev)

# stringname = "teeterd"
# for i in stringname :
#     if stringname.count(i) == 1 :
#         print(i)
#         break

# number = 5
# count = 1
# while number > 0:
#     count = count * number
#     number -= 1
# print(count)

while True:
    enter = int(input("Enter a number: "))
    if 1 <= enter <= 10:
        print("Number is between 0 and 10")
        break
    else:
        print("Number is not between 0 and 10")

        
    