from ft_matrix import Vector, Matrix, linear_combination, lerp
import math
from typing import TypeVar
    

"""println!("{}", lerp(0., 1., 0.));
// 0.0
println!("{}", lerp(0., 1., 1.));
// 1.0
println!("{}", lerp(0., 1., 0.5));
// 0.5
println!("{}", lerp(21., 42., 0.3));
// 27.3
println!("{}", lerp(Vector::from([2., 1.]), Vector::from(4., 2.), 0.3));
// [2.6]
// [1.3]
println!("{}", lerp(Matrix::from([[2., 1.], [3., 4.]]), Matrix::from([[20.,
10.], [30., 40.]]), 0.5));
// [[11., 5.5]
// [16.5, 22.]]"""

def main():
    print(f'{lerp(0,1,0)} - Answer: 0')
    print(f'{lerp(0,1,1)} - Answer: 1')
    print(f'{lerp(0,1,0.5)} - Answer: 0.5')
    print(f'{lerp(21,42,0.3)} - Answer: 27.3')
    print(f'{lerp(Vector([2,1]),Vector([4,2]),0.3)} - Answer: [2.6, 1.3]')
    print(f'{lerp(Matrix([[2,1],[3,4]]),Matrix([[20,10],[30,40]]),0.5)} - Answer: [[11., 5.5], [16.5, 22.]]')
    
if __name__=="__main__":
    main()