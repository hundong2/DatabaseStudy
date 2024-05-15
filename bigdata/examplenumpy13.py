#reference by https://rfriend.tistory.com/380
import numpy as np

def exampleeye(): #Unit matrix, Identify matrix
    a=np.eye(4)
    print("eye(4)\n{}\n".format(a))
    '''
    eye(4)
    [[1. 0. 0. 0.]
    [0. 1. 0. 0.]
    [0. 0. 1. 0.]
    [0. 0. 0. 1.]]
    '''

def examplediag(): #diagonal matrix
    a = np.arange(9).reshape(3,3)
    print("input array\n{}\n".format(a))
    print("np.diag\n{}\n".format(np.diag(a))) # np.diag = [0 4 8]
    print("np.diag(np.diag)\n{}\n".format(np.diag(np.diag(a))))
    '''
    np.diag(np.diag)
    [[0 0 0]
    [0 4 0]
    [0 0 8]]
    '''

def main():
    print("example13 linear algebra")
    exampleeye()
    examplediag()

if __name__=="__main__":
    main()