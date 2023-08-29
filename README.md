# Passkey: Passkey Generator and Validator (python version)

This project involves two Python scripts `generate.py` and `validate.py` that generate and validate passkeys. The `generate.py` script generates a certain number of passkeys, while the `validate.py` script checks these passkeys against a list of used passkeys and validates them. These scripts are perfect for events like school elections or some other elections where 1 vote per participant is important. You can pair this with Google Forms and have Passkey as an input question to validate their vote afterwards. The script gives you files that you can mass print with a passkey, these papers can be given out to participants.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The project requires Python 3.6 or higher. You can download Python from [here](https://www.python.org/downloads/).

### Installing

Download and unpack the .Zip file:

```bash
passkeys v#.#.Zip
```

Clone the GitHub repository:

```bash
git clone <repo-url>
```

Navigate to the project directory:

```bash
cd <project-directory>
```

## Usage

The project consists of two scripts: `generate.py` and `validate.py`.

### generate.py

This script generates a specified number of passkeys. Each passkey is a random six-digit number. The passkeys are saved in a file named `ids.txt` in a new directory named with the current date. Each passkey is also saved in a separate file in a `passkeys` subdirectory. These are the files you should print and hand out to participants!

You can run the script with default parameters (10 passkeys, output directory named "generate") as follows:

```bash
python generate.py
```

You can also specify the number of passkeys as command-line arguments:

```bash
python generate.py --num-passkeys 20
```

### validate.py

To validate results with the original IDs, you need to have 2 files in the input directory within the validation directory. The files have to be named ids.txt (the originally generated passkeys, and result.txt (a list of 6-digit numbers from for example Google Forms). Result.txt should be formatted like this:

```bash
123456
123456
123456
...
```

This script validates the generated passkeys against a list of passkeys in result.txt. The validation results are saved in a file named `ids_validated.txt` in the `output` subdirectory of the `validate` directory. The first line of this document will tell you how many of the ids have been used. There will also be created a file called ids_invalid.txt. This file includes a list of invalid IDs from the result.txt file.

You can run the script as follows:

```bash
python validate.py
```

## File Structure

After running the scripts, the project directory should have the following structure:

```
project-directory/
│
├── generate.py
├── validate.py
│
├── generate/ (or other name specified as output-dir)
│   ├── dd-mm-yyyy/ (current date)
│   │   ├── ids.txt
│   │   └── passkeys/
│   │       ├── key0.txt
│   │       ├── key1.txt
│   │       ├── ...
│   │       └── keyn.txt
│
├── validate/
│   ├── input/
│   │   ├── ids.txt
│   │   └── result.txt
│   └── output/
│       ├── ids_invalid.txt
│       └── ids_validated.txt
```

## Troubleshooting

If an error occurs during the execution of either script, the error message will be printed to the console. Check the error message for details.

## Authors

* Tobias Kulvik (tobias@kulvik.no)

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.
