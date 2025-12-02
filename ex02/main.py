from ft_matrix import Vector, Matrix, linear_combination, lerp
import math
from typing import TypeVar
    
def main():
    v1 = Vector[int]([2,1])
    v2 = Vector[int]([4,2])
    
    v = lerp(v1,v2,0.3)
    print(f'{v} [2.6, 4.3]')
    v = lerp([21],[42],0.3)
    
if __name__=="__main__":
    main()