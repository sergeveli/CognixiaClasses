# Using Python, write a FizzBuzz program. Accept the user's integer input. 
# For every integer between 0 and that number, add the following to a list: If a number is divisible by 3, add 'Fizz', 
# if the number is divisible by 5, add 'Buzz', 
# If the number is divisible by both 3 and 5, add 'Fizzbuzz', 
# if the number is divisible by neither, add the number itself to the list. 
# Loop over the list and print each element in that list, then print the sum of all integers and the count of Fizz, Buzz and Fizzbuzz.



# First, the user inputs an integer number, which is stored in the num variable. A list lst is also created to store the results of FizzBuzz program.
# Three variables count_fizz, count_buzz, and count_fizzbuzz are also initialized to keep track of how many times each of these words occurs in the list lst.
# Another variable sum_integers is used to keep the sum of all integers that are not divisible by 3 or 5.
# Next, a for loop runs from 1 to num (inclusive). For each integer in this range, we check if it is divisible by 3 or 5, or both.
# If it is, we append the corresponding word ("Fizz", "Buzz", or "Fizzbuzz") to the list lst, and increment the corresponding count variable.
# If it is not divisible by either 3 or 5, we append the integer itself to the list lst, and add it to the sum_integers variable.
# After the loop completes, we iterate over the list lst and print each element.
# Then, we print the count of each word(Fizz, Buzz, and Fizzbuzz), as well as the sum of all integers that are not divisible by 3 or 5.

num = int(input("Enter a number: "))
lst = []
count_fizz = count_buzz = count_fizzbuzz = sum_integers = 0

for i in range(1, num):
    if i % 3 == 0 and i % 5 == 0:
        lst.append("Fizzbuzz")
        count_fizzbuzz += 1
    elif i % 3 == 0:
        lst.append("Fizz")
        count_fizz += 1
    elif i % 5 == 0:
        lst.append("Buzz")
        count_buzz += 1
    else:
        lst.append(i)
        sum_integers += i

for i in lst:
    print(i)

print("Count of Fizz: ", count_fizz)
print("Count of Buzz: ", count_buzz)
print("Count of Fizzbuzz: ", count_fizzbuzz)
print("Sum of integers: ", sum_integers)