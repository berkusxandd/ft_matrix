from ft_matrix import Vector, linear_combination
    
def main():
    """
    let e1 = Vector::from([1., 0., 0.]);
    let e2 = Vector::from([0., 1., 0.]);
    let e3 = Vector::from([0., 0., 1.]);
    let v1 = Vector::from([1., 2., 3.]);
    let v2 = Vector::from([0., 10., -100.]);
    println!("{}", linear_combination<Vector<f32>, f32>([e1, e2, e3], [10., -2.,
    0.5]));
    // [10.]
    // [-2.]
    // [0.5]
    println!("{}", linear_combination<Vector<f32>, f32>([v1, v2], [10., -2.]));
    // [10.]
    // [0.]
    // [230.]"""


    e1 = Vector[float]([1,0,0])
    e2 = Vector[float]([0,1,0])
    e3 = Vector[float]([0,0,1])

    v1 = Vector[int]([1,2,3])
    v2 = Vector[int]([0,10,-100])
   
    v_comb = linear_combination([e1, e2, e3], [10,-2,0.5])
    print(v_comb)
    
    v_comb = linear_combination([v1, v2], [10,-2])
    print(v_comb)

    v_comb = linear_combination([v1, v2], [10])
    print(v_comb)

    
if __name__=="__main__":
    main()