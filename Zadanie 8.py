shoping_list = open('plik/Zadanie_8.txt', 'w')
shoping_list.writelines(["Bananas ", "Oranges ", "Apple "])

shoping_list.flush()

shoping_list_read = open('plik/Zadanie_8.txt', 'r')
print(shoping_list_read.read())

shoping_list_read.close()
shoping_list.close()