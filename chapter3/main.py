MAX_SIZE = 30
phone_book = []


def display(action):
    if action == "menu":
        print("--- 메뉴 ---")
        print("1. 전화번호 목록")
        print("2. 전화번호 등록")
        print("3. 전화번호 삭제")
        print("4. 전화번호 수정")
        print("5. 종료")

        try:
            c = int(input(": "))
        except ValueError:
            print("정수만 입력할 수 있습니다.")
            return 0

        return c

    elif action == "end":
        print("프로그램이 종료됩니다.")

    else:
        print(f"{action} 완료되었습니다.")


def list_phone_book(pb):
    for i in range(len(pb)):
        print(f"번호: {i}")
        print(f"이름: {pb[i][0]}")
        print(f"전화 번호: {pb[i][1]}")


def add_phone_book():
    if len(phone_book) == MAX_SIZE:
        print("더이상 저장할 수 없습니다")
    name = input("이름 : ")
    phone_number = input("번호 : ")
    return [name, phone_number]


def validation_phone_book_index(pb):
    try:
        idx = int(input("수정할 번호: "))
    except ValueError:
        print("정수만 입력할 수 있습니다.")
        return ""

    try:
        pb[idx]
    except IndexError:
        print("수정할 연락처가 없습니다.")
        return ""

    return idx


def update_phone_book():
    try:
        idx = int(input("수정할 번호: "))
    except ValueError:
        print("정수만 입력할 수 있습니다.")
        return False

    try:
        phone_book_info = []
        phone_book_info[0] = input("이름: ")
        phone_book_info[1] = input("전화번호: ")
        phone_book[idx] = phone_book_info
    except IndexError:
        print("수정할 연락처가 없습니다.")
        return False

    return True


while True:
    choice = display("menu")

    if choice == 1:  # 목록
        list_phone_book(phone_book)

    if choice == 2:  # 등록
        phone_book.append(add_phone_book())
        display(action="등록")

    if choice == 3:  # 삭제
        index = int(input("삭제할 번호: "))
        phone_book.pop(index)
        display(action="delete")

    if choice == 4:  # 수정
        if not update_phone_book():
            continue

        display("update")

    if choice == 5:  # 종료
        display("end")
        break
