args <- strsplit(commandArgs(TRUE),";")[[1]]
state <- as.data.frame(do.call(rbind,strsplit(args[-(1:3)],"_")), stringsAsFactors=FALSE)
colnames(state) <- c("id","pts","flipped","unflipped")
state$flipped <- as.integer(state$flipped)
state$unflipped <- as.integer(state$unflipped)
nb <- nrow(state)
score <- function(place) 2*state$flipped[place]-state$unflipped[place]
my_place <- which(state$id==args[2])
next_1 <- ifelse(my_place!=nb,my_place+1,1)
next_2 <- ifelse(next_1!=nb,next_1+1,1)
next_3 <- ifelse(next_2!=nb,next_2+1,1)
previous_1 <- ifelse(my_place!=1,my_place-1,nb)
previous_2 <- ifelse(previous_1!=1,previous_1-1,nb)
previous_3 <- ifelse(previous_2!=1,previous_2-1,nb)
n <- 3
out <- c()
while(n){
    M <- N <- score(my_place)
    R <- switch(n,"1"=score(next_1),
                "2"=cumsum(c(score(next_1),score(next_2))),
                "3"=cumsum(c(score(next_1),score(next_2),score(next_3))))
    P <- switch(n,"1"=score(previous_1),
                "2"=cumsum(c(score(previous_1),score(previous_2))),
                "3"=cumsum(c(score(previous_1),score(previous_2),score(previous_3))))
    M <- c(M,M+R[-n])
    N <- c(N,N+P[-n])
    if(any(R>M & R>0)){
        action <- c("R","RR","RRR")[which.max(R-M)]
        out <- c(out, action)
        state[,3:4] <- state[c((nchar(action)+1):nb,seq_len(nchar(action))),3:4]
        n <- n-nchar(action)
    }else if(any(P>N & P>0)){
        action <- c("T","TT","TTT")[which.max(P-N)]
        out <- c(out, action)
        state[,3:4] <- state[c((nb+1-seq_len(nchar(action))),1:(nb-seq_len(nchar(action)))),3:4]
        n <- n-nchar(action)
    }else if(n>1 & all(R[1]+M[1]>c(0,P[1]+M[1],R[1]+R[2]))){
        out <- c(out,"RT")
        n <- n-2
    }else if(n>1 & all(P[1]+M[1]>c(0,R[1]+M[1],P[1]+P[2]))){
        out <- c(out,"TR")
        n <- n-2
    }else{
        out <- c(out, switch(n,"1"="A","2"="1F","3"="2FF"))
        n <- 0
        }
    }
cat(paste(out,collapse=""))