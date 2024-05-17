import numpy as np
import matplotlib.pyplot as plt

def examplehistogram():
    a = np.array([89, 34, 56, 87, 90, 23, 45, 12, 65, 78, 9, 34, 12, 11, 2 ,65, 78, 82, 28, 78])
    histogram=np.histogram(a)
    print(histogram)
    '''
    histogram
    (array([2, 3, 2, 2, 1, 0, 1, 2, 3, 4], dtype=int64), array([ 2. , 10.8, 19.6, 28.4, 37.2, 46. , 54.8, 63.6, 72.4, 81.2, 90. ]))
    '''
    histogram2 = np.histogram(a,bins=2)
    print(histogram2) # (array([10, 10], dtype=int64), array([ 2., 46., 90.]))

    histogram3=np.histogram(a, bins=[0,30,60,90])
    print(histogram3) #(array([7, 4, 9], dtype=int64), array([ 0, 30, 60, 90]))

    histogram4=np.histogram(a, bins=5, density=True) #density 확률 값
    print(histogram4) #(array([0.01420455, 0.01136364, 0.00284091, 0.00852273, 0.01988636]), array([ 2. , 19.6, 37.2, 54.8, 72.4, 90. ]))

def exampledrawing():
    a = np.array([89, 34, 56, 87, 90, 23, 45, 12, 65, 78, 9, 34, 12, 11, 2 ,65, 78, 82, 28, 78])
    plt.hist(a, color='green', alpha=0.4) #alpha: 투명도 
    plt.title("my histogram")
    plt.show()

def exampledrawing2():
    a = np.array([89, 34, 56, 87, 90, 23, 45, 12, 65, 78, 9, 34, 12, 11, 2 ,65, 78, 82, 28, 78])
    histogram2 = np.histogram(a,bins=2)# (array([10, 10], dtype=int64), array([ 2., 46., 90.]))
    plt.hist(histogram2)
    plt.title("histogram")
    plt.show()


def main():
    print("histogram")
    examplehistogram()
    exampledrawing()
    exampledrawing2()
if __name__=="__main__":
    main()