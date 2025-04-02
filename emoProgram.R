setwd("/Users/477z/Desktop")

AIRDMs = read.csv('/Users/477z/Desktop/EmoDNN/behavior/all/allRDMS.csv', header = TRUE, fileEncoding = "UTF8") 

subRDMs = read.csv('/Users/477z/Desktop/EmoDNN/behavior/all/STD_allSubRDMS.csv', header = TRUE, fileEncoding = "UTF8") 
#以下負責barchart
representData = data.frame(layers = c(), data = c())

for (AI in names(AIRDMs)) {
  totalCo = 0
  count = 0
  temp = c(AI)
  for (sub in names(subRDMs)) {
    co = cor(AIRDMs[[AI]], subRDMs[[sub]], method = "spearman")
    co = fisherz(co)
    totalCo = totalCo + co
    count = count + 1
  }
  average = totalCo/count
  temp = c(temp, average)
  representData = rbind(representData, temp)
}
colnames(representData) <- c("layers", "data")


library(ggplot2)

#轉為長資料

reLong <- tidyr::gather(representData, key = "Dimensions", value = "Value", -layers)

reLong$Value <- as.numeric(reLong$Value)

#讓其依照理想排序
orderd = c() 
for(i in representData$layers){
  orderd = append(orderd, i)
}
reLong$layers = factor(reLong$layers, levels = orderd)


# 使用 ggplot 函數繪製bar圖
plot = ggplot(reLong, aes(x = layers, y = Value, color = Dimensions, group = Dimensions)) +
geom_bar(stat = "identity", fill = "skyblue", width = 0.5, color = "skyblue") +
labs(x = "layers", y = "Spearman's correlation") +
ylim(-0.1, 0.4)

###############
plot

ggsave("Nor_All_plot.png", plot, width = 6, height = 4, dpi = 300)





