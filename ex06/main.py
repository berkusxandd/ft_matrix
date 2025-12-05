from ft_matrix import Vector, cross_product
import math
from typing import TypeVar
    

def main():
  
    u = Vector[int]([0,0,1])
    v = Vector[int]([1,0,0])
    print(f"{cross_product(u,v)} Answer = [0,1,0]")

    u = Vector[int]([1,2,3])
    v = Vector[int]([4,5,6])
    print(f"{cross_product(u,v)} Answer = [-3,6,-3]")

    u = Vector[int]([4,2,-3])
    v = Vector[int]([-2,-5,16])
    print(f"{cross_product(u,v)} Answer = [17,-58,-16]")
if __name__=="__main__":
    main()