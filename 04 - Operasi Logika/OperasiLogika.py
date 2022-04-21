# operasi logika ==> TABEL KEBENARAN
# not, or, and, xor

from re import A


print("===NOT===")
a = True
c = not a
print("data a = ", a)
print("------NOT")
print("data c = ", c)

print("===OR===")  # jika salah satu true maka hasil nya true (penjumlahan)
a = False
b = False
c = a or b
print(a, "OR", b, c)

print("===AND===")  # jika 2 buah nilai true maka hasil true (perkalian)
a = False
b = False
c = a AND b
print(a, "AND", b, c)

print("===XOR===")  # akan true jika salah satu true
a = False
b = False
c = a AND b
print(a, "XOR", b, c)
