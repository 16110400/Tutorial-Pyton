# macam komparasi pada operasi komperasi boolean
# > , < , >= , <= , == , != , is , is not

a = 4
b = 2

# lebih besar
hasil = a > 6
print("a > 6 = ", hasil)

# 'is' sebagai komparasi object identity
x = 5  # ini buat object
y = 7

print("nilai x = ", x, ", id = ", hex(id(x)))
print("nilai y = ", y, ", id = ", hex(id(y)))

hasil = x is y
print("x is y = ", hasil)
