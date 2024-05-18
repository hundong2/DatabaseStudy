import pandas as pd
from pandas import Series, DataFrame

#exampe pandas dataframe

def exampleDataframe():
    print("example dataframe\n")
    items={
        'code':[1,2,3,4],
        '계정과목': ['매출채권', '매출원가', '현금', '자본'],
        '금액': [1500, 15000, 1000, 500],
        '재무제표': ['재무상태표', '손익계산서', '현금흐름표', '자본변동표']
    }
    data=DataFrame(items)
    print(data)
    '''
        code  계정과목     금액   재무제표
    0     1  매출채권   1500  재무상태표
    1     2  매출원가  15000  손익계산서
    2     3    현금   1000  현금흐름표
    3     4    자본    500  자본변동표
    '''
    #data.to_csv('exampledataframe.csv')
    '''
    ,code,계정과목,금액,재무제표
    0,1,매출채권,1500,재무상태표
    1,2,매출원가,15000,손익계산서
    2,3,현금,1000,현금흐름표
    3,4,자본,500,자본변동표
    '''

def examplereadcsv():
    pandasvalue=pd.read_csv("exampledataframe.csv") #encoding='cp949'   
    print(pandasvalue)

def main():
    print("Example datafram\n")
    exampleDataframe()
    examplereadcsv()

if __name__=="__main__":
    main()