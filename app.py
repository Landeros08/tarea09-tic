import platform
from datetime import datetime

numbers = [4, 8, 15, 16, 23, 42]
print("Hello from a Python container!")
print("Python version:", platform.python_version())
print("Sum of numbers:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))
print("Current date:", datetime.now().strftime("%B %d, %Y"))