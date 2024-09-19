import random
import string
def generate_password():
    password_length = int(input("Enter the required password length: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(password_length))
    print(f"\nYour generated password is: {password}")
generate_password()
