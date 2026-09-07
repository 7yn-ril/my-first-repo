"""
Name: April Lhen Paniza
Section: BSIT 4A
"""

def greet(name):
    print(f"Hello, {name}!")

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference between two numbers."""
    return a - b
    
greet("World")

print("--------ADD---------")

add_a = int(input("Enter a number: "))
add_b = int(input("Enter another number: "))

addresult_c = add(add_a, add_b)

print(f"{add_a} + {add_b} = {addresult_c}")

print("------SUBTRACT------")

sub_a = int(input("Enter a number: "))
sub_b = int(input("Enter another number: "))

subresult_c = subtract(sub_a, sub_b)

print(f"{sub_a} - {sub_b} = {subresult_c}")