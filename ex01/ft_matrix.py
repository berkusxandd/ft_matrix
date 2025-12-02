from typing import TypeVar, Generic, List

K = TypeVar("K")

class Vector (Generic[K]):
    def __init__(self, data: List[K]):
        self.data = data

    def __repr__(self):
        return f"Vector({self.data})"
    
    def _assertion(self, vx: "Vector[K]"):
        assert len(self.data) == len(vx.data), \
            "Two Vectors are not in the same shape"
 
    def add(self, v: "Vector[K]"):
        self._assertion(v)
        self.data = [a + b for a, b in zip(self.data, v.data)]

    def sub(self, v: "Vector[K]"):
        self._assertion(v)
        self.data = [a - b for a, b in zip(self.data, v.data)]

    def scl(self, s: K):
        self.data = [i * s for i in self.data]


class Matrix (Generic[K]):
    def __init__(self, data: List[K][K]):
        self.data = data

    def _assertion(self, mx: "Matrix[K]"):
        assert len(self.data) == len(mx.data), \
            "Two matrices are not in the same shape"
        
        for row_a, row_b in zip(self.data, mx.data):
            assert len(row_a) == len(row_b), \
               "Two matrices are not in the same shape"

    def add(self, m:"Matrix[K]"):
        self._assertion(m)
        self.data = [
            [a + b for a,b in zip(row_a, row_b)]
            for row_a, row_b in zip(self.data, m.data)
        ]

    def sub(self, m:"Matrix[K]"):
        self._assertion(m)
        self.data = [
            [a - b for a,b in zip(row_a, row_b)]
            for row_a, row_b in zip(self.data, m.data)
        ]

    def scl(self, s:K):
        self.data = [
            [i * s for i in row]
            for row in self.data
        ]

def linear_combination(vs: list[Vector], es: list[K]) -> Vector[K]:

    v_new = Vector(vs[0].data if len(vs) > 0 else [])
    v_new.scl(0)
    for v,e in zip(vs,es):
        v.scl(e)
        v_new.add(v)
    return v_new