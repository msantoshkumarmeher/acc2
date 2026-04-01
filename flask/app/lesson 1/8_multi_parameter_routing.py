from flask import Flask

# ============================================================
# Lesson 1 - Multi-Parameter Routing
# File: 8_multi_parameter_routing.py
# Purpose: Capture more than one value from the URL
# ============================================================

app = Flask(__name__)

# This route captures:
# 1) product name as string
# 2) price as integer
# Example: /product/Book/499
@app.route("/product/<name>/<int:price>")
def product(name, price):
    return f"Product: {name}, Price: {price}"

if __name__ == "__main__":
    app.run(debug=True)