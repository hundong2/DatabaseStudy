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

if __name__ == "__main__":
    main()


