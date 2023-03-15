#Mencari persamaan jarak miles dan kilo meter
def convert_distance(miles):
    km = miles * 1.6 
    result = "{} sama dengan {:.1f} km".format(miles, km)
    return result


print(convert_distance(12)) # Harus: 12 miles sama dengan 19.2 km
print(convert_distance(5.5)) # Harus: 5.5 miles sama dengan 8.8 km
print(convert_distance(11)) # Harus: 11 miles sama dengan 17.6 km