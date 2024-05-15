import numpy as np

def exampleSqrt():
    listvariable=[10, 20, 30, 40, 50]
    sqrtvariable=np.sqrt(listvariable)
    print("input variable: {}\noutput variable(np.sqrt): {}\n".format(listvariable, sqrtvariable))
    '''
    input variable: [10, 20, 30, 40, 50]
    output variable(np.sqrt): [3.16227766 4.47213595 5.47722558 6.32455532 7.07106781]  
    '''
    
def exampleLog():
    listvariable=[10, 20, 30, 40, 50]
    logvariable=np.log(listvariable)
    print("input variable: {},\nlog variable: {}\n".format(listvariable, logvariable))
    '''
    input variable: [10, 20, 30, 40, 50],
    log variable: [2.30258509 2.99573227 3.40119738 3.68887945 3.91202301]
    '''

def exampleExponential():
    listvariable=[10,20,30,40,50]
    expvariable=np.exp(listvariable)
    print("input variable: {}\nexp variable: {}\n".format(listvariable, expvariable))
    '''
    input variable: [10, 20, 30, 40, 50]
    exp variable: [2.20264658e+04 4.85165195e+08 1.06864746e+13 2.35385267e+17
    5.18470553e+21]
    '''

def main():
    print("example numpy page62~")
    exampleSqrt()
    exampleLog()
    exampleExponential()

if __name__=="__main__":
    main()