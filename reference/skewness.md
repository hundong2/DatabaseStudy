# Skewness ( 왜도 ) 

- symmetrical bell curve or normal distribution에서 왜곡 정도를 말한다. 
- 데이터 분포으 ㅣ대칭성이 얼마나 결핍되었는지를 측정. 
- 집중화 경향 측정에는 평균(Mean)/ 중앙값(Median)/ 최빈값(Mode) 가 사용된다. 
- Negative Skewed : 왼쪽 꼬리가 긴 상태, 오른쪽에 데이터가 치우친 상태 
  - `Mean < Median < Mode` 
- Symmetrical Distribution ( 대칭 )
  - `Mean = Median = Mode`
- Positive-Skewed : 오른쪽 꼬리가 긴 상태, 왼쪽에 데이터가 치우친 상태
  - `Mean > Median > Mode`  
- Outlier(이상치)
  - 꼬리가 긴 방향에 있을 수 있음.  
  - 평균은 이상치의 영향을 많이 받고, 중앙값은 이상치에 민감하지 않음.  

![https://miro.medium.com/v2/resize:fit:640/format:webp/1*nj-Ch3AUFmkd0JUSOW_bTQ.jpeg](https://miro.medium.com/v2/resize:fit:640/format:webp/1*nj-Ch3AUFmkd0JUSOW_bTQ.jpeg)  

# Kurtosis ( 첨도 )

- 분포에 존재하는 특이치(outlier)의 척도이다. 
- kurtois가 높으면 데이터가 두꺼운 꼬리나 outlier를 가지고 있다는 것을 의미하는 지표.   
- Kurtois가 낮으면 데이터가 얇은 꼬리나 oulier를 가지고 있지 않다는 뜻이다. 

![picture2](https://miro.medium.com/v2/resize:fit:640/format:webp/1*Nqu07THa7APRTOF7kaVr5Q.jpeg)  

- `Mesokurtic` : 이 분포는 정규 분포와 유사한 첨도 통계량을 가지고 있다. 분포의 극단값이 정규 분포 특성과 유사하다는 뜻이다. 표준 정규 분포는 3의 첨도 갖는다.

- `Leptokurtic (Kurtosis > 3)` : 분포가 길고, 꼬리가 더 뚱뚱하다. 피크는 Mesokurtic보다 높고 날카롭기 때문에 데이터는 꼬리가 무겁거나 특이치(outlier)가 많다는 것을 의미한다.
특이치(outlier)는 히스토그램 그래프의 수평 축을 확장하여 데이터의 대부분이 좁은 수직 범위로 나타나도록 하여 Leptokurtic 분포의 "skinniness"을 부여한다.

- `Platykurtic (Kurtosis < 3)` : 분포는 짧고 꼬리는 정규 분포보다 얇다. 피크는 Mesokurtic보다 낮고 넓으며, 이는 데이터가 가벼운 편이나 특이치(outlier)가 부족하다는 것을 의미한다.
이유는 극단값(extream value)이 정규 분포의 극단값보다 작기 때문이다.

$$
\bar{x}=\frac{x_1+x_2+...+x_n}{n}=\frac{1}{n}\sum_{i=1}^{n}x_i
$$

# 데이터 퍼짐 정도 측정  

- 산포도 (Dispersion)
  - 자료의 변량들이 흩어져 있는 정도를 하나의 수로 나타낸 값
  - 산포도가 크면 변량들이 평균으로 부터 멀리 흩어져 있고, 변동성이 커진다.  
  - 산포도가 작으면 변량들이 평균 주위에 밀집, 변동성이 작아진다. 
  - 범위, 사분위수 범위, 분산, 표준편차, 절대편차, 변동 계수 등이 있다. 

- 범위 ( Range )
  - `범위=최댓값-최솟값`  

- 사분위수 범위( Interqualtile Range )
  - IQR=Q3-Q1
  - 가운데 50% 데이터가 위치하는 범위. 
  - 이상치 검출에 사용되는 수치. 
  - boxplot 

- 편차(Deviation)
  - `편차=변량-평균`  
  - 어떤 자료의 변량에서 평균을 뺀값. 
  - 편차의 총합은 항상 0. 
  - 편차의 절댓값이 클수록 변량들은 평균에서 멀리 떨어져 있다. 
  - 퓨ㅕㄴ차의 절댓값이 작을 수록 변량들은 평균에 가까이 있다. 

- 표본 분산 (Variance) 
  $$ 
  s^2 = \frac{1}{n-1}\sum_{x=1}^{n}(x_i - \bar{x})^2 
  $$
  - 편차 제곱의 합을 자유도(n-1)로 나눈 것. 
  - 데이터 집합이 얼마나 퍼져 있는지 알아볼 수 있는 수치. 
  - 평균이 같아도 분산은 다를 수 있다. 
  - example
    - input = [1,3,5,7,9]
    - mean = (1+3+5+7+9)/5 = 5
    - variance = (16+4+0+4+16) / 4 = 10

- 표본 표준 편차( s, Standard Deviation)

  $$
  s=\sqrt{\frac{1}{n-1}\sum_{x=1}{n}(x_i-\bar{x})^2}
  $$

  - 자료의 산포도를 나타내는 수치. 분산의 양의 제곱근을 의미한다. 
## reference 

- https://dining-developer.tistory.com/17  
- https://codeburst.io/2-important-statistics-terms-you-need-to-know-in-data-science-skewness-and-kurtosis-388fef94eeaa
- 표본 분산 : https://m.blog.naver.com/sw4r/221021838997  



