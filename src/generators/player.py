from src.enums.user_enums import Statuses

from src.generators.player_localization import PlayerLocalization

class Player():
    def __init__(self) -> None:
        self.result = {}
        self.reset()

    def set_status(self, status=Statuses.ACTIVE.value):
        self.result['account_status'] = status
        return self
    
    def set_balance(self, balance=0):
        self.result["balance"] = balance
        return self
    
    def set_avatar(self, avatar="https://www.google.ru/?hl=ru"):
        self.result["avatar"] = avatar

    def reset(self):
        self.set_status()
        self.set_balance()
        self.set_avatar()
        self.result["localize"] = {
            "en": PlayerLocalization('en_US').build(),
            "ru": PlayerLocalization('ru_RU').build()
        }
        return self
    
    def update_inner_generator(self, key, generator):
        self.result[key] = {"fr": generator.build()}
        return self
    
    def build(self):
        return self.result
