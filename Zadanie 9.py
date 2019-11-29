try:
    with open('Zadanie_8.txt', 'r') as shoping_list, open('Zadanie_9.txt', 'w') as out_file:
        data = shoping_list.read()
        out_file.write(data)
except IOError as ioe:
    print(ioe)
