# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

# letter = ""
# letter = input('Please enter a letter from the alphabet (a-z or A-Z): ')
# if letter in "aeiouAEIOU":
#   print("The letter", letter, "is a vowel")
# else:
#   print("The letter", letter, "is a consanant")


# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

# phrase = ""
# while phrase != "quit":
#   phrase = input('Please enter a word or phrase: ')
#   print("What you entered is", len(phrase), "characters long.")




# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age like this:
#      Input a dog's age: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hints:
# Use the int() function to convert the string returned from input() into an integer
# Start with an if that checks if the age is less than 3

# age = input("Input a dog's age: ")
# if int(age) < 3:
#   print(int(age) * 10)
# elif int(age) >= 3:
#   print((int(age) - 2) * 7 + 20)





# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equilateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - exactly two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle 

# tot = ""
# x, y, z = input("Enter the lengths of three sides of a triangle (separated by a space): ").split()
# x, y, z = int(x), int(y), int(z)
# if x == y and y == z:
#   tot = "equilateral"
# elif x == y or y == z or x == z:
#   tot = "isosceles"
# else:
#   tot = "scalene"
# print("A triangle with the sides of", x, y, z, "is an", tot, "triangle")


# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hints:
# The next number is found by adding the two numbers before it
# Use a while loop with a looping variable, or look into Python ranges, e.g.:
#   for n in range(50):

# n = 50
# x, y = 0, 1
# z = y 
# term = 1

# while term <= n:
#   print("term:", term, "/ number:", x)
#   z = x + y
#   x, y = y, z
#   term += 1



# exercise-06 What's the Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
#   if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

season =""
month = input('Enter a month of the year (Jan - Dec): ')
day = input('Enter the day of the month: ')
day = int(day) # i need this because input() will always read the input as a string. confusing. 

if month in ('Jan', 'Feb', 'Mar'):
  season = 'Winter'
  if month == 'Mar' and day >= 20:
    season = 'Spring'
elif month in ('Apr', 'May', 'Jun'):
  season = 'Spring'
  if month == 'Jun' and day >= 21:
    season = 'Summer'
elif month in ('Jul', 'Aug', 'Sep'):
  season = 'Summer'
  if month == 'Sep' and day >= 22:
    season = 'Fall'
else:
  season = 'Fall'
  if month == 'Dec' and day >= 21: 
    season = 'Winter'

print(month, day, "is in", season)

