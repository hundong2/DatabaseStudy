import pandas as pd
from pandas import Series, DataFrame

def exampleSeries():
    print("example Series\n")
    cost=Series([4000,3000,3500,2000])
    print(cost)
    '''
    example Series
    0    4000
    1    3000
    2    3500
    3    2000
    dtype: int64
    '''
    print(cost.index) #cost.index = RangeIndex(start=0, stop=4, step=1)
    print(cost.values) #cost.values = [4000 3000 3500 2000]

def exampeSeries1():
    print("example Series()")
    cost=Series([4000,3000,3500,2000], index=['cash', 'account receivable', 'land', 'building' ])
    print(cost)
    '''
    cash                  4000
    account receivable    3000
    land                  3500
    building              2000
    dtype: int64
    '''
    print("cost[0] = {}\n".format( cost.iloc[0] )) #cost[0] == cost.iloc[0], result "cost[0]=4000"
    print("cost.dtype={}\n".format(cost.dtype)) #cost.dtype=int64
    print("cost.size={}\n".format(cost.size)) #cost.size=4
    print("cost.ndim={}\n".format(cost.ndim)) #cost.ndim=1
    #calculate 
    print("cost + 100={}\n".format(cost+100)) #not change original value
    '''
    cash                  4100
    account receivable    3100
    land                  3600
    building              2100
    '''
    print("sum(cost)={}\n".format(sum(cost))) #sum(cost)=12500

def exampeSeries2():
    print("example Series\n")
    cost1=Series([4000,3000,None,2000], ['A','B','C','D'])
    cost2=Series([3000,3000,3500,None], ['A','E','B','D'])
    print(cost1)
    print(cost2)
    print(cost1+cost2)
    '''
    A    4000.0
    B    3000.0
    C       NaN
    D    2000.0
    dtype: float64

    + 

    A    3000.0
    E    3000.0
    B    3500.0
    D       NaN
    dtype: float64
    
    = 
    
    A    7000.0 ( cost1 + cost2 )
    B    6500.0 ( cost1 + cost2 )
    C       NaN ( cost1 value is Nan ( None ))
    D       NaN ( cost2 value is NaN ( None ))
    E       NaN ( cost1 not contained E )
    dtype: float64
    '''
    print(cost1['A'] + cost2['E']) #7000.0 (4000+3000)
    print(cost1.iloc[0] + cost2['E']) #7000.0 (4000+3000)

def exampleSeries3():
    print("example conditional\n")
    cost=Series([4000,3000,3500,2000],index=['A','B','C','D'])
    print(cost)
    '''
    A    4000
    B    3000
    C    3500
    D    2000
    dtype: int64
    '''
    print(cost>3000)
    '''
    A     True
    B    False
    C     True
    D    False
    dtype: bool
    '''
    print(cost[cost>3000])
    '''
    A    4000
    C    3500
    dtype: int64
    '''
    print(cost[[True,False,True,True]])
    '''
    A    4000
    C    3500
    D    2000
    dtype: int64
    '''
def exampleSeries4():
    print("example isnull\n")
    cost=Series([4000,3000,None,2000],index=['A','B','C','D'])
    print(cost.isnull())
    '''
    A    False
    B    False
    C     True
    D    False
    dtype: bool
    '''
    print(cost[cost.isnull()])
    '''
    C   NaN
    dtype: float64
    '''

def main():
    print("pandas example1\n")
    exampleSeries()
    exampeSeries1()
    exampeSeries2()
    exampleSeries3()
    exampleSeries4()
if __name__=="__main__":
    main()