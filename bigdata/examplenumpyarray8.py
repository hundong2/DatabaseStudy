"""@package docstring
    The code defines two functions in Python that demonstrate flipping arrays horizontally and
    vertically using NumPy, and then calls these functions in the main function.
Python array example 
"""
import sys
import numpy as np


def examplefliplr():
    """
    The `examplefliplr` function flips an array from top to bottom and prints the original and flipped
    arrays.
    """
    print("==example {}()===".format(sys._getframe().f_code.co_name))
    arrayorigin=np.array([5,8,7,9,3])
    arrayflip=np.flipud(arrayorigin)
    print("left to right flip\n- original array {} \n- fliped array {}\n".format(arrayorigin, arrayflip))
    '''
    ==example exampleflip()===
    left to right flip
    - original array [5 8 7 9 3] 
    - fliped array [3 9 7 8 5]
    '''

def exampleflipud():
    """
    The `exampleflipud` function flips a 2D array vertically (upside down) and prints both the original
    and flipped arrays.
    """
    print("==example {}()===".format(sys._getframe().f_code.co_name))
    arrayorigin=np.array([
        [9,6,1,15],
        [16,11,11,2],
        [8,17,3,5]
    ])
    arrayupdown=np.flipud(arrayorigin)
    print("up to down\n- origin \n{}\n-up down array \n{}\n".format(arrayorigin, arrayupdown))
    '''
    up to down
    - origin 
    [[ 9  6  1 15]
    [16 11 11  2]
    [ 8 17  3  5]]
    -up down array 
    [[ 8 17  3  5]
    [16 11 11  2]
    [ 9  6  1 15]]
    '''

def exampleflip():
    """
    The `exampleflip` function demonstrates how to perform up-down and left-right flips on a NumPy array
    along with axis-specific flips.
    """
    print("==example {}()===".format(sys._getframe().f_code.co_name))
    arrayorigin=np.array([
        [9,6,1,15],
        [16,11,11,2],
        [8,17,3,5]
    ])
    arrayudlr=np.flip(arrayorigin)
    print("ud + lr flip\n- original \n{}\n- flip() \n{}\n".format(arrayorigin, arrayudlr))
    '''
    ud + lr flip
    - original 
    [[ 9  6  1 15]
    [16 11 11  2]
    [ 8 17  3  5]]
    - flip() 
    [[ 5  3 17  8]
    [ 2 11 11 16]
    [15  1  6  9]]
    '''
    arrayudlraxis0=np.flip(arrayorigin, axis=0) #same flipud()
    arrayydlraxis1=np.flip(arrayorigin, axis=1) #same fliplr()
    print("flip(axis=0)\n{}\n".format(arrayudlraxis0))
    print("flip(axis=1)\n{}\n".format(arrayydlraxis1))
    '''
    flip(axis=0)
    [[ 8 17  3  5]
    [16 11 11  2]
    [ 9  6  1 15]]

    flip(axis=1)
    [[15  1  6  9]
    [ 2 11 11 16]
    [ 5  3 17  8]]
    '''

def main():
    print("array of numpy")
    examplefliplr()
    exampleflipud()
    exampleflip()

if __name__=="__main__":
    main()