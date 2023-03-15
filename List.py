def guest_list(guests):
	for tamu  in guests:
		nama, umur, pekerjaan = tamu
		print("{} is {} years old and works as {}".format(nama, umur, pekerjaan))

guest_list([('Ken', 30, "Penyanyi"), ("Pat", 35, 'Peramu Obat'), ('Amanda', 25, "Apoteker")])
