#example dataframe 
import pandas as pd
from pandas import Series, DataFrame

def example1():
    df=pd.read_csv('./examplefile/분개장.csv', encoding='utf-8')
    print(df.shape) #(24237, 9) 24237 row, 9 column
    print(df.size) #218133
    print(df.dtypes)
    '''
    전표일자       object
    전표번호        int64
    계정코드        int64
    계정과목       object
    차변금액       object
    대변금액       object
    거래처       float64
    승인일자       object
    프로젝트코드     object
    dtype: object
    '''
    print(df['차변금액'].dtypes) #object

def example2():
    df=pd.read_csv('./examplefile/분개장.csv', encoding='utf-8')
    #df['차변금액'] = df['차변금액'].astype('int64') #error ValueError: invalid literal for int() with base 10: '832,000' comma(,)
    df['차변금액'] = df['차변금액'].str.replace(',', '').astype('int64')
    print(df['차변금액'])
    '''
    0           832000
    1            83200
    2                0
    3           120340
    4            12034
            ...
    24232    536903920
    24233            0
    24234    350000000
    24235            0
    24236            0
    Name: 차변금액, Length: 24237, dtype: int64
    '''
    
def main():
    print("example dataframe")
    example1()
    example2()
if __name__=="__main__":
    main()