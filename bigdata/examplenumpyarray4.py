# accending/descending order 
import numpy as np

def array_sort_test():
    array_sort = np.array([[3, 4, 7],
                           [13, 5, 6],
                           [10, 11, 9]])
    print("<==array sort example==>")
    print("input array : \n{}\n".format( array_sort))
    array_sort.sort(axis=1)
    print("array.sort() result \n{}\n".format(array_sort))
    arange_array = array_sort[:, ::-1]
    print("array[:, ::-1] \n{}\n".format(arange_array))

    
def dimension_test():
    array_dimension = np.array([[3, 4, 7],
                                [13, 5, 6],
                                [10, 11, 9]])
    
    print("===column array sort===\n")
    print("<-directing(left, right)->\n")
    print("input array \n{}\n".format(array_dimension))
    print("np.sort() \n{}\n".format(np.sort(array_dimension, axis=1))) #column
    print("np.sort() [::-1] \n{}\n".format(np.sort(array_dimension, axis=1)[::-1]))
    '''
    input array 
    [[ 3  4  7]
    [13  5  6]
    [10 11  9]]

    np.sort() 
    [[ 3  4  7]
    [ 5  6 13]
    [ 9 10 11]]

    np.sort() [::-1] 
    [[ 9 10 11]
    [ 5  6 13]
    [ 3  4  7]]
    '''

    print("===row array sort===\n")
    print("directing up, down\n")
    print("input array \n{}\n".format(array_dimension))
    print("np.sort() \n{}\n".format(np.sort(array_dimension, axis=0))) #row
    print("np.sort() [::-1] \n{}\n".format(np.sort(array_dimension, axis=0)[::-1]))
    '''
    input array 
    [[ 3  4  7]
    [13  5  6]
    [10 11  9]]

    np.sort() 
    [[ 3  4  6]
    [10  5  7]
    [13 11  9]]

    np.sort() [::-1] 
    [[13 11  9]
    [10  5  7]
    [ 3  4  6]]
    '''
def descending_test():
    array_value = np.array([13, 5, 6, 7, 2, 8])
    print("input array \n{}\n".format(array_value))
    array_descending = np.sort(array_value)[::-1]
    print("Descending - np.sort(array)[::-1]\n{}\n".format(array_descending))
    print("Ascending - np.sort(array)\n{}\n".format(np.sort(array_value)))
    array_flip = np.flip(np.sort(array_value), axis = 0)
    print("np.flip <axis = 0>\n{}\n".format(array_flip))
    '''
    input array 
    [13  5  6  7  2  8]

    Descending - np.sort(array)[::-1]
    [13  8  7  6  5  2]

    Ascending - np.sort(array)
    [ 2  5  6  7  8 13]

    np.flip <axis = 0>
    [13  8  7  6  5  2]
    '''

def main():
    print("==ascending/ descending==\n")
    descending_test()
    print("==2 dimension test==\n")
    dimension_test()
    print("==array sort==\n")
    array_sort_test()

if __name__=="__main__":
    main()