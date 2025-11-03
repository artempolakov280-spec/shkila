import math
print("ПРОГРАММА ДЛЯ РЕШЕНИЯ 3 ЗАДАЧ")
print("Выберите номер задачи(1,2 или 3)")
while True:
    print("***МЕНЮ***")
    print("1 - Задача с радиацией")
    print("2 - Задача про числа")
    print("3 - Задача про отрезки")
    print("0 - Выйти из программы")
    dota = input("Твой выбор - ")
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
        print(f"Ответ: понадобиться {days} дней")


    elif dota == "2":
        print("ЗАДАЧА 2. Поиск числа K")
        print("Найдём наименьшее положительное число K, где K^2>N")
        while True:
            try:
                N = int(input("Введи целое число N - "))
                if N>0:
                    break
                else:
                    print("Введи значение N>0")
            except:
                print("Введи значение больше 0!")

        K = 1
        print(f"Ищем K для N={N}")

        while True:
            dota2 = K * K
            print(f"K = {K}, K^2 ={dota2}")

            if dota2 > N:
                break
            K += 1
            print(f"Ответ: K = {K}")






