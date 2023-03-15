

def sum_divisors(number):
# Initialize the appropriate variables
  divisor = 1
  total = 0

  # Hindari membagi dengan 0 dan angka negatif 
  # dalam perulangan perulangan dengan keluar dari fungsi
  # jika "jumlah" kurang dari satu
  if number < 1:
    return 0 

  # Complete the while loop
  while divisor < number:
    if number % divisor == 0:
      total += divisor
    # Increment the correct variable
    divisor += 1

  # Return the correct variable 
  return total


print(sum_divisors(0)) # Harus print 0
print(sum_divisors(3)) # Harus print 1
# 1
print(sum_divisors(36)) # Harus print 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Harus print 1+2+3+6+17+34+51
# 114
