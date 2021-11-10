class NegativePointException(Exception):
    def __init__(self):
        super().__init__("Negative Points Exception")