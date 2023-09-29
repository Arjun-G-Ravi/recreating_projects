class Value:
    def __init__(self, val):
        self.val = val
        self.grad = 0

    def __repr__(self):
        return f'<Value Object> val={self.val} grad={self.grad}'
    
    def __add__(self,other):
        return Value(self.val + other.val)
    
    def __mul__(self, other):
        return Value(self.val * other.val)

    def relu(self):
        return Value(max(0, self.val))


if __name__ == '__main__':
    val_obj = Value.relu(Value(10) + Value(-11) * Value(2))
    print(val_obj)
