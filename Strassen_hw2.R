# 09/02/2020
# CS531 HW 1(a)

m1 = matrix(c(6,9,1,3,2,4,5,5,1,3,5,8,2,9,9,6), nrow=4, byrow = T)
m2 = matrix(c(2,1,0,3,5,4,2,4,3,3,1,6,8,7,5,2), nrow=4, byrow=T)

A = m1[1:2,1:2]
B = m1[1:2,3:4]
C = m1[3:4,1:2]
D = m1[3:4,3:4]

E = m2[1:2,1:2]
FF = m2[1:2,3:4]
G = m2[3:4,1:2]
H = m2[3:4,3:4]

P1 = A %*% (FF - H)
P2 = (A+B) %*% H
P3 = (C+D) %*% E
P4 = D %*% (G-E)
P5 = (A+D) %*% (E+H)
P6 = (B-D) %*% (G+H)
P7 = (A-C) %*% (E+FF)

R = P5 + P4 - P2 + P6
S = P1 + P2
TT = P3 + P4
U = P5 + P1 - P3 - P7

res = matrix(nrow=4,ncol=4)
res[1:2,1:2] = R
res[1:2,3:4] = S
res[3:4,1:2] = TT
res[3:4,3:4] = U

res == m1 %*% m2