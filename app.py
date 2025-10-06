import time
print("Hello, World!")
print("This is a sample Python application.")


def greet(name):
    return f"Hello, {name}! Welcome to the Python world.This message is generated using a function."

print(greet("Asha"))

print("Simulating a long-running process...")
time.sleep(2)
print("Process completed.")
print("Goodbye!")