import requests

from Casino.Player import Player

URL = 'http://95.217.177.249/casino'
LAST_ID = 1


def connect():
    pass


def lcg_crack():
    pass


def mt_crack():
    pass


if __name__ == '__main__':
    player = Player.register()
    for i in range (1000):
        print(player.play('Lcg', 1, 1), player.money)