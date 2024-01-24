class Value:
    def __init__(self, val, _children=(), _op=''):
        self.val = val
        self.grad = 0
        self._prev = set(_children)  # This exists only for operations
        self._op = _op  # This also exists for only operations
        self._backward = lambda: None  # an empty function, but will be defined for operations

    def __repr__(self):
        return f'<Value Object: val={self.val}, grad={self.grad}>'
    
    def __add__(self,other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.val + other.val, (self, other), '+')
        
        def _backward():
            self.grad += out.grad
            other.grad += out.grad
        out._backward = _backward
        return out
    
    def __radd__(self,other):
        return self+other
    
    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.val * other.val, (self, other), '*')

        def _backward():
            self.grad += out.grad * other.val
            other.grad += out.grad * self.val
        out._backward = _backward
        return out
    
    def __rmul__(self, other):
        return self*other
    def __sub__(self,other):
        return self+(other*-1)

    def __rsub__(self, other):
        return self-other
    
    def relu(self):
        out = Value(max(0, self.val), (self,), 'relu')
        
        def _backward():
            self.grad += out.grad * (out.val > 0)
        out._backward = _backward
        return out
    
    def __neg__(self,x):
        return self*-1

    def backward(self):
        ordered_computational_graph_nodes = []
        visited = set()
        
        def traverse_computational_graph(node):
            if node not in visited:
                visited.add(node)
                for child in node._prev:  # selects only 'op' nodes as only they have children
                    traverse_computational_graph(child)
                
                # recursively appends the elements in the computational graph into this array from left to right
                ordered_computational_graph_nodes.append(node)  
        
        traverse_computational_graph(self)
        # print('Order:',ordered_computational_graph_nodes)
        self.grad = 1
        for node in reversed(ordered_computational_graph_nodes):
            node._backward()



if __name__ == '__main__':
    a = Value(2)
    print(a)