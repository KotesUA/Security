import datetime
import datetime as dt

import requests

from Casino.Player import Player
from MT19937 import MT19937

URL = 'http://95.217.177.249/casino'
LAST_ID = 1197
M = 2 ** 32


def connect():
    pass


def lcg_crack():
    pass


def mt_crack():
    pass


if __name__ == '__main__':
    player = Player.register()
    # time_seed = player.creation_time - dt.datetime.fromtimestamp(0, dt.timezone.utc)



    # generator = MT19937(int(time_seed.total_seconds()))
    # for i in range(100):
    #     num = generator.extract_number()
    #     # print(f'Wanted = {num}')
    #
    #     num_casino = player.play('Mt', 1, 1)
    #     # print(f'Casino showed = {num_casino}')
    #
    #     if num == num_casino:
    #         print('Win')

    values = [int(player.play('Lcg', 1, 1)['realNumber']) for _ in range(3)]
    print(values)
    delta1, delta2 = values[1] - values[0], values[2] - values[1]

    # https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
    mod_inverse = pow(delta1, M - 2, M)
    print(mod_inverse)

    a = (delta2 * mod_inverse) % M
    b = (delta1 * a) % M
    print(f'A={a}, B={b}')

    val = int(player.play('Lcg', 1, 1)['realNumber'])
    num = (a * val + b) % M
    print(num)
    print(player.play('Lcg', 999, num))
    if player.money < 1000000:
        num = (a * val + b) % M
        print(player.play('Lcg', player.money, num))


