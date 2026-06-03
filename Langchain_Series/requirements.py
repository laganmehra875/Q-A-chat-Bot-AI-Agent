# Python Dependencies Information
# 
# In Python development, package dependencies are standardly defined in a 'requirements.txt' file.
# You can install the required packages using:
#     pip install -r requirements.txt
# 

import sys

def print_requirements():
    print("Project dependencies listed in requirements.txt:")
    try:
        with open("requirements.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        try:
            with open("Langchain_Series/requirements.txt", "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("requirements.txt not found.")

if __name__ == "__main__":
    print_requirements()
