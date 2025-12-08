from ft_matrix import Vector, Matrix
import math
from typing import TypeVar
    
def main():
    u = Matrix[float]([[1,0],[0,1]])
    print(f"{u.trace()} Answer = 2.0")

    u = Matrix[float]([[2,-5,0],[4,3,7],[-2,3,4]])
    print(f"{u.trace()} Answer = 9.0")

    u = Matrix[float]([[-2,-8,4],[1,-23,4],[0,6,4]])
    print(f"{u.trace()} Answer = -21.0")

    try:
        u = Matrix[float]([[-2,-8,4],[1,-23,4],[0,6,4],[45,77,44]])
        print(f"{u.trace()} Answer = -21.0")
    except:
        print("Error")
    
if __name__=="__main__":
    main()