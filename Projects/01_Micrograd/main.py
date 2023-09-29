class Value:
    def __init__(self, val, _children=(), _op=''):
        self.val = val
        self.grad = 0
        self._prev = set(_children)  # This exists only for operations
        self._op = _op  # This exists for only operations
        self._backward = lambda: None  # an empty function

    def __repr__(self):
        return f'<Value Object> val={self.val} grad={self.grad}'
    
    def __add__(self,other):
        out = Value(self.val + other.val, (self, other), '+')
        
        def _backward():
            self.grad += out.grad
            other.grad += out.grad
        out._backward = _backward
        return out
    
    
    def __mul__(self, other):



        
        return Value(self.val * other.val)

    def relu(self):
        return Value(max(0, self.val))

    def backward(self):
        ordered_computational_graph_nodes = []
        visited = set()
        
        def traverse_computational_graph(node):
            if node not in visited:
                visited.add(node)
                print(visited)
                for child in node._prev:  # selects only op nodes
                    traverse_computational_graph(child)
                
                # recursively appends the elements in the computational graph into this array from left to right
                ordered_computational_graph_nodes.append(node)  
        
        traverse_computational_graph(self)
        print('Order:',ordered_computational_graph_nodes)
        self.grad = 1
        for node in reversed(ordered_computational_graph_nodes):
            node._backward()



if __name__ == '__main__':
    a = Value(2)
    b = Value(3)
    c = a + b  
    c.backward()
    print(a,b,c)



