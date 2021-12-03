def generate_tuple(a, b):
    tuple1 = []
    for i in range(a, b+1):
        tuple1.append(i**2)
    return tuple(tuple1)


var1 = generate_tuple(1, 20)


print(var1)
print(type(var1))
