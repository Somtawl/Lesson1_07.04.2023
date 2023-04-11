ticket_number = int(input("Введите номер билета "))
if len(str(ticket_number)) == 6:
    left_sight = 0
    right_sight = 0
    index = 0
    for i in str(ticket_number):
        print("Число i = ", i, " index = ", index)
        if index < len(str(ticket_number))/2:
            left_sight = left_sight + int(i)
        else:
            right_sight = right_sight + int(i)
        index = index + 1
    print("Сумма чисел левой стороны = ", left_sight)
    print("Сумма чисел правой стороны = ", right_sight)
    if right_sight == left_sight:
        print("Сумма чисел левой и правой стороны одинаковые. Поздравляю!!!")
    else:
        print("Повезёт в другой раз")
else:
    print("Номер бидета должен сожержать 6 цифр")