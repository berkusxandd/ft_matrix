from ft_matrix import Vector, Matrix, linear_combination, lerp, angle_cos
import math
from typing import TypeVar
    

def main():
    
    u = Vector[int]([1,0])
    v = Vector[int]([1,0])
    print(f"{angle_cos(u,v)} Answer = 1.0")

    u = Vector[int]([1,0])
    v = Vector[int]([0,1])
    print(f"{angle_cos(u,v)} Answer = 0.0")

    u = Vector[int]([-1,1])
    v = Vector[int]([1,-1])
    print(f"{angle_cos(u,v)} Answer = -1.0")

    u = Vector[int]([2,1])
    v = Vector[int]([4,2])
    print(f"{angle_cos(u,v)} Answer = 1.0")

    u = Vector[float]([1,2,3])
    v = Vector[float]([4,5,6])
    print(f"{angle_cos(u,v)} Answer = 0.974631846")

if __name__=="__main__":
    main()