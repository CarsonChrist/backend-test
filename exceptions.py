# Class for creating the negative point exception implemented in point_tracker.py
class NegativePointException(Exception):
    def __init__(self):
        super().__init__("Negative Points Exception")