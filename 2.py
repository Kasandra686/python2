sp = input("Введите список")
sp2 = []
i = 0
for el in sp:
    i += 1
    if (i % 2) != 0:
        el2 = sp[i - 1]
        if len(sp) == i:
            sp2.append(el2)
    else:
        sp2.append(el)
        sp2.append(el2)
print(sp2)
