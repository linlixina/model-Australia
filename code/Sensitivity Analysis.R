#Sensitivity Analysis (IFR).

SI <- function(ifr){
  #Scenario 3
  data = read.csv("model-Australia/Results/scenario_3_all.csv")
  #the following term data$X1 correspond to r_u(t)
  r = as.vector(as.numeric((data$X1)))
  S <- rep(0,48)
  D <- rep(0,48)
  I <- rep(0,48)
  SS <- matrix(0,48,100000)
  DD <- matrix(0,48,100000)
  II <- matrix(0,48,100000)
  SSS <- matrix(0,48,3)
  DDD <- matrix(0,48,5)
  III <- matrix(0,48,3)
  for (i in 1:100000){
    for (t in 1:1){
      S[t] = 2885951
      D[t] = rbinom(1,round(S[t]),r[t])
      I[t] = 1/ifr*D[t]
    }
    for (t in 2:21){
      m=0
      for (w in 1:(t-1)){
        m = m + I[w]
      }
      S[t] = S[1]-1*m
      D[t] = rbinom(1,round(S[t]),r[t])
      I[t] = 1/ifr*D[t]
    }
    for (t in 22:22){
      m=0
      for (w in 1:(t-1)){
        m = m + I[w]
      }
      S[t] = S[1]-0.56*m
      D[t] = rbinom(1,round(S[t]),r[t])
      I[t] = 1/(0.31*ifr)*D[t]
    }
    for (t in 23:48){
      m=0
      for (w in 1:21){
        m = m + I[w]
      }
      n=0
      for (w in 22:(t-1)){
        n = n + I[w]
      }
      S[t] = S[1]-0.56*m-1*n
      D[t] = rbinom(1,round(S[t]),r[t])
      I[t] = 1/(0.31*ifr)*D[t]
    }
    SS[,i] <- S[]
    DD[,i] <- D[]
    II[,i] <- I[]
  }
  for (p in 1:48){
    SSS[p,1] <-mean(SS[p,]) 
    SSS[p,2] <-sort(SS[p,])[10000] 
    SSS[p,3] <-sort(SS[p,])[90000] 
    DDD[p,1] <-mean(DD[p,]) 
    DDD[p,2] <-sort(DD[p,])[10000] 
    DDD[p,3] <-sort(DD[p,])[90000] 
    DDD[p,4] <-sort(DD[p,])[2500] 
    DDD[p,5] <-sort(DD[p,])[97500] 
    III[p,1] <-mean(II[p,]) 
    III[p,2] <-sort(II[p,])[10000] 
    III[p,3] <-sort(II[p,])[90000] 
  }
  return(c(sum(DDD[, 1]), sum(DDD[, 4]), sum(DDD[, 5])))
}

SI(ifr=0.01)
SI(ifr=0.02)
SI(ifr=0.03)
SI(ifr=0.04)
SI(ifr=0.0445)
SI(ifr=0.05)



# Fig J
library(ggplot2)
data <- read.csv("model-Australia/Results/CFR-D.csv")

ggplot(data, aes(x = IFR, y = Deaths)) + 
  geom_errorbar(aes(ymin = Deaths_0.025, ymax = Deaths_0.975), width = 0.001) +
  ylim(5000, 25000) +
  geom_point() +
  labs(title = "Sensitivity Analysis (IFR)",
       x = expression(rho*", IFR of Delta variant in unvaccinated 50+"),
       y = "Total estimated deaths (Ds)") +
  theme_minimal()



