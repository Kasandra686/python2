text = input("Введите слова через пробел: ")
spisok = text.split(" ")
i = 0
for el in spisok:
    i += 1
    print(f"{i}. {el[:10]}")
