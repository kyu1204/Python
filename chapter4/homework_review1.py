add = 0
minus = 0
multiply = 0
division = 0
result = 0
while True:
    print("---- 메뉴 ----")
    print("1.덧셈")
    print("2.뺄셈")
    print("3.곱셈")
    print("4.나눗셈 ")
    print("5.종료")
    print("초기값 = 0입니다.")
    choice = int(input(": "))

    if choice == 1:  # 덧셈
        add = int(input("더할 값 : "))
        result += add
        print(result)
    if choice == 2:  # 뺄셈
        minus = int(input("뺄 값 : "))
        result -= minus
        print(result)
    if choice == 3:  # 곱셈
        multiply = int(input("곱할 값 : "))
        result *= multiply
        print(result)
    if choice == 4:  # 나눗셈
        division = int(input("나눌 값 : "))
        try:
            result /= division
            print(result)
        except ZeroDivisionError:
            print("0의 값은 나눌수 없습니다.")
    if choice == 5:  # 종료
        print("서비스를 종료합니다.")
        break
