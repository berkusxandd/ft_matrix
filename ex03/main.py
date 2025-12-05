from ft_matrix import Vector, Matrix, linear_combination, lerp
import math
from typing import TypeVar
    

def main():

    u = Vector[float]([0,0])
    v = Vector[float]([1,1])
    print(f"{u.dot(v)} Answer = 0.0")

    u = Vector[float]([1,1])
    v = Vector[float]([1,1])
    print(f"{u.dot(v)} Answer = 2")


    u = Vector[float]([-1,6])
    v = Vector[float]([3,2])
    print(f"{u.dot(v)} Answer = 9")

    u = Vector[float]([89,-655,42])
    v = Vector[float]([154,732,10])
    print(f"{u.dot(v)} Answer = -465334")

    v = Vector[float]([154,732,10,88])
    try:
        u.dot(v)
    except:
        print("Error")

if __name__=="__main__":
    main()