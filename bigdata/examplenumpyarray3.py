# 2 dimension 
import numpy as np

def function_array1():
    array_dimension = np.array([[3, 4, 7],
                                [13, 5, 6],
                                [10, 11, 9]])
    print("input array \n{}\n".format(array_dimension))
    print("np.sort() axis=1 \n{}\n".format(np.sort(array_dimension, axis = 1))) #default option 1
    array_dimension.sort(axis = 1)
    print("array.sort() axis=1 \n{}\n".format(array_dimension))

    '''
    input array 
    [[ 3  4  7]
    [13  5  6]
    [10 11  9]]

    np.sort() axis=1 
    [[ 3  4  7]
    [ 5  6 13]
    [ 9 10 11]]

    array.sort() axis=1 
    [[ 3  4  7]
    [ 5  6 13]
    [ 9 10 11]]
    '''

def function_array2():
    array_dimension = np.array([[3, 4, 7],
                                [13, 5, 6],
                                [10, 11, 9]])
    print("input array \n{}\n".format(array_dimension))
    print("np.sort() axis=0 \n{}\n".format(np.sort(array_dimension, axis = 0))) #default option 1
    array_dimension.sort(axis = 0)
    print("array.sort() axis=0 \n{}\n".format(array_dimension))

    '''
    input array 
    [[ 3  4  7]
    [13  5  6]
    [10 11  9]]

    np.sort() axis=0 
    [[ 3  4  6]
    [10  5  7]
    [13 11  9]]

    array.sort() axis=0 
    [[ 3  4  6]
    [10  5  7]
    [13 11  9]]
    '''

def main():
    function_array1()
    function_array2()

if __name__=="__main__":
    main()