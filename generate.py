import os
import random
from datetime import date
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(description="Generate passkeys and save them to files.")
parser.add_argument("--num-passkeys", type=int, default=10, help="Number of passkeys to generate")
parser.add_argument("--output-dir", default="generate", help="Output directory for saving generated files")
args = parser.parse_args()

# Retrieve command line arguments for number of passkeys and output directory
number_of_passkeys = args.num_passkeys  # Number of passkeys to generate
output_dir = args.output_dir  # Output directory

try:
    # Initialize list of users
    users = []  

    # Define User class with id, passkey, and status attributes
    class User:
        def __init__(self, id, status):
            self.id = int(id)
            self.passkey = random.randint(100000, 999999)
            self.status = int(status)

    # Generate users with unique passkeys
    for i in range(number_of_passkeys):
        user = User(i, 0)
        users.append(user)

    # Get the current date and format it
    today = date.today()
    formatted_date = today.strftime("%d-%m-%Y")

    # Define paths for the date folder, ids file, and passkeys folder
    date_folder_path = os.path.join(output_dir, formatted_date)
    ids_file_path = os.path.join(date_folder_path, 'ids.txt')
    passkeys_folder_path = os.path.join(date_folder_path, 'passkeys')

    # Create date folder if it doesn't exist
    if not os.path.exists(date_folder_path):
        os.makedirs(date_folder_path)

    # Write user ids, passkeys, and status to ids file
    with open(ids_file_path, 'w') as f:
        for i in range(number_of_passkeys):
            f.write(f"{users[i].id},{users[i].passkey},{users[i].status}\n")

    # Create passkeys folder if it doesn't exist
    if not os.path.exists(passkeys_folder_path):
        os.makedirs(passkeys_folder_path)

    # Write each user's passkey to a separate file in the passkeys folder
    for i in range(number_of_passkeys):
        passkey_file_path = os.path.join(passkeys_folder_path, f'key{i}.txt')
        with open(passkey_file_path, 'w') as f:
            f.write(f"Passkey: {users[i].passkey}")

    print("Passkeys generated and saved successfully.")

except Exception as e:
    print(f"An error occurred: {e}")
