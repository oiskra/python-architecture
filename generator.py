import itertools

class NToPowerGenerator:
    def __init__(self, a, n):
        self.a = a
        self.n = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        pass