# File: main.py
import calculator
result = calculator.add(5, 3)  # Returns 8
print("Addition : ",result)
# Or using specific imports
from calculator import multiply
result = multiply(5, 3)  # Returns 15
print("Multiply : ",result)