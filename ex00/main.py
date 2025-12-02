from ft_matrix import Vector, Matrix


def main():
    print("\n**Vector Init Tests**\n")
    v0 = Vector[int]([])
    v1 = Vector[int]([0,1,2])
    v2 = Vector[float]([1,2.5,3.89])

    print(f'{v0} {v1} {v2}')

    try:
        v3 = Vector[int]([100,145],[78,44])
    except:
        print("Error")

    print("\n*Vector operation tests*\n")
    v_tmp = Vector(v1.data.copy())
    v1.add(v2)
    print(f"\n{v1} \nOperation: {v_tmp.data} + {v2.data}")

    v_tmp = Vector(v1.data.copy())
    v1.sub(v2)    
    print(f"\n{v1} \nOperation: {v_tmp.data} - {v2.data}")

    v_tmp = Vector(v2.data.copy())
    scalar = -10
    v2.scl(scalar)
    print(f"\n{v2} \nOperation: {v_tmp.data} * {scalar}")

    #Edge cases
    print("\n **Edge Cases**\n")
    v3 = Vector[float]([10,25,389,42])
    try:
        v3.sub(v1)
    except:
        print("Error")

    print("\n**Matrix Init Tests**\n")
    m0 = Matrix[int]([])
    m1 = Matrix[int]([[5,5,4,4],[8,8,5,5],[56,44,78,99]])
    m2 = Matrix[int]([[50,50,40,40],[80,80,50,50],[560,440,780,990]])
    print(f"{m0} {m1} {m2}")

    print("\n*Matrix Operation Tests*\n")
    #add
    m_tmp = Matrix(m1.data.copy())
    m1.add(m2)
    print(f"{m1} \nOperation: {m_tmp} + {m2}\n\n")
    #sub
    m_tmp = Matrix(m1.data.copy())
    m1.sub(m2)
    print(f"{m1} \nOperation: {m_tmp} - {m2}\n\n")

    #scl
    m_tmp = Matrix(m1.data.copy())
    m1.scl(scalar)
    print(f"{m1} \nOperation: {m_tmp} * {scalar}\n")

    #test with different shapes
    try:
        m3 = Matrix[int]([[60,70],[80,90],[50,40]])
        m1.add(m3)
    except:
        print("Error")

if __name__=="__main__":
    main()