# Read the data from the text file

with open('students.txt', 'r') as f:
    lines = f.read().splitlines()

# Print the header

print('Student ID\t Student Name\t Student Age\t Student Location'
      ' \n----------\t ------------\t ------------\t ---------------')

# Print the data

for line in lines:
    id, name, age, location = line.split('\t')
    print(f'{id}\t\t\t {name}\t\t\t\t {age}\t\t\t {location}')

# Print the total number of students

print(f'\nNo. of Students\t\t\t: \t{len(lines)}')

# get the lowest and highest age of students
ages = [int(line.split('\t')[2]) for line in lines]
print(f'Lowest Age of Student\t\t: \t{min(ages)}')
print(f'Highest Age of Student\t\t: \t{max(ages)}')
