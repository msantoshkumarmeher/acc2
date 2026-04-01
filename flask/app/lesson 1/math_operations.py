# ============================================================
# Lesson 1 - Why __name__ == "__main__" Is Important
# File: math_operations.py
# Purpose: Show that top-level code runs during import
# ============================================================

# Functions are reusable when imported into another file.
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


# These lines execute immediately, even during import.
print("Addition:", add(5, 3))
print("Multiplication:", multiply(5, 3))

# Better approach: wrap run-only code in if __name__ == "__main__"

# def add(a, b):
#     return a + b

# def multiply(a, b):
#     return a * b

# if __name__ == "__main__":
#     print("Addition:", add(5, 3))
#     print("Multiplication:", multiply(5, 3))