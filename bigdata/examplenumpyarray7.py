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

def main():
    print("statistics np\n")
    calculate_mean()
    print("two dimension statistics mean\n")
    calculate_mean_axis()


if __name__=="__main__":
    main()
    