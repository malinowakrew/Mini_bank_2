#from errors import Error

class Error(Exception):
    pass

class NotEnoughFounds(Error):
    def __init__(self, message="Not enough founds on your account") -> None:
        self.message = message
        super().__init__(self.message)