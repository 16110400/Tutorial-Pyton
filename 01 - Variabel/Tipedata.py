# tipe data

from ctypes import c_double, c_char
data_interger = 0

print(type(data_interger))
print("data : ", data_interger)
print(" - bertipe", type(data_interger))

data_float = 0.202020

print(type(data_float))
print("data : ", data_float)
print(" - bertipe", type(data_float))

data_string = "ini string bukan ?"

print(type(data_string))
print("data : ", data_string)
print(" - bertipe", type(data_string))

data_bool = True

print(type(data_bool))
print("data : ", data_bool)
print(" - bertipe", type(data_bool))

# tipe data khusus

# 1 bilangan kompleks
data_complex = complex(5, 6)
print("data : ", data_complex)
print(" - bertipe", type(data_complex))

# 2 tipe data dari bahasa c


data_c_double = c_double(10.213123123123)
print("data : ", data_c_double)
print(" - bertipe", type(data_c_double))
