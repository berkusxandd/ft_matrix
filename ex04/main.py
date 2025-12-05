from ft_matrix import Vector, Matrix, linear_combination, lerp
import math
from typing import TypeVar
    

def main():
    
    u = Vector[float]([0,0,0])
    print(f"{u.norm_1()} {u.norm()} {u.norm_inf()} Answer = 0.0 0.0 0.0")

    u = Vector[float]([1,2,3])
    print(f"{u.norm_1()} {u.norm()} {u.norm_inf()} Answer = 6.0, 3.74165738, 3.0")

    u = Vector[float]([-1,-2])
    print(f"{u.norm_1()} {u.norm()} {u.norm_inf()} Answer = 3.0, 2.236067977, 2.0")

if __name__=="__main__":
    main()