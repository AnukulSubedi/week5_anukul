from _math_functions import ffi, lib

# Call the compiled C functions
result_add = lib.add(4545, 3535)
result_multiply = lib.multiply(52, 58)

print(f"Add: 4545 + 3535 = {result_add}")
print(f"Multiply: 52 * 58 = {result_multiply}")