a = 10
b = 3

hasil = a + b
print(a, '+', b, '=', hasil)

hasil = a - b
print(a, '-', b, '=', hasil)

hasil = a * b
print(a, '*', b, '=', hasil)

hasil = a / b
print(a, '/', b, '=', hasil)

hasil = a ** b
print(a, '**', b, '=', hasil)

hasil = a % b  # sisa bagi
print(a, '%', b, '=', hasil)

hasil = a // b  # pembulatan hasil bagi
print(a, '//', b, '=', hasil)

# prioritas operasi
# urutan 1. dalam kurung 2. exponen** 3. perkalian 4. pertambahan

x = 3
y = 2
z = 4

hasil = x + y + z / 2 - 1 ** 3 * 2 / 3
print('x + y + z / 2 - 1 ** 3 * 2 / 3', '=', hasil)

hasil = (x + y) * z
print(hasil)
