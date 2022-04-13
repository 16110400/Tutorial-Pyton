# latihan 1
# program konversi suhu (temperature)


# print("Program Konversi Suhu")

# celcius = float(input("Masukkan suhu dalam celcius : "))
# print("suhu adalah: ", celcius, "c")

# # reamur
# reamur = (4/5) * celcius
# print("suhu dalam reamur adalah: ", reamur, "r")

# # fahrenheit
# fahrenheit = (9/5) * celcius + 32
# print("suhu dalam fahrenheit adalah: ", fahrenheit, "k")

# # Kelvin
# kelvin = celcius + 273
# print("suhu dalam kelvin adalah: ", kelvin, "k")

# konversi fahrenheit ke kelvin

print("PROGRAM KONVERSI FAHRENHEIT KE KELVIN")

suhu_fahrenheit = float(input("Masukkan suhu dalam fahrenheit = "))
print("suhu adalah: ", suhu_fahrenheit, " f")

# konversi ke kelvin -> reamur -> kelvin
hasil_kelvin = (suhu_fahrenheit-32) * 5/9 + 273.15
print("suhu dalam kelvin adalah : ", hasil_kelvin)
