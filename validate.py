import os

# Define directory and file settings
main_dir = "validate"
input_dir = "input"
output_dir = "output"
output_file = "ids_validated.txt"
input_file = "ids.txt"
input_result_file = "result.txt"
invalid_ids_file = "ids_invalid.txt"  # New file for invalid IDs

try:
    # Initialize lists for storing passkey data
    generated_passkeys = []  # List of generated passkeys
    result_passkeys = []  # List of result passkeys

    # Load generated passkeys from file
    try:
        with open(os.path.join(main_dir, input_dir, input_file)) as f:
            lines = f.readlines()
            for line in lines:
                row = line.strip().split(',')
                generated_passkeys.append({
                    "id": int(row[0]),
                    "passkey": row[1],
                    "status": int(row[2])
                })
    except FileNotFoundError:
        print("Error: ids.txt file not found in input folder.")
        exit()

    # Load result passkeys from file
    try:
        with open(os.path.join(main_dir, input_dir, input_result_file)) as f:
            lines = f.readlines()
            for line in lines:
                row = line.strip().split(',')
                result_passkeys.append(row[0])
    except FileNotFoundError:
        print("Error: result.txt file not found in input folder.")
        exit()

    validated_passkeys = []  # List of validated passkeys
    invalid_passkeys = []  # List of invalid passkeys

    # Validate passkeys and update their status
    for generated_passkey in generated_passkeys:
        if generated_passkey["passkey"] in result_passkeys:
            validated_passkeys.append(generated_passkey["passkey"])
            result_passkeys.remove(generated_passkey["passkey"])  # Remove validated passkey from result_passkeys
            generated_passkey["status"] = 1
        else:
            generated_passkey["status"] = 0

    invalid_passkeys = result_passkeys  # Remaining passkeys in result_passkeys are invalid

    # Write the validation results to a file
    try:
        with open(f"{main_dir}/{output_dir}/{output_file}", 'w') as f:
            f.write(f"{len(validated_passkeys)}/{len(generated_passkeys)} passkeys used\n\n")
            for generated_passkey in generated_passkeys:
                f.write(f"{generated_passkey['id']},{generated_passkey['passkey']},{generated_passkey['status']}\n")
    except FileNotFoundError:
        print(f"Error: Unable to write to file {output_file}.")
        exit()

    # Write the invalid passkeys to a new file
    try:
        with open(f"{main_dir}/{output_dir}/{invalid_ids_file}", 'w') as f:
            for invalid_passkey in invalid_passkeys:
                f.write(f"{invalid_passkey}\n")
    except FileNotFoundError:
        print(f"Error: Unable to write to file {invalid_ids_file}.")
        exit()

    print("Passkeys validated successfully.")

except Exception as e:
    print(f"An error occurred: {e}")
