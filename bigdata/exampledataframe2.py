import pandas as pd
from pandas import Series, DataFrame

def example1():
    data=[{'col_1':3, 'col_2': 'a'},
          {'col_1':2, 'col_2': 'b'},
          {'col_1':1, 'col_2': 'c'},
          {'col_1':0, 'col_2': 'd'}]
    data2={'col_1':3, 'col_2': 'a'}
    data3=(1,3)
    print(data)
    print("data type dictionary list [{{}}, {{}}, ...]: {}".format(type(data)) )
    #data type dictionary list [{}, {}, ...]: <class 'list'> 
    print("data type dictionary {{}}: {}".format(type(data2))) #data type dictionary {}: <class 'dict'>
    print("data type (value1, value2): {}".format(type(data3))) #data type <class 'tuple'>
    
    print(pd.DataFrame.from_records(data))
    '''
        col_1 col_2
    0      3     a
    1      2     b
    2      1     c
    3      0     d
    '''

def example2():
    data=[(3,'a'),(2,'b'),(1,'c'),(0,'d')]
    print(pd.DataFrame.from_records(data, columns=['col_1', 'col_2']))
    '''
       col_1 col_2
    0      3     a
    1      2     b
    2      1     c
    3      0     d
    '''

def examplereadcsv():
    df = pd.read_csv('./bigdata/exampledataframe2.csv')
    print(df)
    '''
       code  계정과목     금액       재무제표
    0     1  매출채권   1500  재무상태표, BS
    1     2  매출원가  15000  손익계산서, IS
    2     3    현금   1000  현금흐름표, CF
    3     4    자본    500   자본변동표,EC
    '''
    #change column ( not changed df )
    print(df[['code','금액','계정과목','재무제표']])
    '''
       code     금액  계정과목       재무제표
    0     1   1500  매출채권  재무상태표, BS
    1     2  15000  매출원가  손익계산서, IS
    2     3   1000    현금  현금흐름표, CF
    3     4    500    자본   자본변동표,EC
    '''
    print(df['금액'])
    '''
    0     1500
    1    15000
    2     1000
    3      500
    '''
    print(df.iloc[0]) #0번째 데이터 가져오기 
    '''
    code            1
    계정과목         매출채권
    금액           1500
    재무제표    재무상태표, BS
    Name: 0, dtype: object
    '''
    print("df.iloc[0]['재무제표']: {}\n".format(df.iloc[0]['재무제표'])) #df.iloc[0]['재무제표']: 재무상태표, BS
    print("df.iloc[0][3]: {}\n".format(df.iloc[0][3])) #df.iloc[0][3]: 재무상태표, BS
    print("df.iloc[재무제표][0]: {}\n".format(df['재무제표'][0])) #df.iloc[재무제표][0]: 재무상태표, BS
    #0~1 row values
    print("df.iloc[0:2]: {}".format(df.iloc[0:2]))
    '''
    df.iloc[0:2]:   
          code  계정과목     금액       재무제표
    0     1  매출채권       1500        재무상태표, BS
    1     2  매출원가       15000       손익계산서, IS
    '''
    #0~1 row, 1~2 column
    print("df.iloc[0:2,1:3]:\n{}\n".format(df.iloc[0:2,1:3]))
    '''
    df.iloc[0:2,1:3]:
       계정과목     금액
    0  매출채권   1500
    1  매출원가  15000
    '''

def exampleloc():
    df = pd.read_csv('./bigdata/exampledataframe2.csv')
    print(df)
    '''
       code  계정과목     금액       재무제표
    0     1  매출채권   1500  재무상태표, BS
    1     2  매출원가  15000  손익계산서, IS
    2     3    현금   1000  현금흐름표, CF
    3     4    자본    500   자본변동표,EC
    '''
    print("df.loc[0:2]\n{}\n".format(df.loc[0:2]))
    '''
    df.loc[0:2]
        code  계정과목     금액       재무제표
    0     1  매출채권   1500  재무상태표, BS
    1     2  매출원가  15000  손익계산서, IS
    '''
    print("df.loc[0:2, ['금액','계정과목']]:\n{}\n".format(df.loc[0:2, ['금액', '계정과목']]))
    '''
    df.loc[0:2, ['금액','계정과목']]:
        금액  계정과목
    0   1500  매출채권
    1  15000  매출원가
    2   1000    현금
    '''
    print("df.loc[0:2,['금액','계정과목']]:\n{}\n".format(df.loc[0:2, ['금액','계정과목']]))
    '''
    df.loc[0:2,['금액','계정과목']]:
        금액  계정과목
    0   1500  매출채권
    1  15000  매출원가
    2   1000    현금
    '''
 

def main():
    print("read data example")
    example1()
    example2()
    examplereadcsv()
    exampleloc()


if __name__=="__main__":
    main()
