from sympy import mod_inverse
from Casino.Player import Player
from MT19937 import MT19937
import datetime as dt

URL = 'http://95.217.177.249/casino'
LAST_ID = 1197
M = (2 ** 32) // 2


def lcg_crack(player):
    n1, n2, n3 = [player.play('Lcg', 1, 1)['realNumber'] for _ in range(3)]

    # https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
    # mod_inverse = pow(delta1, M - 2, M)

    # https://www.kite.com/python/answers/how-to-calculate-modular-multiplicative-inverse-in-python
    a = ((n3 - n2) * mod_inverse((n2 - n1), M)) % M
    b = (n2 - n1 * a) % M
    print(f'A={a}, B={b}')

    val = player.play('Lcg', 1, 1)['realNumber']
    num = (a * val + b) % M

    while player.money <= 1000000:
        print(player.play('Lcg', player.money, num))
        num = (a * num + b) % M


def mt_crack(player):
    time_seed = player.creation_time - dt.datetime.fromtimestamp(0, dt.timezone.utc)

    generator = MT19937(int(time_seed.total_seconds()))
    while player.money <= 1000000:
        num = generator.extract_number()
        print(player.play('Mt', player.money, num))


if __name__ == '__main__':
    player = Player.register()

    lcg_crack(player)

    # mt_crack(player)
