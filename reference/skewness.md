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


## reference 

- https://dining-developer.tistory.com/17  
- https://codeburst.io/2-important-statistics-terms-you-need-to-know-in-data-science-skewness-and-kurtosis-388fef94eeaa


