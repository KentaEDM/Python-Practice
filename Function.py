def is_power_of_two(nomor):
  # Perulangan perulangan sementara ini memeriksa apakah "angka" dapat dibagi dua
  # tanpa meninggalkan sisa. Bagaimana Anda dapat mengubah perulangan while untuk
  # menghindari Python ZeroDivisionError?
  if nomor !=0:
    while nomor % 2 == 0:
      nomor = nomor / 2
  # Jika setelah dibagi dengan 2 "angka" sama dengan 1, maka "angka" adalah pangkat
  # dari 2.
  if nomor == 1:
    return True
  return False
  

# Calls to the function
print(is_power_of_two(0)) # Harus False
print(is_power_of_two(1)) # Harus True
print(is_power_of_two(8)) # Harus True
print(is_power_of_two(9)) # Harus False