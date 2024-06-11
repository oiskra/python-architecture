import itertools

class NToPowerGenerator:
    def __init__(self, a, n):
        self.a = a
        self.n = n
    
    def __iter__(self):
        self.current = 0
        return self
    
    def __next__(self):
        self.current += 1
        if(self.current >= self.n):
            raise StopIteration      
        
        return self.a ** self.current
    
    
x = NToPowerGenerator(2, 10)

for i in iter(x):
    print(i)