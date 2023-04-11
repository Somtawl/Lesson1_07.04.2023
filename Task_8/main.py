hight = int(input("Задайте высоту шоколадки "))
width = int(input("Задайте ширину шоколадки "))
parts = int(input("Сколько честей шоколадеи нужно отделить ? "))
if parts <= hight*width:
    if parts == hight*width or parts%hight == 0 or parts%width == 0:
        print("Делим")
    else:
        print("Так поделить не получится")
else:
    print("В шоколадке нет столько частей")