set.seed(2)
x=runif(50, 0, 5) #0~5 범위에서 50개의 난수를 균등분포를 따르도록 생성. 
y = 5 + 2 * x + rnorm(50, 0, 0.5) # rnorm 특정 평균 및 표준편차를 갖으며 정규분포를 따르는 난수를 발생. 평균0, 표준편차 0.5, 50개의 정규 분포를 따르는 난수. 
df <- data.frame(x, y) 
fit <- lm(y~x, data=df)
fit
# 2.072x + 4.748 = y ( 회귀계수: 2.072, 절편: 4.748 )