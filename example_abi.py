from cffi import FFI

ffi = FFI()

# Load the shared library
lib = ffi.dlopen("./libmath_functions.dylib")

# Declare the function signatures
ffi.cdef("""
    int add(int a, int b);
    int multiply(int a, int b);
""")

# Call the functions from the library
result_add = lib.add(5000, 4000)
result_multiply = lib.multiply(3535, 1212)

print(f"Add: 5000+4000 = {result_add}")
print(f"Multiply: 3535 * 1212 = {result_multiply}")

