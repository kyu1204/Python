from datetime import datetime


# class Character:
#     def __init__(self, name):
#         self.name = name
#         self.hp = 100
#         self.mp = 100
#
#     def status(self):
#         print(self.name)
#         print(f"hp: {self.hp}")
#         print(f"mp: {self.mp}")
#
#
# class Server:
#     def __init__(self, name):
#         self.name = name
#         self.max_channel = 10000000
#         self.channel = []
#
#         for idx in range(self.max_channel):
#             self.channel.append([idx + 1, []])
#
#         # self.channel = {}
#
#     def join(self, character, channel_num):
#         for channel in self.channel:
#             if channel[0] == channel_num:
#                 channel[1].append(character.name)
#
#     def status(self):
#         for channel in self.channel:
#             print(f"{channel[0]} 채널: {channel[1]}")
#
#
# naro = Character("zi존나로")
# naro.status()
#
#
# server_create_time = datetime.now()
# scania = Server("스카니아")
# print(datetime.now() - server_create_time)
#
# server_join_time = datetime.now()
# scania.join(naro, 9899999)
# print(datetime.now() - server_join_time)


class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.mp = 100

    def status(self):
        print(self.name)
        print(f"hp: {self.hp}")
        print(f"mp: {self.mp}")


class Server:
    def __init__(self, name):
        self.name = name
        self.max_channel = 10000000
        self.channel = {}

        for idx in range(self.max_channel):
            self.channel[idx + 1] = []

    def join(self, character, channel_num):
        if channel_num in self.channel:
            self.channel[channel_num].append(character.name)

    def status(self):
        for key, value in self.channel.items():
            print(f"{key} 채널: {value}")


naro = Character("zi존나로")
naro.status()


server_create_time = datetime.now()
scania = Server("스카니아")
print(datetime.now() - server_create_time)

server_join_time = datetime.now()
scania.join(naro, 1)
print(datetime.now() - server_join_time)
