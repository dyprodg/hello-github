# Python code
import os
import argparse

def greet(first_name, last_name):
    return f"Hello, from GithubAction {first_name} {last_name}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Greet someone.')
    parser.add_argument('first_name', type=str, help='The first name of the person to greet.')
    parser.add_argument('last_name', type=str, help='The last name of the person to greet.')
    args = parser.parse_args()

    print(greet(args.first_name, args.last_name))