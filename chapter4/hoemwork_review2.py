import math

MAX_SIZE = 30
score_book = []


def display(action, sc_book=None):
    if action == "menu":
        print("----- 메뉴 -----")
        print("1. 성적 입력")
        print("2. 종료")
        try:
            c = int(input(": "))
        except ValueError:
            print("정수만 입력할 수 있습니다.")
            return

        return c

    elif action == "grade":
        """
        scores = ["A", "B", "C", "F]
        start = 0
        end = 5
        for idx, score in enumerate(scores):
            print(f"{score_book[start:end]}: {score}")
            start = end
            if idx == 0 or idx == 1:
                end += 10
            else:
                end += 5
        """
        scores = [["A", 0.15], ["B", 0.3], ["C", 0.3], ["F", -1]]
        score_len = len(score_book)
        start = 0
        end = 0
        for score in scores:
            if score[1] < 0:
                print(f"{score_book[start:]}: {score[0]}")

            if score[1] == 0:
                continue

            if score[1] > 0:
                end = start + math.ceil(score_len * score[1])
                print(f"{score_book[start:end]}: {score[0]}")

            start = end


def score_add():
    if len(score_book) == MAX_SIZE:
        print("더이상 저장할 수 없습니다.")
        return

    score = int(input("점수 :"))
    print(score)
    if 0 <= score <= 100:
        score_book.append(score)
        print("등록이 완료되었습니다.")
    elif not score <= 100 and score >= 0:
        print("잘못 입력 하셨습니다.")
    return 0


def grade():
    score_book.sort(reverse=True)
    display("grade", score_book)


while True:
    choice = display(action="menu")
    if choice == 1:
        score_add()

    elif choice == 2:
        print("입력한 점수의 등급")
        break

    else:
        print("잘못 입력하셨습니다.")
        continue

grade()
