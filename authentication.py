def signin():

# Open the text file with stored credentials text file

    with open('credentials.txt', 'r') as f:

# Read the file split the lines

        ranges = f.read().splitlines()

# Get the username and password from user input

        user_name = input('Enter your username: ')
        pass_word = input('Enter your password: ')

# Check if the credentials are valid

        if user_name == ranges[0] and pass_word == ranges[1]:
            print("Authentication successful!")
            return True
        else:
            print("Invalid Password. Try again.")
            return False

