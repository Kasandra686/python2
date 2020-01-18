sp = [7, 5, 3, 3, 0, -2, -2, -2, -3]
new_sp = []
new_num = int(input("Введите любое число: "))
i = 0
if new_num > sp[0]:
    i += 1
    new_sp.append(str(new_num))
    new_sp = new_sp + sp
else:
    for el in sp:
        if el > new_num:
            new_sp.append(el)
        elif el == new_num:
            i += 1
            new_sp.append(el)
            if sp.count(el) == i:
                new_sp.append(str(new_num))
        else:
            if i == 0:
                i += 1
                new_sp.append(str(new_num))
            new_sp.append(el)
if i == 0:
    new_sp.append(str(new_num))
print(new_sp)
