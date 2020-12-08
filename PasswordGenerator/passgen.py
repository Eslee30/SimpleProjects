import random

# Lowercase Alphabets
alph_lower_string = "abcdefghijklmnopqrstuvwxyz"
alph_lower_list = list(alph_lower_string)

# Uppercase Alphabets
alph_upper_list = list(alph_lower_string.upper())

# Punctuations
punc_list = list("!@#$%^&*-_+=:;<,>./?~")

def generate_password():
    password = ""

    count_la = 0
    while count_la < 3:
        random_la = random.choice(alph_lower_list)
        password += random_la
        count_la += 1

    count_ua = 0
    while count_ua < 3:
        random_ua = random.choice(alph_upper_list)
        password += random_ua
        count_ua += 1

    count_n = 0
    while count_n < 3:
        random_n = str(random.randint(0,9))
        password += random_n
        count_n += 1

    count_p = 0
    while count_p < 3:
        random_p = random.choice(punc_list)
        password += random_p
        count_p += 1

    password_new = ''.join(random.sample(password, 12))
    print("Your new password is: " + password_new)

while True:
    print("\nHi, welcome to Python Password Generator!\n")
    print("--- Menu ---")
    print("1. Generate password")
    print("2. Exit\n")

    inp = input("Select menu: ")

    if inp == "1":
        generate_password()
    elif inp == "2":
        print("\nThank you. Bye!")
        break
    else:
        print("\nError. Please try again.")