# doxygen 

- drag & drop source code range of function or all text 
- command key + `.` key

# numpy 

- Numpy array 느ㄴ 데이터 불러오기, 삽입, 삭ㅔ, 업ㅔ이트에 있어서 매우 빠름. 
- 일반적인 파이썬 array에 비하여 고급의 브로드캐스트 기능을 제공
- 고급 수학 및 선형대수 옵션을 지원하는 많은 함수를 가지고 있다. 
- 다차원 array 를 분리해주는 고급 기능을 제공

## data type

- `i` = integer 
- `b` = boolean
- `u` = unsigned integer 
- `f` = float 
- `c` = complex float 
- `m` = timedelta
- `M` = datetime 
- `o` = Object 
- `S` = string 
- `U` = Unicode string 
- `V` = fixed chunk of memory other type(void)  

- example 
  - [numpy data type example](numpyexample.py)  

## standard deviation

### reference site 

- [standard deviation](https://ko.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-population/a/calculating-standard-deviation-step-by-step)   
  
$$
\frac{\sqrt{\sum{(x - \mu)^2}}}{N}
$$

- $\mu$ = average, $N$ = count of numbers
- [example python code](./examplenumpyarray7.py)  
  - calc_standard_deviation function  


## correlation coefficient (상관계수)  

- 상관계수(相關係數, 영어: correlation coefficient)는 두 변수 사이의 통계적 관계를 표현하기 위해 특정한 상관 관계의 정도를 수치적으로 나타낸 계수이다.[1]  
여러 유형의 상관계수가 존재하지만 제각기 자신들만의 정의와 특징이 있다. 이들은 모두 값의 범위가 -1에서 +1 사이에 속하며 여기서 ±1은 정도가 가장 센 잠재적 일치를 나타내고 0은 정도가 가장 센 불일치를 나타낸다.[2]  

[위키백과, 우리 모두의 백과사전.](https://ko.wikipedia.org/wiki/%EC%83%81%EA%B4%80%EA%B3%84%EC%88%98)   

- [python code](./examplenumpyarray7.py)  
  - corrcoef() function  

## numpy

- [array of numpy page - p50](./examplenumpyarray7.py)  
  - example numpy mean, median, corrcoef, min/max, unique 
- [array of numpy page - p60](./examplenumpyarray8.py)  
  - example flipud, fliplr (ud : updown, lr : leftright ), upper 2 dimension 
- [csv file save, load - p61](./examplenumpyarray9.py)
  - getfromtxt, savetxt, ... 
- [numpy calculate, page - p62~63](./examplenumpyarray10.py)  
  - sqrt, log, exp
- [numpy array matrix calculate - p64~p65](./examplenumpyarray11.py)  
  - np.dot
- [numpy calculate matrix - p66~67](./examplenumpyarray12.py)  
  - matrix scalar mul
- [numpy linalg](./examplenumpy13.py)/ [reference site](https://rfriend.tistory.com/380)  
  - linalg : linear algebra 
  - Unit matrix(단위행렬) : np.eye(n)
  - Diagnoal matrix(대각행렬) : np.diag(x)
  - Dot product, Inner product ( 내적 ) : np.dot(a,b)
  - Trace(대각합) : np.trace(x)
  - Matrix Determinant ( 행렬식 ) : np.linalg.det(x)
  - Inverse of a matrix ( 역행렬 ) : np.linalg.inv(x)  
  - Singular Value Decomposition ( 특이값 분해 ) : u,s,vh = np.linalg.svd(A) 
  - Solve a linear matrix equation ( 연립방벙식 해 풀기 ) : np.linalg.solve(a,b)  
  - Compute the least-squares solution (최소자승 해 풀기) : m,c = np.linalg.lstsq(A, y, rcond=None)[0]  
- [example1 histogram](./examplenumpy14.py)  
- 