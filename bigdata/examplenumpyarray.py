import numpy as np

def main():
    num_list = [10, 12, 14, 16, 20 ]
    print( "numlist {} ", type(num_list))

    nums_array = np.array(num_list)
    print("convert to numpy {}, type {} ", nums_array, type(nums_array))

    #array 

    row1 = [10,12,13]
    row2 = [45,32,16]
    row3 = [45, 32, 16]

    print("value {} : {} ".format([name for name in globals() if globals()[name] is row1], row1 ))
    print("value {} : {} ".format([name for name in globals() if globals()[name] is row2], row2 ))
    print("value {} : {} ".format([name for name in globals() if globals()[name] is row3], row3 ))

    nums_2d = np.array([row1, row2, row3])
    print( nums_2d )
    print( nums_2d.dtype)
    print( nums_2d.shape)
    #arrange
    nums_arr = np.arange(5,11) #np.arange(5,11) => [5 6 7 8 9 10]
    print(nums_arr)
    #arrange step
    nums_step_arr = np.arange(5,11,2) #5~10, step +2 => [5 7 9]
    print(nums_step_arr)
    #ones composed 1 
    ones_array = np.ones(3)
    print("ones function {}, datatype : {} ".format( ones_array, ones_array.dtype))
    #ones tuple row, column
    ones_array_tuple = np.ones((3, 5))
    print("tuple of ones\n {}".format(ones_array_tuple))
    #combination row, column 
    ones_combination_array = np.ones((2,3,5))
    print("combination \n {}".format(ones_combination_array))
    #zeros() function
    ones_zero_array = np.zeros(6)
    print("np zeros \n{} ".format(ones_zero_array))
    #zeros(row, column)
    ones_zeros_rowcol_array = np.zeros((3,5))
    print("np zeros(3,5)\n{} ".format( ones_zeros_rowcol_array ))
    #eye() unit matrix
    eyes_array = np.eye(5)
    print("eyes(5) \n {} ", eyes_array) 
    #randon() 0~1 random numbers from uniform distribution ( 균등분포 난수 )
    # you want to get fixed value at that times of execution -> setting seed
    np.random.seed(0)
    random_array = np.random.rand(6)
    print("random.rand(6) \n {} ".format( random_array))  
    # random.randn()
    # avarage 0, standard deviation 1( 표준편차 )
    # standard normal distribution ( 표준정규분포 )
    random_randn_array = np.random.randn(6)
    print("random randn \n {}".format(random_randn_array)) 

    #random integer numpy random randint 
    random_int = np.random.randint(1,6) # (1, 6) = 1 ~ 5, (6) = 0 ~ 5
    print("random int {} ".format(random_int))
    print("random int {} ( 10~14, 5 numbers random variable [x, x, x, x, x] )".format(np.random.randint(10, 15, 5)))

    #numpy dimension, shape 
    np_array_of_value = np.array([10, 12, 14, 16, 18, 20])
    print("numpy array {} ".format(np_array_of_value))
    print("numpy dimension {}, shape {} ".format(np_array_of_value.ndim, np_array_of_value.shape))
    for i in np_array_of_value:
        print(i, end=' ')
    print("\narray append {} + [22, 24] -> {}".format(np_array_of_value, np.append(np_array_of_value, [22, 24])))
    print("\nnumpy range area {}".format( np.arange(10,21,2) ))

    #array row (4), column (5)
    print("\nnumpy array row, column\n {} ".format( np.random.randint(1, 11, size = (4, 5))))

    #numpy zeros row, column 
    print("\nnumpy zeros row, column \n {}".format(np.zeros((3, 3))))

    #numpy append to array, axis = 0 -> x axis
    nparray = np.zeros((3, 3))
    value_x_axis = np.append(nparray ,[[1, 2, 3]], axis =0)
    print("\nnumpy append row, column \n {}".format(value_x_axis))

    '''
    numpy append row, column 
    [[0. 0. 0.]
    [0. 0. 0.]
    [0. 0. 0.]
    [1. 2. 3.]]
    '''

    #numpy append to array, axis = 1 -> y axis 
    value_y_axis = np.append(nparray, [[1], [2], [3]], axis = 1)
    print("\nnumpy append row, column \n {}".format(value_y_axis))

    '''
    numpy append row, column 
    [[0. 0. 0. 1.]
    [0. 0. 0. 2.]
    [0. 0. 0. 3.]]
    '''

    # delete array 
    delete_array = np.array(["Red", "Green", "Orange"])
    print("delete array {}\n".format(delete_array))
    #delete array ['Red' 'Green' 'Orange']

    deleted_array = np.delete(delete_array, 1)
    print("deleted array {}\n".format(deleted_array))
    #deleted array ['Red' 'Orange']

    deleted_array_set_position = np.delete(delete_array, [0, 2])
    print("deleted array set position {}\n".format(deleted_array_set_position))
    #deleted array set position ['Green']

    array_random_for_delete = np.random.randint(1, 11, size= (4,5))
    print("set array for delete axis \n {}\n".format(array_random_for_delete))
    print("delete axis x \n{}\n".format(np.delete(array_random_for_delete, 1, axis = 0)))
    print("delete axis y \n{}\n".format(np.delete(array_random_for_delete, 1, axis = 1)))

    '''
    set array for delete axis 
    [[ 4  3  8  3  1]
    [ 1  5  6  6  7]
    [ 9  5  2  5 10]
    [ 9  2  2  8 10]]

    delete axis x 
    [[ 4  3  8  3  1]
    [ 9  5  2  5 10]
    [ 9  2  2  8 10]]

    delete axis y 
    [[ 4  8  3  1]
    [ 1  6  6  7]
    [ 9  2  5 10]
    [ 9  2  8 10]]
    '''




if __name__ == "__main__":
    main()


