import numpy as np

def calculate_mean():
    array_mean=np.array([2,4,8,10,12])
    print("array mean = {}, mean= {}\n".format(array_mean, np.mean(array_mean)))

def calculate_mean_axis():
    array_mean = np.array([[10, 12, 13],
                            [45, 32, 16]])
    print("input array\n{}\n".format(array_mean))
    print("np.mean(array, axis=1)\n{}\n".format(np.mean(array_mean, axis=1)))
    print("np.mean(array, axis=0)\n{}\n".format(np.mean(array_mean, axis=0)))
    print("np.mean(array) -> all array element / array number of count\n{}\n".format(np.mean(array_mean)))
    '''
    *input array
    [[10 12 13]
    [45 32 16]]
    *np.mean(array, axis=1)
    (10+12+13)/3, (45, 32, 16)/3
    = [11.66666667 31.        ]
    *np.mean(array, axis=0)
    (10+45)/2, (12+32)/2, (13+16)/2
    = [27.5 22.  14.5]
    *np.mean(array)
    (10+12+13+45+32+16)/6
    = 21.333333333333332
    '''

def calculate_median():
    print("\n===calculate median===\n")
    array_median=np.array([2, 4, 8, 10, 12])
    print("input variable\n{}\n".format(array_median))
    print("median {}\n".format(np.median(array_median)))
    '''
    *input variable
    [ 2  4  8 10 12]
    *median 8.0
    '''
def calculate_two_dimension():
    print("calculate median two dimension\n")
    array_meidan=np.array([[10, 12, 13],
                           [20, 24, 26],
                           [45, 32, 16]])
    print("input array\n{}\n".format(array_meidan))
    print("np.median(array, axis=1)\n{}\n".format(np.median(array_meidan, axis=1)))
    print("np.median(array, axis=0)\n{}\n".format(np.median(array_meidan, axis=0)))
    print("np.mdedian(array)\n{}\n".format(np.median(array_meidan)))

    '''
    calculate median two dimension

    input array
    [[10 12 13]
    [20 24 26]
    [45 32 16]]

    np.median(array, axis=1)
    [12. 24. 32.]

    np.median(array, axis=0)
    [20. 24. 16.]

    np.mdedian(array)
    20.0
    '''

#https://ko.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-population/a/calculating-standard-deviation-step-by-step
def calc_standard_deviation():
    print("calculate deviation\n")
    array_input=np.array([[10, 12, 13], # 1.24721913 ( axis=1 )
                          [20, 24, 26], # 2.49443826 ( axis=1 )
                          [45, 32, 16]]) # 11.86029792 ( axis=1 )
                        # [14.71960144  8.21921867  5.55777733] ( axis = 0)

    print("calculate np.std(array, axis=1) \n{}\n".format(np.std(array_input, axis=1)))
    print("calculate np.std(array, axis=0) \n{}\n".format(np.std(array_input, axis=0)))
    print("calculate np.std(array)\n{}\n".format(np.std(array_input)))
    '''
    * calculate deviation
    * calculate np.std(array, axis=1) 
    [ 1.24721913  2.49443826 11.86029792]
    * calculate np.std(array, axis=0) 
    [14.71960144  8.21921867  5.55777733]
    * calculate np.std(array)
    10.614455552060438
    '''

def calculate_corrcoef():
    array_first = np.array([1, 3, 0, 0.9, 1.2])
    array_second = np.array([-1, 0.5, 0.2, 0.6, 5])
    print("correlation coefficient\n")
    print("input first array\n{}\ninput second array\n{}\n".format(array_first, array_second))
    print(np.corrcoef(array_first, array_second))

    '''
    correlation coefficient

    input first array
    [1.  3.  0.  0.9 1.2]
    input second array
    [-1.   0.5  0.2  0.6  5. ]

    [[1.         0.05708071]
    [0.05708071 1.        ]]
    '''

def example_min_max():
    array_minmax = np.array([2, 4, 8, 10, 12])
    print("example min/max variable\n")
    print("min variable {}\n".format(np.min(array_minmax)))
    print("max variable {}\n".format(np.max(array_minmax)))

def example_min_max_dimension():
    array_minmax_dimension= np.array([[10, 12, 13], 
                                      [20, 24, 26],
                                      [45, 32, 16]])
    print("input variable \n{}\n".format(array_minmax_dimension))
    print("* np.min(array) {}\n".format(np.min(array_minmax_dimension)))
    print("* np.max(array) {}\n".format(np.max(array_minmax_dimension)))
    print("* np.min(array, axis=1) \n{}\n".format(np.min(array_minmax_dimension, axis=1)))
    print("* np.min(array, axis=0) \n{}\n".format(np.min(array_minmax_dimension, axis=0)))
    print("* np.max(array, axis=1) \n{}\n".format(np.max(array_minmax_dimension, axis=1)))
    print("* np.max(array, axis=0) \n{}\n".format(np.max(array_minmax_dimension, axis=0)))      

    '''
    input variable 
    [[10 12 13]
    [20 24 26]
    [45 32 16]]

    * np.min(array) 10

    * np.max(array) 45

    * np.min(array, axis=1) 
    [10 20 16]

    * np.min(array, axis=0) 
    [10 12 13]

    * np.max(array, axis=1) 
    [13 26 45]

    * np.max(array, axis=0) 
    [45 32 26]
    '''

def example_unique():
    print("===unique array===")
    array_unique=np.array([5,8,7,5,9,3,7,7,1,1,8,4,6,9,7,3])
    print("input array {}\n".format(array_unique))
    print("np.unique(array) {}\n".format(np.unique(array_unique)))
    '''
    ===unique array===
    * input array [5 8 7 5 9 3 7 7 1 1 8 4 6 9 7 3]
    * np.unique(array) [1 3 4 5 6 7 8 9]
    '''
def example_tuple_unique():
    print("===tuple unique===\n")
    array_unique=np.array([[9, 18, 2, 17],
                           [8, 2, 18, 15],
                           [18, 17, 17, 13]])
    print("* input variable\n{}\n".format(array_unique))
    print("* np.unique(array, return_counts=True)\n{}\n".format(np.unique(array_unique, return_counts= True)))
    '''
    ===tuple unique===

    * input variable
    [[ 9 18  2 17]
    [ 8  2 18 15]
    [18 17 17 13]]

    * np.unique(array, return_counts=True)
    (array([ 2,  8,  9, 13, 15, 17, 18]), array([2, 1, 1, 1, 1, 3, 3]))
    '''

def example_unique_array():
    print("===example unique===")
    array_unique=np.array([5,8,7,5,9,3,7,7,1,1,8,4,6,9,7,3])
    delete_unique=np.unique(array_unique, return_counts=True)
    print("input vairalbe {}\n".format(array_unique))
    print("deleted unique array {}\n".format(delete_unique))
    '''
    ===example unique===
    input vairalbe [5 8 7 5 9 3 7 7 1 1 8 4 6 9 7 3]

    deleted unique array (array([1, 3, 4, 5, 6, 7, 8, 9]), array([2, 2, 1, 2, 1, 4, 2, 2]))
    '''

def example_axis_switching():
    print("===axis switching===\n")
    array_unique=np.array([5,8,7,5,9,3,7,7,1,1,8,4,6,9,7,3])
    delete_unique=np.unique(array_unique, return_counts=True)
    aixs_switching=np.array(delete_unique).T
    print("deleted array \n{}\n".format(delete_unique))
    print("changed axis \n{}\n".format(aixs_switching))
    '''
    ===axis switching===

    deleted array 
    (array([1, 3, 4, 5, 6, 7, 8, 9]), array([2, 2, 1, 2, 1, 4, 2, 2]))
    
    changed axis 
    [[1 2]
    [3 2]
    [4 1]
    [5 2]
    [6 1]
    [7 4]
    [8 2]
    [9 2]]
    '''
    
def main():
    print("statistics np\n")
    calculate_mean()
    print("two dimension statistics mean\n")
    calculate_mean_axis()
    print("calculate median\n")
    calculate_median()
    calculate_two_dimension()
    calc_standard_deviation()
    calculate_corrcoef()
    example_min_max()
    example_min_max_dimension()
    example_unique()
    example_tuple_unique()
    example_unique_array()
    example_axis_switching()

if __name__=="__main__":
    main()
    