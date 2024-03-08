library(RCurl)
res <- getURL("https://fruityvice.com/api/fruit/banana", .opts=list(followlocation = TRUE))
cat(res)