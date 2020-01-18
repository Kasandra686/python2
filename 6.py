goods = []
i = 0
sp_name = []
sp_price = []
sp_quantity = []
sp_unit = []
while True:
    i += 1
    name = input("Название товара: ")
    sp_name.append(name)
    price = int(input("Цена: "))
    sp_price.append(price)
    quantity = int(input("Количество: "))
    sp_quantity.append(quantity)
    unit = input("Единица: ")
    sp_unit.append(unit)
    common = input("Продолжать ввод следующего товара да/нет?:  ")
    goods.append((i, {"название": name, "цена": price, "количество": quantity, "eд": unit}))
    if (common.lower() == "нет"):
        break
analitik = dict(название=sp_name, цена=sp_price, количество=sp_quantity, ед=sp_unit)
print(goods)
print(analitik)
