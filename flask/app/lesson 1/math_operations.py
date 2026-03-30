# Without __name__ == __main__ 


def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

print("Addition:", add(5, 3))
print("Multiplication:", multiply(5, 3))

# With __name__ == __main__ 

# def add(a, b):
#     return a + b

# def multiply(a, b):
#     return a * b

# if __name__ == "__main__":
#     print("Addition:", add(5, 3))
#     print("Multiplication:", multiply(5, 3))