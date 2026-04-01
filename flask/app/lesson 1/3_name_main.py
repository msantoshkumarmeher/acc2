# ============================================================
# Lesson 1 - Import Behavior Demo
# File: 3_name_main.py
# Purpose: Demonstrate what happens when another Python file is imported
# ============================================================

# Importing this module executes top-level code inside math_operations.py
# (unless protected with: if __name__ == "__main__":)
import math_operations

# This line runs after import completes
print("Program started")

