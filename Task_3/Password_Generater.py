import random
import string

print("Please enter 'q' to quit.")

while 0 < 1:
    try:
        def generate_password(length=12):
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            return password

        if __name__ == "__main__":
            password_length = input("Enter the desired password length: ")
            if password_length.lower() == 'q':
                break
            elif int(password_length) < 8:
                print('Sorry length must be equal to or more than 8.')
            else:
                generated_password = generate_password(int(password_length))
                print("Generated Password:", generated_password)
    except ValueError:
        print('Please enter a valid number for the password length.')
