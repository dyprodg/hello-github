# Python code
import os

def greet():
    name = os.getenv('NAME', 'GitHub Copilot')
    return f"Hello, from GithubAction {name}"

print(greet())

