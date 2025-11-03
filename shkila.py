import math
print("===ПРОГРАММА ДЛЯ РЕШЕНИЯ 3 ЗАДАЧ===")
print("Выберите номер задачи(1,2 или 3)")

while True:
    print("\n***МЕНЮ***")
    print("1 - Задача с радиацией")
    print("2 - Задача про числа")
    print("3 - Задача про отрезки")
    print("0 - Выйти из программы")
    dota = input("Ваш выбор - ")
    if dota =="1":
        print("ЗАДАЧА НОМЕР 1")
        period = 8
        Q0=2
        Q1 = 0.15
        step = 5
        print(f"Начальная мощность: {Q0} р/ч")
        print(f"Период полураспада: {period} дней")
        print(f"Ищем, когда мощность упадет до {Q1} р/ч")
        print("Расчет по дням:")
        formula = math.log(2)/period
        days = 0

        while True:
            vova = Q0*math.exp(-formula*days)
            print(f"Через{days} дней: {vova:.3} р/ч")
            if vova<=Q1:
                break
            days+=step
        print(f"Ответ:{days} дней\n")



    elif dota == "2":
        print("ЗАДАЧА 2.")
        print("Найдём наименьшее положительное число K, где K^2>N")
        while True:
            try:
                N = int(input("Введи целое число N - "))
                if N>0:
                    break
                else:
                    print("Введи значение N>0")
            except:
                print("Введи целое число!")

        K = 1
        print(f"Ищем K для N={N}")

        while True:
            dota2 = K * K
            print(f"K = {K}, K^2 ={dota2}")

            if dota2 > N:
                break
            K += 1
            print(f"Ответ: K = {K}\n")


    elif dota == "3":
        print("ЗАДАЧА 3")
        print("Найдём свободное место на отрезке A")
        while True:
            try:
                A = int(input("Введите целое число A:"))
                B = int(input("Введите целое число B:"))
                if A>0 and B>0:
                    if A>B:
                        break
                    else:
                        print("A должно быть больше B")
                else:
                    print("Числа должны быть положительными!")
            except:
                print("Введи нормальные числа!")

        print(f"Отрезок A ={A}, B={B}")

        c = 0
        dota3 = A
        while dota3>=B:
            dota3-=B
            c+=1
            print(f"Поместился отрезок B, осталось{dota3:.2f}")

        print(f"Всего поместилось отрезков - {c}")
        print(f"\n ОТВЕТ: Свободная часть {dota3:.2f}")

    elif dota == "0":
        print("До новых встреч!")
        break








