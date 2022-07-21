 bilet = 0
while True:
    try:
        bilet_number = input('Сколько билетов вы хотите приобрести на мероприятие? ')
        bilet_number = int(bilet_number)
        if type(bilet_number) == int:
            break
    except ValueError:
        print('Введите целое число')
for i in range(bilet_number):
    i += 1
    while True:
        try:
            age = input(f'Для какого возраста билет №{i}? ')
            age = int(age)
            if age < 18:
                print('Билет бесплатный')
            elif 25 > age >= 18:
                bilet += 990
                print('Стоимость билета: 990 руб.')
            else:
                bilet += 1390
                print('Стоимость билета: 1390 руб.')
            if type(age) == int:
                break
        except ValueError:
            print('Введите целое число')
if bilet_number > 3:
    bilet = bilet - ((bilet / 100) * 10)
    print(f'Сумма к оплате {bilet} руб. с учетом 10%-ой скидки на полную стоимость заказа за регистрацию больше 5-и человек')
else:
    print(f'Сумма к оплате {bilet} руб.')
