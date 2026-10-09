import string
import secrets
import os
x = int(input("How many files to be made, 0 = unlimited,"))
loop = True
directory_name = "SpamLocation"
try:
    os.mkdir(directory_name)
    print(f"Directory '{directory_name}' created successfully.")
except FileExistsError:
    print(f"Directory '{directory_name}' already exists.")
except PermissionError:
    print(f"Permission denied: Unable to create '{directory_name}'.")
except Exception as e:
    print(f"An error occurred: {e}")
CodeLocation = os.getcwd()
counter = 0
while loop:
    if x == 0:
        loop == False
    else:
        if counter == x:
            loop = False
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(30))
        location = CodeLocation + "\SpamLocation"
        fp = os.path.join(location, password)
        DataWrite = ''.join(secrets.choice(alphabet) for i in range(1000))
        with open(fp, 'x') as f:
            f.write(f"{DataWrite}")
        counter += 1
