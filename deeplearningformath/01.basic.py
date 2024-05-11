import numpy as np

def example_numpy():
    arrayValue=np.array([1,2,3,4], dtype="uint8")
    arrayValue32=np.array([1,2,3,4], dtype="uint32")
    arrayValueFloat=np.array([1,2,3,4.0])
    arrayValueOverflow=np.array([111,222,333,444], dtype="uint8")
    print("array {}, dtype {}".format(arrayValue, arrayValue.dtype))
    print("array {}, dtype {}".format(arrayValue32, arrayValue32.dtype))
    print("array {}, dtype {}".format(arrayValueFloat, arrayValueFloat.dtype))
    print("array value overflow example {}, dtype {}".format(arrayValueOverflow, arrayValueOverflow.dtype))
    '''
    For the old behavior, usually:
    np.array(value).astype(dtype)
    will give the desired result (the cast overflows).
    arrayValueOverflow=np.array([111,222,333,444], dtype="uint8")
    array [1 2 3 4], dtype uint8
    array [1 2 3 4], dtype uint32
    array [1. 2. 3. 4.], dtype float64
    array value overflow example [111 222  77 188], dtype uint8
    '''
    
def main():
    print("example basic{}".format("01"))
    example_numpy()

if __name__=="__main__":
    main()