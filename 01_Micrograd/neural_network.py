from main import Value
import random

class Neuron:
    def __init__(self, n_inp):
        self.w = [random.uniform(-1,1) for _ in range(n_in)]
        self.b = 0
        
    def parameters(self):
        pass
    
# will do later ...