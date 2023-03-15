def alphabetize_lists(list1, list2):
    new_list = [] # Initialize a new list.
    new_list.extend(list1) # Combine the lists.
    new_list.extend(list2)
    new_list.sort() # Sort the combined lists.
    return new_list 

keluarga_1 = ["Sani", "Emma", "Uli", "Niar", "Imam"]
keluarga_2 = ["Loika", "Gabi", "Ahmadi", "Soraya Sani"]

print(alphabetize_lists(keluarga_1, keluarga_2))

