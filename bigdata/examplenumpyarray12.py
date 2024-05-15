import numpy as np
import sys

def examplescalar():
    print("==example {}()===".format(sys._getframe().f_code.co_name))
    a=np.array([1,2,3])
    c=np.array([5,5,5])
    b=5
    print("input variable a = {}, b={},c ={}\n".format(a,b,c))
    print("scalar mul a * b = {}\n".format(a*b))
    print("scalar mul a * c = {}\n".format(a*c))
    '''
    input variable a = [1 2 3], b=5
    scalar mul a * b = [ 5 10 15] ~ 1
    scalar mul a * c = [ 5 10 15] ~ 2
    fomula 1 = 2 ( same )
    '''
def examplebroadcasting():
    print("==example {}()===".format(sys._getframe().f_code.co_name))
    a=np.arange(3)
    b=5
    print("input a={}, b={}\n".format(a,b))
    print("calculate a*b = {}\n".format(a*b)) #left to right 
    # calculate a*b = [ 0  5 10]
    print("calculate b*a = {}\n".format(b*a))
    # calculate b*a = [ 0  5 10]
def examplebroadcastingmatrix():
    print("==example {}()===".format(sys._getframe().f_code.co_name))
    a=np.ones((3,3))
    b=np.arange(3)
    print("input variable\n{}\n{}\n".format(a,b))
    print("calculate a*b\n{}\n".format(a*b))
    print("np.dot(a,b)\n{}\n".format(np.dot(a,b)))
    print("calculate b*a\n{}\n".format(b*a))
    '''
    * input variable
    [[1. 1. 1.]
    [1. 1. 1.]
    [1. 1. 1.]]
    [0 1 2]
    * calculate a*b
    [[0. 1. 2.]
    [0. 1. 2.]
    [0. 1. 2.]]
    * np.dot(a,b)
    [3. 3. 3.]
    * calculate b*a
    [[0. 1. 2.]
    [0. 1. 2.]
    [0. 1. 2.]]
    '''
def examplebroadcastingmatrix2():
    print("==example {}()===".format(sys._getframe().f_code.co_name))
    a = np.array([[0],[1],[2]])
    b = np.arange(3)
    c = np.arange(2)
    print("*input variable\na={},b={},c={}\n".format(a, b,c))
    print("*calculate a*b {}{}\n{}\n".format(np.shape(a), np.shape(b), a*b))
    print("*calculate b*a {}{}\n{}\n".format(np.shape(b), np.shape(a), b*a))
    print("*calculate a*c {}{}\n{}\n".format(np.shape(a), np.shape(c), a*c))
    print("*calculate c*a {}{}\n{}\n".format(np.shape(c),np.shape(a),c*a))
    '''
    *input variable
    a=[[0]
    [1]
    [2]],b=[0 1 2]

    *calculate a*b
    [[0 0 0]
    [0 1 2]
    [0 2 4]]

    *calculate b*a
    [[0 0 0]
    [0 1 2]
    [0 2 4]]

    *calculate a*c
    [[0 0]
    [0 1]
    [0 2]]

    *calculate c*a
    [[0 0]
    [0 1]
    [0 2]]
    '''

def examplebroadcastingerror():
    print("==example {}()===".format(sys._getframe().f_code.co_name))
    a = np.ones((3,3))
    b = np.arange(2)
    print("input variable\na={},b={}\n".format(a,b))
    #print("calc a*b\n{}\n".format(a*b)) #ValueError: operands could not be broadcast together with shapes (3,3) (2,)

def main():
    print("numpy broadcasting calculate\n")
    examplescalar()
    examplebroadcasting()
    examplebroadcastingmatrix()
    examplebroadcastingmatrix2()
    examplebroadcastingerror()

if __name__=="__main__":
    main()