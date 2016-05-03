args <- strsplit(commandArgs(TRUE),";")[[1]]
round <- args[1]
Me <- args[2]
global <- args[3]
state <- as.data.frame(do.call(rbind,strsplit(args[-(1:3)],"_")), stringsAsFactors=FALSE)
colnames(state) <- c("id","pts","flipped","unflipped")
state$flipped <- as.integer(state$flipped)
state$unflipped <- as.integer(state$unflipped)
nb <- nrow(state)
my_place <- which(state$id==Me)
next_place <- ifelse(my_place!=nb,my_place+1,1)
previous_place <- ifelse(my_place!=1,my_place-1,nb)
n <- 3
out <- c()
while(n){
    if(2*state$flipped[next_place]-state$unflipped[next_place] > max(0,2*state$flipped[my_place]-state$unflipped[my_place])){
        out <- c(out,"R")
        state[,3:4] <- state[c(2:nb,1),3:4]
        n <- n-1
    }else if(2*state$flipped[previous_place]-state$unflipped[previous_place] > max(0,2*state$flipped[my_place]-state$unflipped[my_place])){
        out <- c(out, "T")
        state[,3:4] <- state[c(nb,1:(nb-1)),3:4]
        n <- n-1
    }else if(state$unflipped[my_place]<2*state$flipped[my_place]){
        out <- c(out, "1")
        state$unflipped[my_place] <- state$unflipped[my_place]+1
        n <- n-1
    }else{
        out <- c(out, switch(n,"1"="A","2"="1F","3"="2FF"))
        n <- 3-nchar(out)
        }
    }
cat(paste(out,collapse=""))