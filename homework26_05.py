import random

# Problem 1.
# Write a program that asks the user for weight in kilograms and converts it to pounds.
# There are 2.2 pounds in a kilogram

kg = float(input("kg "))
pound = 2.2 * kg
print(pound)

# Problem 2
# Write a program that generates and prints 50 random integers, each between 3 and 6.

for i in range(50):
	i = random.randint(3, 6)
	print(i)

# Problem 3
# Write a program that asks the user to enter two numbers, x, and y, and computes | x − y | /  x+y.

x = int(input("enter a number x "))
y = int(input("enter a number y "))
result = abs(x - y) / (x + y)
print(result)

# Problem 4
# A year is a leap year if it is divisible by 4,
# except that years divisible by 100 are not leap years unless they are also divisible by 400.
# Ask the user to enter a year, and, using the // operator, determine how many leap years there have been between 1600 and that year.

year = int(input("enter a year "))
count = 0

for i in range(1600, year + 1):
	if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
		count += 1
print(count)

# Problem 5
# A number is called a perfect number if it is equal to the sum of all of its divisors, not including the number itself.
# For instance, 6 is a perfect number because the divisors of 6 are 1, 2, 3, 6, and 6 = 1 + 2 + 3. 
# As another example, 28 is a perfect number because its divisors are 1, 2, 4, 7,14, 28, and 28=1+2+4+7+14.
# However,15 is not a perfect number because its divisors are 1, 3, 5, 15, and 15 != 1 + 3 + 5. 
# Write a program that finds all four of the perfect numbers that are less than 10000.

for number in range(1, 10000):
	summ = 0
	for divisor in range(1, number):
		if number % divisor == 0:
			summ += divisor
	if summ == number:
		print(summ)