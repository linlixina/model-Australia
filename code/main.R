#Scenario 1
data = read.csv("model-Australia/Results/scenario_1_all.csv")
###the following terms data$X1,data$X2,data$X3,data$X4,data$X5,data$X6 correspond to r_u(t), [1-v_(3+)(t)][1-e(t)]N, r_2a(t), [1-v_(3+)(t)]e(t)N, r_(3+)(t), v_(3+)(t)N in Eq.S4.
list1 = as.vector(as.numeric((data$X1)))
list2 = as.vector(as.numeric((data$X2)))
list3 = as.vector(as.numeric((data$X3)))
list4 = as.vector(as.numeric((data$X4)))
list5 = as.vector(as.numeric((data$X5)))
list6 = as.vector(as.numeric((data$X6)))
X <- rep(0,100000)
Y1 <- rep(0,48)
Y2 <- rep(0,48)
Y3 <- rep(0,48)
Y4 <- rep(0,48)
Y5 <- rep(0,48)
for (j in 1:48){
  for (i in 1:100000){
    X[i]=rbinom(1,round(list2[j]),list1[j])+rbinom(1,round(list4[j]),list3[j])+rbinom(1,round(list6[j]),list5[j])
  }
  Y1[j] <- mean(X)
  Y2[j] <-sort(X)[2500]
  Y3[j] <-sort(X)[97500]
  Y4[j] <-sort(X)[10000]
  Y5[j] <-sort(X)[90000]
}


sum(Y1)
sum(Y2)
sum(Y3)
sum(Y4)
sum(Y5)


#Scenario 2
data = read.csv("model-Australia/Results/scenario_2_all.csv")
###the following terms data$X1,data$X2,data$X3,data$X4,data$X5,data$X6,data$X7,data$X8,data$X9,data$X10, correspond to r_u(t), v_u(t)N, r_1(t), v_1(t)N, r_2(t), v_2(t)N, r_2a(t), N_(b_eff)(t), r_u(t), N_(b_i_eff)(t) in Eq.S6.
list1 = as.vector(as.numeric((data$X1)))
list2 = as.vector(as.numeric((data$X2)))
list3 = as.vector(as.numeric((data$X3)))
list4 = as.vector(as.numeric((data$X4)))
list5 = as.vector(as.numeric((data$X5)))
list6 = as.vector(as.numeric((data$X6)))
list7 = as.vector(as.numeric((data$X7)))
list8 = as.vector(as.numeric((data$X8)))
list9 = as.vector(as.numeric((data$X9)))
list10 = as.vector(as.numeric((data$X10)))
X <- rep(0,100000)
Y1 <- rep(0,48)
Y2 <- rep(0,48)
Y3 <- rep(0,48)
Y4 <- rep(0,48)
Y5 <- rep(0,48)
for (j in 1:48){
  for (i in 1:100000){
    X[i]=rbinom(1,round(list2[j]),list1[j])+rbinom(1,round(list4[j]),list3[j])+rbinom(1,round(list6[j]),list5[j])+rbinom(1,round(list8[j]),list7[j])+rbinom(1,round(list10[j]),list9[j])
  }
  Y1[j] <- mean(X)
  Y2[j] <-sort(X)[2500]
  Y3[j] <-sort(X)[97500]
  Y4[j] <-sort(X)[10000]
  Y5[j] <-sort(X)[90000]
}

sum(Y1)
sum(Y2)
sum(Y3)
sum(Y4)
sum(Y5)



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
    I[t] = 1/0.0445*D[t]
  }
  for (t in 2:21){
    m=0
    for (w in 1:(t-1)){
      m = m + I[w]
    }
    S[t] = S[1]-1*m
    D[t] = rbinom(1,round(S[t]),r[t])
    I[t] = 1/0.0445*D[t]
  }
  for (t in 22:22){
    m=0
    for (w in 1:(t-1)){
      m = m + I[w]
    }
    S[t] = S[1]-0.56*m
    D[t] = rbinom(1,round(S[t]),r[t])
    I[t] = 1/(0.31*0.0445)*D[t]
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
    I[t] = 1/(0.31*0.0445)*D[t]
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





#Scenario 1 (one week delay)
data = read.csv("model-Australia/Results/scenario_1_all_M_1.csv")
###the following items data$X1,data$X2,data$X3,data$X4,data$X5,data$X6 correspond to r_u(t), [1-v_(3+)(t)][1-e(t)]N, r_2a(t), [1-v_(3+)(t)]e(t)N, r_(3+)(t), v_(3+)(t)N in Eq.S4.
list1 = as.vector(as.numeric((data$X1)))
list2 = as.vector(as.numeric((data$X2)))
list3 = as.vector(as.numeric((data$X3)))
list4 = as.vector(as.numeric((data$X4)))
list5 = as.vector(as.numeric((data$X5)))
list6 = as.vector(as.numeric((data$X6)))
X <- rep(0,100000)
Y1 <- rep(0,48)
Y2 <- rep(0,48)
Y3 <- rep(0,48)
Y4 <- rep(0,48)
Y5 <- rep(0,48)
for (j in 1:48){
  for (i in 1:100000){
    X[i]=rbinom(1,round(list2[j]),list1[j])+rbinom(1,round(list4[j]),list3[j])+rbinom(1,round(list6[j]),list5[j])
  }
  Y1[j] <- mean(X)
  Y2[j] <-sort(X)[2500]
  Y3[j] <-sort(X)[97500]
  Y4[j] <-sort(X)[10000]
  Y5[j] <-sort(X)[90000]
}
sum(Y1)
sum(Y2)
sum(Y3)
sum(Y4)
sum(Y5)

#Scenario 2 (one week delay)
data = read.csv("model-Australia/Results/scenario_2_all_M_1.csv")
###the following items data$X1,data$X2,data$X3,data$X4,data$X5,data$X6,data$X7,data$X8,data$X9,data$X10, correspond to r_u(t), v_u(t)N, r_1(t), v_1(t)N, r_2(t), v_2(t)N, r_2a(t), N_(b_eff)(t), r_u(t), N_(b_i_eff)(t) in Eq.S6.
list1 = as.vector(as.numeric((data$X1)))
list2 = as.vector(as.numeric((data$X2)))
list3 = as.vector(as.numeric((data$X3)))
list4 = as.vector(as.numeric((data$X4)))
list5 = as.vector(as.numeric((data$X5)))
list6 = as.vector(as.numeric((data$X6)))
list7 = as.vector(as.numeric((data$X7)))
list8 = as.vector(as.numeric((data$X8)))
list9 = as.vector(as.numeric((data$X9)))
list10 = as.vector(as.numeric((data$X10)))
X <- rep(0,100000)
Y1 <- rep(0,48)
Y2 <- rep(0,48)
Y3 <- rep(0,48)
Y4 <- rep(0,48)
Y5 <- rep(0,48)
for (j in 1:48){
  for (i in 1:100000){
    X[i]=rbinom(1,round(list2[j]),list1[j])+rbinom(1,round(list4[j]),list3[j])+rbinom(1,round(list6[j]),list5[j])+rbinom(1,round(list8[j]),list7[j])+rbinom(1,round(list10[j]),list9[j])
  }
  Y1[j] <- mean(X)
  Y2[j] <-sort(X)[2500]
  Y3[j] <-sort(X)[97500]
  Y4[j] <-sort(X)[10000]
  Y5[j] <-sort(X)[90000]
}
sum(Y1)
sum(Y2)
sum(Y3)
sum(Y4)
sum(Y5)



#Scenario 3 (one week delay)
data = read.csv("model-Australia/Results/scenario_3_all_M_1.csv")
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
    I[t] = 1/0.0445*D[t]
  }
  for (t in 2:21){
    m=0
    for (w in 1:(t-1)){
      m = m + I[w]
    }
    S[t] = S[1]-1*m
    D[t] = rbinom(1,round(S[t]),r[t])
    I[t] = 1/0.0445*D[t]
  }
  for (t in 22:22){
    m=0
    for (w in 1:(t-1)){
      m = m + I[w]
    }
    S[t] = S[1]-0.56*m
    D[t] = rbinom(1,round(S[t]),r[t])
    I[t] = 1/(0.31*0.0445)*D[t]
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
    I[t] = 1/(0.31*0.0445)*D[t]
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





