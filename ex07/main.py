from ft_matrix import Vector, Matrix
import math
from typing import TypeVar
    

"""let u = Matrix::from([
[1., 0.],
[0., 1.],
]);
let v = Matrix::from([
[1., 0.],
[0., 1.],
35
Enter the Matrix An introduction to Linear Algebra
]);
println!("{}", u.mul_mat(&v));
// [1., 0.]
// [0., 1.]
let u = Matrix::from([
[1., 0.],
[0., 1.],
]);
let v = Matrix::from([
[2., 1.],
[4., 2.],
]);
println!("{}", u.mul_mat(&v));
// [2., 1.]
// [4., 2.]
let u = Matrix::from([
[3., -5.],
[6., 8.],
]);
let v = Matrix::from([
[2., 1.],
[4., 2.],
]);
println!("{}", u.mul_mat(&v));
// [-14., -7.]
// [44., 22.]"""
def main():
    u = Matrix[int]([[1,0],[0,1]])
    v = Vector[int]([4,2])
    print(f"{u.mul_vec(v)} Answer: [4, 2]")

    u = Matrix[int]([[2,0], [0,2]])
    print(f"{u.mul_vec(v)} Answer: [8, 4]")

    u = Matrix[int]([[2,-2],[-2,2]])
    print(f"{u.mul_vec(v)} Answer: [4, -4]")

    u = Matrix[int]([[1,0],[0,1]])
    v = Matrix[int]([[1,0],[0,1]])
    print(f"{u.mul_mat(v)} Answer: [1, 0] [0, 1]")
    
    v = Matrix[int]([[2,1],[4,2]])
    print(f"{u.mul_mat(v)} Answer: [2, 1] [4, 2]")

    u = Matrix[int]([[3,-5],[6,8]])
    v = Matrix[int]([[2,1],[4,2]])
    print(f"{u.mul_mat(v)} Answer: [-14, -7] [44, 22]")


    u = Matrix[int]([[44,542,78,-10],[114,-66,42,1],[10,99,66,-78]])
    v = Matrix[int]([[47,54,77],[-15,114,66],[76,-99,106],[13,-66,42]])
    print(f"{u.mul_mat(v)} Answer: [-264, 57102,47008] [9553, -5592,8916] [2987,10440,11024]")

    v = Matrix[int]([])
    try:
        u.mul_mat(v)
    except:
        print("Error")

    #v = Matrix[int]([[47,54,77],[-15,114,66,78],[76,-99,106],[13,-66,42]])
    
    
    
if __name__=="__main__":
    main()