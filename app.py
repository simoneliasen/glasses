import sys
import requests
import os
import math

name = input('Your name?')
print('Hello')

def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting


r = requests.get(
    'https://stackoverflow.com/questions/32964920/should-i-commit-the-vscode-folder-to-source-control')
print(r.status_code)


# Creating a VirtualEnviroment with  vevnv
# python -m venv venv
