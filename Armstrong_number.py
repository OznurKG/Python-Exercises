"""
Find out if a given number is an "Armstrong Number". 
An n-digit number that is the sum of the nth powers of its digits is called an n-Armstrong number. 

Examples : 371 = 3 ** 3 + 7 ** 3 + 1**3;

9474 = 9 ** 4 + 4 ** 4 + 7 ** 4 + 4 ** 4;

93084 = 9 ** 5 + 3 ** 5 + 0 ** 5 + 8 ** 5 + 4 ** 5.

Write a Python program that; 
-takes a positive integer number from the users 
-checks the entered number if it is Armstrong, 
-consider the negative, float and any entries other than numeric values then display a warning message to the user.

"""

#First solution:

num = input("Please enter a positive integer number: ")
sum = 0
if num.isdigit() == False :  # isdigit() method returns True if all the characters are digits, otherwise False.
    print("It is not a valid entry. Don't use non-numeric, float, or negative values!")
else:
    for i in num:
        int(i)**len(num)
        sum += int(i)**len(num)
    if sum == int(num) :
        print(f"Yes, {num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")

#Second solution:

num = input("Enter a number: ")
sum = 0
temp = int(num)
if num.isdigit() == False :
    print("It is not a valid entry.")
else:
    while temp > 0:
      digit = temp % 10
      sum += digit ** len(num)
      temp //= 10
    if int(num) == sum:
      print(num,"is an Armstrong number")
    else:
      print(num,"is not an Armstrong number")

#Third solution:

while True:
    number = input("Enter a positive number: ")
    digits = len(number)
    sum = 0
    if not number.isdigit():
        print(number, "is invalid. Please enter a valid input")
    elif int(number) >= 0:
        for i in range(digits):
            sum = sum + int(number[i]) ** digits
        if sum == int(number):
            print(f"{number} is an Armstrong number")
            break
        else:
            print(f"{number} is not an Armstrong number")
            break

