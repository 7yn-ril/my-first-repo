def greet(name):
    print(f"Hello, {name}!")
    
greet("World")

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

print("--------ADD---------")

add_a = int(input("Enter a number: "))
add_b = int(input("Enter another number: "))

addresult_c = add(add_a, add_b)

print(f"{add_a} + {add_b} = {addresult_c}")
