# Get inputs from the user
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
location = input("Please enter your location: ")
Discipline = input("please enter your Discipline: ")

# Calculate the year in which the user was born
birth_year = 2023 - age  # Change the year accordingly

# Print information
print(f"\nHello, {name} Welcome to B~Coin Exchange!")
print(f"You are {age} years old. That means you were born in {birth_year}.")
print(f"It's interesting to know that you're from {location}.")
print(f"Your Application for Internship in B~Coin Exchange in the Department of {Discipline} has been accepted")
