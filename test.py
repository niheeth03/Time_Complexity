# This program takes a user input of numbers and performs various operations on them using loops

import random

# Ask user for input of numbers
n=int(input())
m=3
num_list = [2]

c=(n+m)*3

for i in range(0,n):
    num_list.append(int(input()))

# Print the list of numbers
print("List of numbers:", num_list)

# For loop: Print the square of each number in the list
print("Squares of each number in the list:")
for num in num_list:
    print(num**2)

# While loop: Print the largest number in the list
largest_num = num_list[0]
i = 1
while i < len(num_list):
    if num_list[i] > largest_num:
        largest_num = num_list[i]
    i += 1
print("Largest number in the list:", largest_num)

# Do-while loop: Calculate the average of the numbers in the list
total_sum = 0
count = 0
while count<m:
    for num in num_list:
        total_sum += num
        count += 1
average = total_sum / count
print("Average of numbers in the list:", average)

# Nested loops: Generate a multiplication table of the numbers in the list
print("Multiplication table:")
for i in num_list:
    for j in range(1, 11):
        print(i, "x", j, "=", i*j)

# Random number generation using a for loop
random_list = []
for i in range(10):
    random_list.append(random.randint(1, 100))
print("Random list of numbers:", random_list)

# List comprehension using a while loop
squares_list = []
i = 0
while i < len(num_list):
    squares_list.append(num_list[i]**2)
    i += 1
print("Squares of each number in the list (using list comprehension):", squares_list)
