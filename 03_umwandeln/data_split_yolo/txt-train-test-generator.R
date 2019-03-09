####### Create test and trainings set
# Achtung: Pfad anpassen
setwd("C:/Users/ValeriaR/Desktop/Yolo")

##### COWC ######
# set directory
#setwd("./03_cowc")

# load txt file
d <- read.csv("t_all_cowc.txt", header=FALSE)
str(d)

# training test data split
samp <- sample(nrow(d), nrow(d)*0.8)
test <- seq(nrow(d))[-samp]
dsamp <- d[samp,]
dtest <- d[test,]
dsamp1 <- as.data.frame(dsamp)
dtest1 <- as.data.frame(dtest)

##### PUCPR #####
# set directory
#setwd("./04_pucpr")

# load txt file
d2 <- read.csv("t_all_pucpr.txt", header=FALSE)
str(d2)

# training test data split
samp <- sample(nrow(d2), nrow(d2)*0.8)
test <- seq(nrow(d2))[-samp]
dsamp <- d2[samp,]
dtest <- d2[test,]
d2samp <- as.data.frame(dsamp)
d2test <- as.data.frame(dtest)

##### CARPK #####
# set directory
#setwd("./05_carpk")

# load txt file
d3 <- read.csv("t_all_carpk.txt", header=FALSE)
str(d3)

# training test data split
samp <- sample(nrow(d3), nrow(d3)*0.8)
test <- seq(nrow(d3))[-samp]
dsamp <- d3[samp,]
dtest <- d3[test,]
d3samp <- as.data.frame(dsamp)
d3test <- as.data.frame(dtest)

##### Google #####
# set directory
#setwd("./06_Google")

# load txt file
d4 <- read.csv("t_all_google.txt", header=FALSE)
str(d4)

# training test data split
samp <- sample(nrow(d4), nrow(d4)*0.8)
test <- seq(nrow(d4))[-samp]
dsamp <- d4[samp,]
dtest <- d4[test,]
d4samp <- as.data.frame(dsamp)
d4test <- as.data.frame(dtest)

###### Create train and test txt.file #####
sampf <- rbind(dsamp1,d2samp,d3samp,d4samp)
testf <- rbind(dtest1,d2test,d3test,d4test)

#setwd("./01_approach-x%-y%")
write.table(sampf,"train.txt",row.names=FALSE, col.names=FALSE, quote=FALSE)
write.table(testf,"test.txt",row.names=FALSE, col.names=FALSE, quote=FALSE)
