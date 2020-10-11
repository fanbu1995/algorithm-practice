# CS531 HW5, prob 2

findModInverse <- function(e, n){
  for(i in c(1:(n-1))){
    if((e*i) %% n == 1){
      cat(i)
      return(i)
    }
  }
}

findModInverse(3,40)
findModInverse(17,40)
