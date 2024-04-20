import numpy as np

def main():
    np.random.seed(0)
    array_randint = np.random.randint(1, 20, 10) # 1 ~ 19
    print(array_randint)
    print("np.sort(variable) sort array \n{}\n".format(np.sort(array_randint)))
    array_randint.sort()
    print("array.sort() \n{}\n".format(array_randint))

    '''
    [13 16  1  4  4  8 10 19  5  7]
    sort array 
    [ 1  4  4  5  7  8 10 13 16 19]

    array.sort() 
    [ 1  4  4  5  7  8 10 13 16 19]
    '''

    array_boolean = np.array([False, True, False, True, False, True, False, False])
    print("array boolean sort \n{}\n".format(np.sort(array_boolean)))
    print("array boolean sort array.sort()\n{}\n".format(array_boolean.sort()))


if __name__=="__main__":
    main()
