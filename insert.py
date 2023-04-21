# Import the signin function from authentication.py

from authentication import signin

# Call the signin function to authenticate the user

while not signin():
    pass

# Get the student's data from user input

id = input("Enter the student ID: ")
name = input("Enter the student name: ")
age = int(input("Enter the student age: "))
location = input("Enter the student location: ")

# Open the text file for appending and write the data

with open('students.txt', 'a') as f:
    f.write(f'{id}\t{name}\t{age}\t{location}\n')
