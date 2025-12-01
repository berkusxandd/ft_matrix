from ft_matrix import Vector, Matrix

def main():
    v1 = Vector[int]([0,1,2])
    v2 = Vector[int]([1,2,3])

    m1 = Matrix[int]([[5,5],[5,5]])
    m2 = Matrix[int]([[4,4],[4,4]])
    m1.scl(5)
    print(m1.data)

if __name__=="__main__":
    main()