from datetime import datetime, timezone

from connector import create_account, play
from classes import PlayMode, Account, PlayResult
from mtimpl import MT19937Gen
from mtcrack import MTCrack


M = (2 ** 32) // 2
ACC_LASTID = 35698


def try_create_acc(last_id):
    if last_id is None:
        last_id = 0
    acc: Account = None
    while acc is None:
        acc = create_account(last_id)
        if acc is None:
            print(f'ID {last_id} exists, skipping...')
        last_id += 1
    return acc


def solve_lcg(account_id: int) -> int:
    from sympy import mod_inverse
    inp = [play(PlayMode.LCG, account_id, 1, 42).real_number for _ in range(3)]
    print(inp)
    x1, x2, x3 = inp
    mi = mod_inverse(x2 - x1, M)
    a = ((x3 - x2) * mi) % M
    c = (x2 - x1 * a) % M
    print(f'a = {a}; c = {c}')
    return x3


def LCG_crack():
    acc = try_create_acc(ACC_LASTID)
    account_id = acc.id
    a = 1664525
    c = 1013904223
    x = play(PlayMode.LCG, account_id, 1, 42).real_number

    def next():
        return (x * a + c) % M

    while acc.money <= 1000000:
        x = next()
        print(f'Playing {x}')
        result = play(PlayMode.LCG, account_id, 900, x)
        print(result)
        acc = result.account


def MT_crack():
    acc = try_create_acc(ACC_LASTID)

    account_id = acc.id

    dt = acc.get_creation_time() - datetime.fromtimestamp(0, timezone.utc)
    seed = int(dt.total_seconds())
    print(f'Seed: {seed}')

    local_rng = MT19937Gen(seed)

    while acc.money <= 1000000:
        expected = local_rng.next()
        result: PlayResult = play(PlayMode.MT, account_id, 900, expected)
        print(result)
        acc = result.account


def MT_BETTER_crack():
    acc = try_create_acc(ACC_LASTID)
    account_id = acc.id

    inputs = []
    for i in range(624):
        res = play(PlayMode.BETTER_MT, account_id, 1, 42)
        acc = res.account
        inputs.append(res.real_number)
        print(f'Playing {i + 1}/624; balance: {acc.money}...')

    cracked_rng = MTCrack(inputs).make_rng()

    while acc.money <= 1000000:
        expected = cracked_rng.next()
        bet = acc.money - 1
        result: PlayResult = play(PlayMode.BETTER_MT,
                                  account_id, bet, expected)
        print(result)
        acc = result.account


if __name__ == '__main__':

    LCG_crack()
    # Yay! https://docs.google.com/document/d/1jhf3P6Iob5fxN4EkM9illeYgAnzwmaCJ2SbSkzpftH4/edit

    # MT_crack()
    # Yay! It's different from the first one: https://docs.google.com/document/d/1_W00GZXLNTk6BML6jEaAJDqwMVjaQUv5WL1DCW7ipy4/edit

    # MT_BETTER_crack()
    # Yay! The last one: https://docs.google.com/document/d/121efoh98-uQQdgpz1fc_Zu27SiNLzib1o2Ah_sr5f1Y/edit?usp=sharing
