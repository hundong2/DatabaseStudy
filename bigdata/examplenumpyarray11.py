import numpy as np

def exampleCalculate():
    arrayvariable=np.array([[1,3,5],[2,4,6]])
    print("input variable a = \n{}\n".format(arrayvariable))
    print("plus element a + a\n{}".format(arrayvariable + arrayvariable))
    '''
    plus element a + a
    [[ 2  6 10]
    [ 4  8 12]]
    '''
    print("minus element a - a\n{}\n".format(arrayvariable-arrayvariable))
    '''
    minus element a - a
    [[0 0 0]
    [0 0 0]]    
    '''
    print("mul element a * a\n{}\n".format(arrayvariable*arrayvariable))
    '''
    mul element a * a
    [[ 1  9 25]
    [ 4 16 36]]
    '''
    print("div element a / a\n{}\n".format(arrayvariable/arrayvariable))
    '''
    div element a / a
    [[1. 1. 1.]
    [1. 1. 1.]]
    '''

def exampleMulMatrix():
    print("each Matrix Calculate\n")
    a = np.array([1,5,10])
    b = np.array([2,7,9])
    c = np.array([1,3])
    print("input array a, b\na={}, b={}".format(a,b))
    print("mul a*b = {}\n".format(a*b))
    print("np.dot(a,b)= {}\n".format(np.dot(a,b)))
    '''
    input array a, b
    a=[ 1  5 10], b=[2 7 9]
    mul a*b = [ 2 35 90]
    np.dot(a,b)= 127
    '''
    print("input array a, c\na={}, c={}".format(a,c))
    #print("mul a*b = {}\n".format(a*c)) ValueError: operands could not be broadcast together with shapes (3,) (2,)
    #print("np.dot(a,b)= {}\n".format(np.dot(a,c))) ValueError: shapes (3,) and (2,) not aligned: 3 (dim 0) != 2 (dim 0)

def exampleMultiDim():
    a = np.array([[2,3],[4,5]])
    b = np.array([[6,7],[8,9]])
    print("input array a\na={}\nb={}\n".format(a,b))
    print("matrix mul axb\n{}\n".format(np.dot(a,b)))
    print("axb={}\n".format(a*b))
    '''
    input array a
    a=[[2 3]
    [4 5]]
    b=[[6 7]
    [8 9]]

    matrix mul axb
    [[36 41]
    [64 73]]

    axb=[[12 21]
    [32 45]]
    '''

def exampleMultiDim2():
    a = np.array([[2,3],[4,5]])
    b = np.array([6,7])
    print("np.dot(a,b)\n{}\n".format(np.dot(a,b)))
    print("np.dot(b,a)\n{}\n".format(np.dot(b,a)))
    '''
    np.dot(a,b)
    [2,3] 
          * [6,7] = [33 59]
    [4,5]
    np.dot(b,a)
             [2,3]
    [6, 7] *        = [40 53] = [2*6+7*4, 3*6+7*5]
             [4,5]
    '''

def main():
    print("example11 linear algebra\nElement-Wise\n")
    exampleCalculate()
    exampleMulMatrix()
    exampleMultiDim()
    exampleMultiDim2()


if __name__=="__main__":
    main()