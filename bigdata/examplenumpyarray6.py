import numpy as np

def slicing_array():
    print("\n===slicing array===\n")
    array_value = np.arange(1, 11)
    print("input array\n{}\n".format(array_value))
    #indexing array
    print("array[1] : {}\n".format(array_value[1]))
    print("array[1:8]\n{}\n".format(array_value[1:8]))
    print("array[:5]\n{}\n".format(array_value[:5]))
    print("array[5:]\n{}\n".format(array_value[5:]))
    print("array[:-1]\n{}\n".format(array_value[:-1]))
    print("array[-1:]\n{}\n".format(array_value[-1:]))
    print("array[-1:n]\n{}\n".format(array_value[-1:1]))
    '''
    ===slicing array===
    input array
    [ 1  2  3  4  5  6  7  8  9 10]
    array[1] : 2
    array[1:8]
    [2 3 4 5 6 7 8]
    array[:5]
    [1 2 3 4 5]
    array[5:]
    [ 6  7  8  9 10]
    array[:-1]
    [1 2 3 4 5 6 7 8 9]
    array[-1:]
    [10]
    array[-1:2]
    []
    '''

def slice_two_dimension():
    print("2 dimension array\n")
    array_two_dimension = np.array([[10, 12, 13],
                                   [24, 32, 16],
                                   [45, 32, 16]])
    print("input array\n{}\n".format(array_two_dimension))
    print("array[:2, :]\n{}\n".format(array_two_dimension[:2, :]))
    print("array[1:,1:]\n{}\n".format(array_two_dimension[1:, 1:]))

    '''
    input array
    [[10 12 13]
    [24 32 16]
    [45 32 16]]

    array[:2, :]
    [[10 12 13]
    [24 32 16]]

    array[1:,1:]
    [[32 16]
    [32 16]]
    '''
def indexchange():
    array_change = np.array([10, 12, 13])
    print("input array\n{}\n".format(array_change))
    print("np.where(array>9)\n{}\n".format(np.where(array_change > 9)))
    print("np.where(array>10)\n{}\n".format(np.where(array_change > 10)))
    print("np.where(array>12)\n{}\n".format(np.where(array_change > 12)))
    '''
    *input array
    [10 12 13]
    *np.where(array>9)
    (array([0, 1, 2]),)
    *np.where(array>10)
    (array([1, 2]),)
    *np.where(array>12)
    (array([2]),)
    '''
def indexchange2():
    array_change = np.array([[12, 9 , 83, 40],
                             [73, 59, 24, 2],
                             [44, 3, 18, 65]])
    print("*input array\n{}\n".format(array_change))
    print("*np.where(array>50)\n{}\n".format(np.where(array_change>50)))
    print("(0,2)=83, (1,0)=73, (1,1)=59, (2,3)=65\n")
    '''
    *input array
    [[12  9 83 40]
    [73 59 24  2]
    [44  3 18 65]]

    *np.where(array>50)
    (array([0, 1, 1, 2]), array([2, 0, 1, 3]))

    (0,2)=83, (1,0)=73, (1,1)=59, (2,3)=65
    '''
    print("array[np.where[array>n]]\n{}\n".format(array_change[np.where(array_change>50)]))
    '''
    array[np.where[array>n]]
    [83 73 59 65]
    '''

def main():
    #slicing information
    slicing_array()
    #slicing two dimension
    slice_two_dimension()
    #change indexing
    indexchange()
    indexchange2()

if __name__=="__main__":
    main()