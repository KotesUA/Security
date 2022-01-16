import datetime as dt

import requests

from Casino.Player import Player
from MT19937 import mt_seed, extract_number

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
    time_seed = player.creation_time - dt.datetime.fromtimestamp(0, dt.timezone.utc)
    # for i in range(1000):
    #     print(player.play('Lcg', 1, 1), player.money)
    mt_seed(int(time_seed.total_seconds()))
    for i in range(1000):
        num = extract_number()
        print(f'Wanted = {num}')

        num_casino = player.play('Lcg', 1, 1)
        print(f'Casino showed = {num_casino}')
