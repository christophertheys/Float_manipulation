# Float manipulation
import math
# The program will ask the user to enter a range of floats
print("\n")
user_entered_number = input("Enter 10 random numbers : ")
print("\n")
list_of_numbers = user_entered_number.split()
# This will convert the inputted values into a list
for sorted_list in range(0, len(list_of_numbers), 1):
    # Range is set for the number of characters entered into the program
    list_of_numbers[sorted_list] = float(list_of_numbers[sorted_list])
# Converting the entire list into float values
print("The sum of all numbers :", sum(list_of_numbers))
print("Index of the largest number :", list_of_numbers.index(max(list_of_numbers)))
print("Index of the smallest number :", list_of_numbers.index(min(list_of_numbers)))
# The index function will give the position of the desired maximum and minimum value within the list
average_numbers = sum(list_of_numbers) / len(list_of_numbers)
print("Average of the numbers :", round(average_numbers, 2))
median_number = (max(list_of_numbers) + min(list_of_numbers)) / 2
# The median number is calculated as the middle value within a range of numbers
print("Median number = ", median_number)
