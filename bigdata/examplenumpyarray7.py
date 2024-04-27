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

def main():
    print("statistics np\n")
    calculate_mean()
    print("two dimension statistics mean\n")
    calculate_mean_axis()
    print("calculate median\n")
    calculate_median()
    calculate_two_dimension()
    calc_standard_deviation()

if __name__=="__main__":
    main()
    