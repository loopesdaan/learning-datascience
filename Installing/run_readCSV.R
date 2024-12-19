
require(data.table)
require(ggplot2)

dt <- fread("/Users/daanloopes/Desktop/learning/learning-python/data/base_test.csv")

summary(dt$score)

data <- data.frame(x = c(1, 2, 3, 4), y = c(1, 4, 9, 16))
ggplot(data, aes(x, y)) + geom_line()
