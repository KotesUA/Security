import requests as r
from classes import *

domain = 'http://95.217.177.249/casino'


# Creating new account
def create_account(player_id: int):
    url = f'{domain}/createacc'
    params = {'id': player_id}
    res = r.get(url, params=params)
    with open('dump.json', 'w') as f:
        f.write(res.text)
    if res.status_code // 100 == 2:
        acc = Account.parse(res.json())
        print('New account:', acc)
        return acc


# Playing a game with params mode, ID, bet and number
def play(mode: PlayMode, player_id: int, bet: int, number: int):
    url = f'{domain}/play{mode}'
    params = {'id': player_id, 'bet': bet, 'number': number}
    res = r.get(url, params)
    if res.status_code // 100 == 2:
        return PlayResult.parse(res.json())
    else:
        print(res.json())
