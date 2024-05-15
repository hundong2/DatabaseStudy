import numpy as np

def saveCSVfiles():
    npArray=np.array([[9,6,1,15],
                      [16,11,11,2],
                      [8,17,3,5]])
    print("input array \n{}\n".format(npArray))
    npArray.tofile('example9_tofile.csv', sep=",")
    # 9,6,1,15,16,11,11,2,8,17,3,5
    np.savetxt('example9_savetxt.csv',npArray, delimiter=',')
    '''
    9.000000000000000000e+00,6.000000000000000000e+00,1.000000000000000000e+00,1.500000000000000000e+01
    1.600000000000000000e+01,1.100000000000000000e+01,1.100000000000000000e+01,2.000000000000000000e+00
    8.000000000000000000e+00,1.700000000000000000e+01,3.000000000000000000e+00,5.000000000000000000e+00
    '''

def loadCSVfiles():
    npArrayGenFromTxt=np.genfromtxt('example9_savetxt.csv', delimiter=',')
    print("np.genfromtxt \n{}\n".format(npArrayGenFromTxt))
    '''
    [[ 9.  6.  1. 15.]
    [16. 11. 11.  2.]
    [ 8. 17.  3.  5.]]
    '''


def main():
    print("example numpy page62")
    #saveCSVfiles()
    loadCSVfiles()

if __name__=="__main__":
    main()