#Kasus Rekursi 1
def is_power_of(number, base):
    # Base case:ketika number lebih kecil dari base.
    number = number/base
    if number < base:
# If number is equal to 1, it's a power (base**0).
        return False
    else:
        return True
    return is_power_of(number, base)

print(is_power_of(8,2)) # Harus True
print(is_power_of(64,4)) # Harus True
print(is_power_of(70,10)) # Harus False


#Kasus rekursi 2
def sum_positive_numbers(n):
  sum=0
  for i in range(n):
    sum = (i+1) + sum
    
  return sum
print(sum_positive_numbers(3)) # Harus 6
print(sum_positive_numbers(5)) # Harus 15