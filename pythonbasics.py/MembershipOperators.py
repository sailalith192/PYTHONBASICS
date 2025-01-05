# List of fruits
friuts = ['apple','banana','orange','grape']
# Check if apple is in the list
result = 'apple' in friuts
print(result)
result = 'pineapple' not in friuts
print(result)

# Identity Operators
# Variables with the same value
name1 = "sai"
name2 = "sai"
# Check if name1 and name2 refer to different objects in memory
hey = name1 is not name2
print(hey)

# VAraibles with different values
num1 = 10
num2 = 20
# Check num1 and num2 refer to different values
result = num1 is not num2
print(result)

