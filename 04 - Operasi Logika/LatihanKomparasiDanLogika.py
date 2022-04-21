# latihan
# membuat gabungan area rentang dari angka
# +++++++3 == == == == == ==10++++++++
inputUser = float(
    input("Masukkan angka yang bernilai \nkurang dari 3 \ndan \nlebih dari 10 :"))

isKurangDari = (inputUser < 3)
print("Kurang dari 3 : ", isKurangDari)

isLebihDari = (inputUser > 10)
print("Lebih dari 10 : ", isLebihDari)

isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukkan : ", isCorrect)

# --------3++++++++++10----------
inputUser = float(
    input("Masukkan angka yang bernilai \nkurang dari 3 \ndan \nlebih dari 10 :"))

isKurangDari = (inputUser > 3)
print("Lebih dari 3 : ", isKurangDari)

isLebihDari = (inputUser < 10)
print("Kurang dari 10 : ", isLebihDari)

isCorrect = isKurangDari and isLebihDari
print("Angka yang anda masukkan : ", isCorrect)
