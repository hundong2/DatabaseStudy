import numpy as np
import matplotlib.pyplot as plt

def example1():
    a = np.array([89, 34, 56, 87, 90, 23, 45, 12, 65, 78, 9, 34, 12, 11, 2 ,65, 78, 82, 28, 78])
    plt.hist(a, bins=5)
    plt.title("histogram example1")
    plt.show()

def example2():
    a = np.array([89, 34, 56, 87, 90, 23, 45, 12, 65, 78, 9, 34, 12, 11, 2 ,65, 78, 82, 28, 78])
    plt.hist(a, bins=[0,30,60,90], color='green')
    plt.title("histogram example2")
    plt.show()

def example3():
    a = np.array([89, 34, 56, 87, 90, 23, 45, 12, 65, 78, 9, 34, 12, 11, 2 ,65, 78, 82, 28, 78])
    plt.hist(a, bins=5, range=[30,80], color='yellow', edgecolor='black')
    plt.title("histogram example3")
    plt.show()

def exampleadditional():
    a = np.array([89, 34, 56, 87, 90, 23, 45, 12, 65, 78, 9, 34, 12, 11, 2 ,65, 78, 82, 28, 78])
    plt.hist(a, bins=10, edgecolor='black', cumulative=True)
    plt.title("example cumulative(True)")
    plt.show()

def exampledensity(): #probability of occurrence 
    a = np.array([89, 34, 56, 87, 90, 23, 45, 12, 65, 78, 9, 34, 12, 11, 2 ,65, 78, 82, 28, 78])
    plt.hist(a, bins=10, edgecolor='black', density=True)
    plt.title("example probability occurrence")
    plt.show()

def examplehistogramtype():
    a = np.array([89, 34, 56, 87, 90, 23, 45, 12, 65, 78, 9, 34, 12, 11, 2 ,65, 78, 82, 28, 78])
    plt.hist(a, bins=10, edgecolor='black', cumulative=True, histtype='step')
    plt.title("example histogram type")
    plt.show()

def main():
    print("example histogram2")
    example1()
    example2()
    example3()
    exampleadditional()
    exampledensity()
    examplehistogramtype()

if __name__=="__main__":
    main()