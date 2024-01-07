MAX_SIZE = 30
phone_book = []

while True:
    print("--- 메뉴 ---")
    print("1. 전화번호 목록")
    print("2. 전화번호 등록")
    print("3. 전화번호 삭제")
    print("4. 전화번호 수정")
    print("5. 종료")

    choice = int(input(": "))

    if choice == 1:  # 목록
        for i in range(len(phone_book)):
            print(f"번호: {i}")
            print(f"이름: {phone_book[i][0]}")
            print(f"전화 번호: {phone_book[i][1]}")

    if choice == 2:  # 등록
        if len(phone_book) == MAX_SIZE:
            print("더이상 저장할 수 없습니다")
        name = input("이름 : ")
        phone_number = input("번호 : ")
        phone_book.append([name, phone_number])

    if choice == 3:  # 삭제
        index = int(input("삭제할 번호: "))
        phone_book.pop(index)
        print("삭제가 완료되었습니다.")

    if choice == 4:  # 수정
        try:
            index = int(input("수정할 번호: "))
        except ValueError:
            print("정수만 입력할 수 있습니다.")
            continue

        try:
            phone_book_info = phone_book[index]
            phone_book_info[0] = input("이름: ")
            phone_book_info[1] = input("전화번호: ")
        except IndexError:
            print("수정할 연락처가 없습니다.")
            continue

        print("수정이 완료되었습니다.")

    if choice == 5:  # 종료
        print("서비스를 종료합니다 .")
        break
