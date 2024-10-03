from cffi import FFI

ffi = FFI()

# Define the C code
ffi.set_source("_math_functions", """
    int add(int a, int b) {
        return a + b;
    }
    
    int multiply(int a, int b) {
        return a * b;
    }
""")

# Declare the C function signatures
ffi.cdef("""
    int add(int a, int b);
    int multiply(int a, int b);
""")

# Compile the C code into a Python extension
ffi.compile()

