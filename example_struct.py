from cffi import FFI

ffi = FFI()

# Load the shared library
lib = ffi.dlopen("./libstruct_example.dylib")

# Declare the C structure and function signature
ffi.cdef("""
    struct Point {
        int a;
        int b;
    };

    int distance(struct Point p1, struct Point p2);
""")

# Create two Point instances
point1 = ffi.new("struct Point *", {'a': 4, 'b': 5})
point2 = ffi.new("struct Point *", {'a': 6, 'b': 7})

# Call the distance function
result = lib.distance(point1[0], point2[0])

print(f"Distance squared between points: {result}")
