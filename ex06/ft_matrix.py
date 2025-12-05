from typing import TypeVar, Generic, List
import math
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
    
    def dot(self, v: "Vector[K]") -> K:
        s = 0
        self._assertion(v)
        for a,b in zip(self.data, v.data):
            s += a * b
        return s
    
    def norm_1(self):
        s = 0
        for i in range(len(self.data)):
            s += abs(self.data[i])
        return s
    
    def norm(self):
        s = 0
        for i in self.data:
            s += pow(i,2)
        return pow(s,0.5)
    
    def norm_inf(self):
        max_i = 0
        for i in self.data:
            if max_i < abs(i):
                max_i = abs(i)
        return max_i


class Matrix (Generic[K]):
    def __init__(self, data: List[K][K]):
        self.data = data

    def __repr__(self):
        return f"Matrix({self.data})"
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

def lerp(u :K,v :K,t :float):

    assert type(u) == type(v)
    if isinstance(u, (Vector, Matrix)):
        v.sub(u)
        v.scl(t)
        u.add(v)
        return u
    else:
        return (u + t * (v - u))
    
def angle_cos(u :"Vector[K]", v: "Vector[K]") -> K:
    return ((u.dot(v)) / (u.norm() * v.norm()))

def cross_product(u: "Vector[K]", v: "Vector[K]") -> Vector[K]:
    assert len(u.data) == 3 or len(v.data) == 3
    v_vector = Vector["K"]([u.data[1]*v.data[2] - u.data[2]*v.data[1],
         u.data[2]*v.data[0] - u.data[0]*v.data[2],
         u.data[0]*v.data[1] - u.data[1]*v.data[0]])

    return v_vector