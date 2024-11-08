def initializing():
    global delit, del_quant, delit_str, summa, symb, quant, base
    delit = 1 # Количество делителей анализируемого числа
    del_quant = 0
    delit_str = (
        ""  # Строка, куда добавляются все делители анализируемого числа через пробел
    )
    summa = 0  # Сумма цифр анализируемого числа
    symb = []  # Все цифры, которые есть в анализируемом числе
    quant = []  # Сколько раз встречается конкретная цифра в анализируемом числе
    base = [10, 2, 8, 16]  # Базы систем счисления, которые нам нужны в этой программе
def pro_int(
    numb,
):  # Функция, определяющая, введено ли число, и если введено число, то в какой системе счисления
    for i in base:  # Перебираем базы систем счисления из списка base
        try:  # Пытаемся перевести строку в число
            if i == 10:
                # Если предполагаем, что строка-аргумент функции - это число в 10-й
                # системе счисления
                # Возможно, пользователь ввел дробное число. Чтобы из дробного числа не
                # сделать целое и не нарушить дальнейшую работу калькулятора, пытаемся
                # преобразовать через float, чтобы не потерять дробную часть
                return float(numb)  # Пытаемся преобразовать через float
            else:  # Если предполагаем, что строка-аргумент функции - это число НЕ в 10-й
                # системе счисления:
                return int(numb, i)  # Пытаемся преобразовать, предполагая, что
                # строка-аргумент это число во 2-й, 8-й либо
                # 16-й системе счисления
        except ValueError:  # Если при этом проходе цикла перевести число не удалось
            pass  # Пропускаем, предполагая,
            # Что при следующем проходе цикла (если он будет) получится перевести
    return "0"  # Если перевести не получилось (иначе говоря, не введено число во 2-й, 8-й, 10-й
    # либо в 16-й системе счисления
    # Возвращаем нуль в виде строки (он нужен для того, чтобы программа распознала  его как знак
    # неудачной попытки перевода и запросила число у пользователя еще раз)
def greet():
    # Объяснения по работе программы
    print(
        """Чтобы воспользоваться калькулятором, вводите первое число в любой системе счисления,
        затем вводите необходимый знак операции, затем вводите второе число в любой системе счисления""")
    print(
        """Если операция требует только одного числа,
        после ввода знака операции программа перейдет к вычислению.""")
    print(
        "Калькулятор переводит оба числа в десятичную систему, в какой системе счисления они не были бы введены."
        )
    print(
        """Обратите внимание, в анализе числа делители находятся для ближайшего целого числа, меньшего текущего числа
    (если оно не является целым). Если же введенное число целое, делители находятся для числа, которое ввел пользователь."""
        )
    print("Справка по знакам:")
    print("+ сложение, требует 2 чисел")
    print("- вычитание, требует 2 чисел")
    print("* умножение, требует 2 чисел")
    print("/ деление, требует 2 чисел")
    print("// деление нацело, требует 2 чисел")
    print("% остаток от деления, требует 2 чисел")
    print("** возведение в степень, требует 2 чисел")
    print("sqrt квадратный корень, требует 1 числа")
    print("dec перевод из любой системы счисления в десятичную, требует 1 числа")
    print("analyze анализ числа, требует 1 числа")
def int_division():
    if y == 0:  # Проверяем, не делят ли на ноль
        print("На ноль не делят.")
    else:  # Если не делят
        print(
            str(x), "//", str(y), "=", str(x // y)
            )  # Делим нацело, выводим результат
def add():
    print(str(x), "+", str(y), "=", str(x + y))  # Складываем, выводим результат
def multiple():
    print(str(x), "*", str(y), "=", str(x * y))  # Умножаем, выводим результат
def division():
    if y == 0:  # Проверяем, не делят ли на ноль
            print("На ноль не делят.")
    else:  # Если не делят
        if float(x) / float(y) == int(
            float(x) / float(y)
            ):  # Если частное будет целым числом
            print(
                str(x), "/", str(y), "=", str(int(float(x) / float(y)))
            )  # Частное выводим
                # в целочисленном виде, чтобы не было лишнего нуля после точки
        else:  # Если частное не будет целым числом
            print(
                str(x), "/", str(y), "=", str(float(x) / float(y))
            )  # Выводим частное в
                # дробном виде
def substract():
    print(str(x), "-", str(y), "=", str(x - y))  # Вычитаем, выводим результат
def remainder():
    if y == 0:  # Проверяем, не делят ли на ноль
        print("На ноль не делят.")
    else:  # Если не делят
        print(
            str(x), "%", str(y), "=", str(x % y)
        )  # Находим остаток, выводим результат
def power():
    if x == 0 and y < 0:
        print("Недопустимо использовать отрицательный показатель степени при основании степени, которое равно нулю.")
    else:
        print(
            str(x), "**", str(y), "=", str(x**y)
            )  # Возводим в степень, выводим результат
def sqrt():
    print(
        "√", str(x), "=", str(x**0.5)
        )  # Находим квадратный корень, выводим результат
def analyze():
    global summa, delit, delit_str, del_quant
    print(
            "Количество разрядов в числе "
            + str(x)
            + ": "
            + str(len(str(abs(int((x))))))
        )
        # Ищем, сколько разрядов в числе. Для этого число переводим в целочисленный тип
        # (десятые, сотые, тысячные и т.д разрядами не являются, поэтому переводом в int
        # вместе с разделительной точкой мы их опустим), также пользуемся не
        # числом, а его модулем (т.к количество разрядов является просто длиной строки,
        # которую мы преобразовали, и если будет введено отрицательное число, то минус
        # в начале числа
        # прибавит лишнюю единицу к значению длины, что даст неверный результат).
    for i in str(abs(x)):  # Для определения того, какие цифры встречаются в
            # анализируемом числе и сколько раз встречается конкретная цифра, будем
            # работать с модулем числа (тогда не придется в цикле писать код, который
            # будет отвечать за то, чтобы минус не был определен как цифра).
            # Переводим число в строку и перебираем каждый символ этого числа
        if i in symb:  # Если нам уже встретился такой символ в числе
            quant[symb.index(i)] += 1  # Увеличиваем то количество раз,
                # которое нам встретилась эта цифра на один
            summa += int(i)  # К текущей сумме цифр числа прибавляем текущую
            # цифру
        elif i not in symb and i != ".":  # Если нам в числе такой символ не
                # стречался, при этом этот символ не точка
            symb.append(i)  # Добавляем эту цифру в список тех цифр, которые нам
                # стретились в данном числе
            quant.append(1)  # В массиве, в котором указывается, сколько раз
                # встретилась конкретная цифра, добавляем цифру 1 (т.е текущее число встре
                # тилось пока 1 раз)
            summa += int(i)  # текущей сумме цифр числа прибавляем текущую цифру
    for i in symb:  # Для каждой найденной в числе цифры выводим, сколько раз
            # она в числе встретилась
        print("Цифр " + i + " в числе " + str(x) + ": " + str(quant[symb.index(i)]))
    quant.clear()  # Очищаем массив найденных в числе цифр и массив, в котором
        # указывается, сколько раз встретилась конкретная цифра (если пользователь
        # захочет проанализировать еще одно число, а массивы от прошлых данных
        # очищены не будут, в результате получатся некорректные значения)
    symb.clear()
        # Если число четное, пишем, что оно четное
    if x % 2 == 0:
        print("Число " + str(x) + " четное.")
        # Если число нечетное, пишем, что оно нечетное
    else:
        print("Число " + str(x) + " нечетное.")
        # Выводим сумму цифр в этом числе
    print("Сумма цифр в числе " + str(x) + ": " + str(summa))
        # Сбрасываем сумму (чтобы при анализе последующих чисел результаты
        # сумм цифр для этих чисел были корректными)
    summa = 0
        # Находим делители числа
    while delit <= int(abs(x)):  # Пока текущий делитель числа не
            # больше самого числа
        if int(abs(x)) % delit == 0:  # Если остатка после деления
                # числа на текущий делитель нет
                # Добавляем текущий делитель в строку со всеми делите
                # лями числа на данный момент
            delit_str += str(delit) + " "
                # Увеличиваем количество делителей числа на 1
            del_quant += 1
            # Текущий делитель увеличиваем на 1
        delit += 1
        # Если по результатам нахождения делителей число составное,
        # пишем, что число составное, выводим все его делители
    if del_quant > 2:
        print(
            "Число "
            + str(int(x))
            + " составное, делители числа "
            + str(int(x))
            + ": "
            + delit_str
        )
        # Если по результатам нахождения делителей число простое,
        # пишем, что число простое
    elif del_quant == 2:
        print("Число " + str(int(x)) + " простое.")
    elif x == 1:
        # Число 1 ни простое, ни составное, так и пишем
        print("Число 1 ни простое, ни составное.")
        # Сбрасываем значения этих переменных, для того,
        # чтобы нахождение делителей для последующих
        # анализируемых чисел было корректным
    delit_str = ""
    del_quant = 0
    delit = 1
        # Если число отрицательное или число положительное,
        # но при этом корень числа не целое число, пишем,
        # что число полным квадратом не является
    if x >= 0 and float(x**0.5) != int(x**0.5) or x < 0:
        print("Число " + str(x) + " не является полным квадратом.")
        # Если число положительное и при этом корень числа
        # целое число, пишем, что число является полным
        # квадратом
    elif x >= 0 and float(x**0.5) == int(x**0.5):
        print(
            "Число "
            + str(x)
            + " является полным квадратом числа "
            + str(int(x**0.5))
            + "."
        )
        # Т.к результатом нахождения кубического корня из
        # отрицательного числа в питоне будет комплексное
        # число, сначала находим кубический корень
        # из модуля числа. Если он целый (или не целый,
        # но находится на расстоянии не меньше 0.00000001
        # от ближайшего целого числа) и анализируемое
        # число является целым, пишем, что число
        # является полным кубом, иначе пишем, что число
        # не является полным кубом. При этом если число
        # изначально было отрицательным, умножаем
        # получившийся корень на -1.
    if x <= 0:
        if abs(
            abs(x) ** (1 / 3) * (-1) - round(abs(x) ** (1 / 3) * (-1))
        ) <= 0.00000001 and int(x) == float(x):
            print(
                "Число "
                + str(x)
                + " является полным кубом числа "
                + str(round(abs(x) ** (1 / 3) * (-1)))
                + "."
            )
        else:
            print("Число " + str(x) + " не является полным кубом.")
    elif x > 0:
        if abs(x ** (1 / 3) - round(x ** (1 / 3))) <= 0.00000001 and int(
            x
        ) == float(x):
            print(
                "Число "
                + str(x)
                + " является полным кубом числа "
                + str(round(x ** (1 / 3)))
                + "."
            )
        else:
            print("Число " + str(x) + " не является полным кубом.")
def decim():
    # Если введен знак перевода числа в число в 10-й системе счисления
    print("dec(" + dec + ") = " + str(x)) # Просто выводим результат, все уже было
        # вычислено в функции pro_int
def main():
    global dec, x, y
    answer = "да"  # Объявляем переменную, где будет храниться ответ пользователя, хочет он продолжать либо нет
# В начале должно быть да, иначе мы не сможем попасть в цикл while
    while answer != "нет" and answer == "да":  # Пока пользователь соглашается продолжать (пишет да)
        x = input("Первое число = ")  # Просим первое число
        dec = x  # Заблаговременно дублируем строку, введенную пользователем, в эту переменную (нужно для
    # того, чтобы показать, каким число было до перевода в дес.сист.счисления, для знака dec).
        x = pro_int(
            x
        )  # Пытаемся перевести введенную пользователем строку в число в 10-й системе счисления
        while x == "0":  # Пока не получится перевести введенную строку в число в 10-й системе счисления
            x = input("Еще раз. Первое число = ")  # Просим первое число
            dec = x  # Дублируем введенное пользователем (выше указано, зачем)
            x = pro_int(x)  # Пытаемся перевести введенную строку в число в 10-й сист.счисл.
        if float(x) == int(x):  # Если число целое
            x = int(
                x
            )  # Переводим число в целочисленный тип (чтобы не было лишнего нуля после точки
        # при отображении конечного результата).
        sign = input("Введите нужный знак операции. ")  # Просим знак действия
        if (
            sign != "sqrt" and sign != "dec" and sign != "analyze"
        ):  # Если введенный знак действия требует 2-х
        # чисел
            y = input("Второе число = ")  # Просим второе число
            y = pro_int(
                y
            )  # Проделываем со вторым числом все то же, что и с первым (за исключением дублирования числа,
        # знак dec требует только первое число)
            while y == "0":
                y = input("Еще раз. Второе число = ")
                y = pro_int(y)
            if float(y) == int(y):
                y = int(y)
        if sign == "+":  # Если введен знак сложения
            add()
        elif sign == "-":  # Если введен знак вычитания
            substract()
        elif sign == "*":  # Если введен знак умножения
            multiple()
        elif sign == "/":  # Если введен знак деления
            division()
        elif sign == "//":  # Если введен знак деления нацело
            int_division()
        elif sign == "%":  # Если введен знак нахождения остатка
            remainder()
        elif sign == "**":  # Если введен знак возведения в степень
            power()
        elif sign == "sqrt":  # Если введен знак нахождения квадратного корня
            sqrt()
        elif sign == "dec":
            decim()
        elif sign == "analyze":  # Если введен знак анализа числа
            analyze()
        else:  # Если введенная строка не совпадает ни
        # с одним знаком из справки знаков в начале
        # программы, пишем, что введен неверный
        # знак операции
            print("Введен неверный знак операции.")
    # Спрашиваем, хочет ли пользователь продолжить,
    # результат записываем в переменную ответа
        answer = input(
            "Хотите продолжить? Если не хотите, вводите нет (именно так), если хотите - вводите да (именно так). "
        )
    print("Удачи!")
# Если пользователь написал нет (именно так), желаем удачи
initializing()
greet()
main()
