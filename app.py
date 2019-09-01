import sys

print(sys.version)
print(sys.executable)

def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting

print(greet("John"))
print(greet("Corey"))


#Creating a VirtualEnviroment with  vevnv
#python -m venv venv