import numpy as np

def example1():
    #zeros(shape, dtype=float, order='C')
    print("np.zeros(4) {}".format(np.zeros(4))) #[0. 0. 0. 0.]
    #print("np.zeros(4,4) {}".format(np.zeros(4,4))) #TypeError: Cannot interpret '4' as a data type
    print("np.zeros((4,4))\n{}\n".format(np.zeros((4,4)))) 
    '''
    np.zeros((4,4))
    [[0. 0. 0. 0.]
    [0. 0. 0. 0.]
    [0. 0. 0. 0.]
    [0. 0. 0. 0.]]
    '''
    print("np.eye(4,4) \n{}\n".format(np.eye(4,4)))
    '''
    [[1. 0. 0. 0.]
    [0. 1. 0. 0.]
    [0. 0. 1. 0.]
    [0. 0. 0. 1.]]
    '''
    print("np.ones((4,4)) \n{}\n".format(np.ones((4,4))))
    '''
    [[1. 1. 1. 1.]
    [1. 1. 1. 1.]
    [1. 1. 1. 1.]
    [1. 1. 1. 1.]]
    '''

def example2():
    #numpy 4,7,10,13,16
    print("np.arange(3,16,3): {}\n".format(np.arange(3,16,3))) 
    print("np.arange(4,16,3): {}\n".format(np.arange(4,16,3))) 
    print("np.arange(4,15,3): {}\n".format(np.arange(4,15,3)))
    print("np.arange(4,17,3): {}\n".format(np.arange(4,17,3)))
    print("np.arange(4,18,3): {}\n".format(np.arange(4,18,3)))    
    '''
    np.arange(3,16,3): [ 3  6  9 12 15]
    np.arange(4,16,3): [ 4  7 10 13]
    np.arange(4,15,3): [ 4  7 10 13]
    np.arange(4,17,3): [ 4  7 10 13 16] OK
    np.arange(4,18,3): [ 4  7 10 13 16] OK
    '''

def examplerand():
    print("random example\n")
    '''
    >>> np.random.rand(3,2)
    array([[ 0.14022471,  0.96360618],  #random
           [ 0.37601032,  0.25528411],  #random
           [ 0.49313049,  0.94909878]]) #random
    '''
    uniform_random=np.random.rand(5,4)
    print("np.random.rand(5,4){}\n".format(uniform_random))

    '''
    np.random.rand(5,4)[[0.96112589 0.02531253 0.90553193 0.61395328]
    [0.65284584 0.43079657 0.52603434 0.35748111]
    [0.02764348 0.87210643 0.21481016 0.9047538 ]
    [0.40665152 0.10483078 0.74843804 0.33739189]
    [0.36601187 0.88918341 0.6770971  0.39739344]]
    '''

    onesarray=np.ones((2,3,5))
    print("np.ones((2,3,5))\n{}\n".format(onesarray))
    '''
    np.ones((2,3,5))
    [[[1. 1. 1. 1. 1.]
    [1. 1. 1. 1. 1.]
    [1. 1. 1. 1. 1.]]

    [[1. 1. 1. 1. 1.]
    [1. 1. 1. 1. 1.]
    [1. 1. 1. 1. 1.]]]
    '''
def exampereshape():
    arrayrand=np.random.randint(1,20,size=(3,6))
    arrayreshape=np.reshape(arrayrand,(2,9))
    print("input array \n{}\n".format(arrayrand))
    print("reshape\n{}\n".format(arrayreshape))
    '''
    input array
    [[16  5  3  9  9  3]
    [10  3  3 19  5 16]
    [ 2 14  6 19 14  9]]

    reshape
    [[16  5  3  9  9  3 10  3  3]
    [19  5 16  2 14  6 19 14  9]]
    '''

def examplenumpy():
    arraynp=np.array(["red", "green", "orange"])
    arrayappend=np.append(arraynp, "black")
    print("input array\n{}\n".format(arraynp))
    print("appended array\n{}\n".format(arrayappend))
    '''
    input array
    ['red' 'green' 'orange']

    appended array
    ['red' 'green' 'orange' 'black']
    '''
def examplesort():
    arraynp=np.array([[3,4,7],
                      [13,5,6],
                      [10,11,9]])
    arraysorted=np.sort(arraynp, axis=1)
    print("input array\n{}\n".format(arraynp))
    print("sorted array\n{}\n".format(arraysorted))
    '''
    input array
    [[ 3  4  7]
    [13  5  6]
    [10 11  9]]

    sorted array
    [[ 3  4  7]
    [ 5  6 13]
    [ 9 10 11]]
    '''

def examplewhere():
    arrayvalue=np.array([[12,9,83,40],
                         [73,59,24,2],
                         [44,3,18,65]])
    print("input array\n{}\n".format(arrayvalue))
    print("np.where(arrayvalue>58)\n{}\n".format(np.where(arrayvalue>58)))
    #np.where(arrayvalue>58) (array([0, 1, 1, 2], dtype=int64), array([2, 0, 1, 3], dtype=int64))
    print("np.where(arrayvalue>60)\n{}\n".format(np.where(arrayvalue>60)))
    #np.where(arrayvalue>60) (array([0, 1, 2], dtype=int64), array([2, 0, 3], dtype=int64))

def exampleflip():
    #flitud + fliplr = flip ( not sort, just change arange up to down, left to right )
    arrayvalue=np.array([[9,6,1,15],
                         [16,11,11,2],
                         [8,17,3,5]])
    arrayflip=np.flip(arrayvalue)
    print("input value\n{}\n".format(arrayvalue))
    print("np.flip(value)\n{}\n".format(arrayflip))
    '''
    input value
    [[ 9  6  1 15]
    [16 11 11  2]
    [ 8 17  3  5]]

    np.flip(value)
    [[ 5  3 17  8]
    [ 2 11 11 16]
    [15  1  6  9]]
    '''

def exampledot():
    #matrix mul
    a=np.array([[2,3],[4,5]])
    b=np.array([6,7])
    print("input array a={}, b={}\n".format(a,b))
    print("np.dot(a,b)\n{}\n".format(np.dot(a,b)))
    '''
    input array 
    a=[[2 3][4 5]], b=[6 7]
    np.dot(a,b)
    [33 59]
    '''
def examplehistogram():
    #numpy.histogram(a, bins=10, range=None, density=None, weights=None)[source]
    a=np.array([89,34,56,87,90,23,45,12,65,78,9,34,12,11,2,65,78,82,28,78])
    b=np.histogram(a,bins=2)
    print("input array = {}\n".format(a))
    print("histogram result {}\n".format(b))
    '''
    input array = [89 34 56 87 90 23 45 12 65 78  9 34 12 11  2 65 78 82 28 78]
    histogram result (array([10, 10], dtype=int64), array([ 2., 46., 90.])) 꼭짓점 값(y), x축 시작 값 부터,...,끝 edge 값 (edge for x axis) 
    '''

def main():
    print("practice example\n")
    example1()
    example2()
    examplerand()
    exampereshape()
    examplenumpy()
    examplesort()
    examplewhere()
    exampleflip()
    exampledot()
    examplehistogram()

if __name__=="__main__":
    main()