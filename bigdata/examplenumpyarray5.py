#array shape
import numpy as np

def changedimension():
    np.random.seed(0) 
    array_value = np.random.randint( 1, 20, 10 )
    print("input random variable shape {} \n{}\n".format(array_value.shape, array_value))
    change_array = array_value.reshape(2,5)
    print("reshape(2, 5) shape: {} \n{}\n".format(change_array.shape, change_array))
    '''
    input random variable 
    [13 16  1  4  4  8 10 19  5  7]

    reshape(2, 5) 
    [[13 16  1  4  4]
    [ 8 10 19  5  7]]
    '''

def makerandint_withshape():
    np.random.seed(0)
    shape_array = np.random.randint(1, 20, size=(3, 6))
    print("make randint with shape {} \n{}\n".format(shape_array.shape, shape_array))
    '''
    make randint with shape (3, 6) 
    [[13 16  1  4  4  8]
    [10 19  5  7 13  2]
    [ 7  8 15 18  6 14]]
    '''
    array_reshape = np.reshape(shape_array, ( 3,2,3))
    print("make reshape {}\n{}\n".format(array_reshape.shape, array_reshape))
    '''
    make reshape (3, 2, 3)
    [[[13 16  1]
    [ 4  4  8]]

    [[10 19  5]
    [ 7 13  2]]

    [[ 7  8 15]
    [18  6 14]]]
    '''  
def change_dimension():
    print("\n==change dimension==\n")
    array_value = np.random.randint(1 , 20, size=(3,6))
    print("input array: \n{}\n".format(array_value))
    print("array np.reshape(array, n), n = 18\n{}\n".format(np.reshape(array_value, 18)))
    print("array np.reshape(array, -1)\n{}\n".format(np.reshape(array_value, -1)))
    '''
    ==change dimension==
    input array: 
    [[ 9 10 17  6 16 16]
    [ 1 19  4 18 15  8]
    [ 1  2 10  1 11  4]]
    array np.reshape(array, n), n = 18
    [ 9 10 17  6 16 16  1 19  4 18 15  8  1  2 10  1 11  4]
    array np.reshape(array, -1)
    [ 9 10 17  6 16 16  1 19  4 18 15  8  1  2 10  1 11  4]
    '''
def main():
    #change dimension with shape 
    changedimension()

    #make randint with shape
    makerandint_withshape()

    #change dimension 
    change_dimension()


if __name__=="__main__":
    main()