import requests

URL = 'http://95.217.177.249/casino'

class Player:
    ID = 0

    def __init__(self, uuid):
        self.uuid = self.register()

    @classmethod
    def register(cls):
        url = f'{URL}/createacc'
        response = requests.get(url, {id: uuid})
        return 0

    def play(self, gamemode):
        if gamemode == 'LCG':
            return 0
        elif gamemode == 'MT':
            return 1
