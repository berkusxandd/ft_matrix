from ft_matrix import Vector, Matrix
import math
from typing import TypeVar
    
def main():
    u = Matrix[float]([[10,20,30],[40,50,60],[70,80,90]])
    print(f"{u.transpose()} Answer = [10,40,70] [20,50,80] [30,60,90]")

    u = Matrix[float]([[10,20],[30,40],[50,60]])
    print(f"{u.transpose()} Answer = [10,30,50] [20,40,60]")

if __name__=="__main__":
    main()