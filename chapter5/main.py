"""
다음 케릭터 클래스를 참고하여 메이플 서버 클래스를 만드세요
서버 클래스는 create 라는 함수를 가지고 있어야 합니다.

"""


class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.mp = 200
        self.str = 4
        self.int = 4
        self.dex = 4
        self.luk = 4

    def status(self):
        print(self.name)
        print(self.hp)
        print(self.mp)
        print(self.str)
        print(self.dex)
        print(self.int)
        print(self.luk)

    def __del__(self):
        print(f"good bye {self.name}!")


class Server:
    def __init__(self):
        ...

    def join(self):
        ...


naro = Character(name="zl존나로")
warrior = Character(name="타락파워전사")

naro.status()
warrior.status()
