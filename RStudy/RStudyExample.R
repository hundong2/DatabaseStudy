#Matrix Study 
print("Matrix Study")

#matrix(data, row, ncol=1, byrow=FALSE)
#행, 열의 수를 지정하여 데이터를 2차원의 matrix 구조로 만든다. 
m1 <- matrix(c(1,2,3,4,5,6), ncol = 3, byrow=TRUE)
#ncol(column number)-> ncol=3 ,then row numbers is 2
#byrow=TRUE, 1행을 모두 채우고 2행을 채우는 순서로 채우기를 진행 
print(m1)

m2 <- matrix(c(1,2,3,4,5,6), nrow=3)
print(m2)

#rbind: rbind 함수에 목록으로 제공된 vector나 matrix들이 각각 행방향으로 연결된 행렬이 생성된다. 
#row bind(?)
x <- 1:3 
y <- seq(10, 30, 10)
result1 <- rbind(x,y)
print(result1)

#cbind: cbind 함수에 목록으로 제공된 vector나 matrix들이 각각 열 방향으로 연결된 행렬이 생성된다. 
#column bind(?)
x <- 1:3 
y <- seq(10, 30, 10)
result2 <- cbind(x,y)

#data.frame
xNum <- c(1:3)
xLog <- c(TRUE, FALSE, TRUE)
xChar <- c("a", "b", "C")
data <- data.frame(xNum, xLog, xChar)
str(data)
print(data$xNum)
print(data$xLog)
print(data$xChar)