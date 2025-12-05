from ft_matrix import Vector, Matrix
import math
from typing import TypeVar
    

def main():
    """let u = Matrix::from([
[1., 0.],
[0., 1.],
]);
let v = Vector::from([4., 2.]);
println!("{}", u.mul_vec(&v));
// [4.]
// [2.]
let u = Matrix::from([
[2., 0.],
[0., 2.],
]);
let v = Vector::from([4., 2.]);
println!("{}", u.mul_vec(&v));
// [8.]
// [4.]
let u = Matrix::from([
[2., -2.],
[-2., 2.],
]);
let v = Vector::from([4., 2.]);
println!("{}", u.mul_vec(&v));
// [4.]
// [-4.]"""
    u = Matrix[int]([[1,0],[0,1]])
    v = Vector[int]([4,2])
    print(u.mul_vec(v))
    u = Matrix[int]([[5,6],[7,8]])
    u.mul_mat(v)
if __name__=="__main__":
    main()