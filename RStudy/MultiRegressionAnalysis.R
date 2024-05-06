set.seed(10)
u <- runif(50,0,6)
v <- runif(50,6,12)
w <- runif(50,3,25)
y = 3 + 0.5*u + 1*v - 2*w + rnorm(50, 0, 0.5)
df <- data.frame(y,u,v,w)

a <- lm(y ~ u + v + w, df)
a

'''
Call:
  lm(formula = y ~ u + v + w, data = df)

Coefficients:
  (Intercept)            u            v            w  
3.4374       0.4676       0.9556      -1.9923  

'''