import requests

URL = 'http://95.217.177.249/casino'

class Player:
    ID = 1132

    def __init__(self, uuid, money, deletion_time):
        self.uuid = uuid
        self.money = money
        self.deletion_time = deletion_time

    @classmethod
    def register(cls):
        url = f'{URL}/createacc'
        player: cls = None
        while player is None:
            response = requests.get(url, {'id': cls.ID})
            print(response.json(), f'ID={cls.ID}')
            if response.status_code // 100 == 2:
                player = cls(cls.ID, response.json()['money'], response.json()['deletionTime'])
                print(f'Created account; ID={player.uuid}, money={player.money}, deletion time={player.deletion_time}')
            cls.ID += 1
        return player

    def play(self, gamemode, bet, number):
        url = f'{URL}/play{gamemode}'
        response = requests.get(url, {'id': self.uuid, 'bet': bet, 'number': number})
        if response.status_code // 100 == 2:
            self.money = response.json()['account']['money']
            return response.json()['realNumber']
