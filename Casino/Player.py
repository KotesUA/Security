import requests

URL = 'http://95.217.177.249/casino'

class Player:
    ID = 1100

    def __init__(self, uuid, money, deletionTime):
        self.uuid = uuid
        self.money = money
        self.deletionTime = deletionTime

    @classmethod
    def register(cls):
        url = f'{URL}/createacc'
        player: cls = None
        while player is None:
            response = requests.get(url, {'id': cls.ID})
            print(response.json())
            if response.status_code // 100 == 2:
                player = cls(cls.ID, response.json()['money'], response.json()['deletionTime'])
                print(f'Created account; ID={player.uuid}, money={player.money}, deletion time={player.deletionTime}')
            cls.ID += 1
        return player

    def play(self, gamemode):
        if gamemode == 'LCG':
            return 0
        elif gamemode == 'MT':
            return 1
