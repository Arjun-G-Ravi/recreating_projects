class Value:
    def __init__(self, val):
        self.val = val
        self.grad = 0

    def __repr__(self):
        return f'<Value Object> val={self.val} grad={self.grad}'
    
if __name__ == '__main__':
    val_obj = Value(10)
    print(val_obj)
    