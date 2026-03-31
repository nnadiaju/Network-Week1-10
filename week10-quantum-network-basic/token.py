import time

class Token:
    def __init__(self, message):
        self.message = message
        self.read = False
        self.timestamp = time.time()

    def read_token(self):
        if self.read or time.time() - self.timestamp > 10:
            return None
        self.read = True
        return self.message