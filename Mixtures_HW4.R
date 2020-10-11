# CS531 HW4 problem 3

# Problem 3, (d)
# visualize the triangle region of possible mixtures

x = c(.1, .2, .4)
y = c(.35, .05, .25)
plot(y~x, pch=16, main='region of viable mixtures', 
     xlim=c(0,0.5), ylim=c(0,0.5), xlab='component A density', ylab='component B density')
polygon(x,y,col = 'lightgray')
points(x=c(.25,.3,.15), y=c(.27,.14,.15), 
       pch=16, col=c('red','blue','orange'))