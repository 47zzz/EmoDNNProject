setwd("/Users/477z/Desktop")

AIRDMs = read.csv('/Users/477z/Desktop/AIRDMS.csv', header = TRUE, fileEncoding = "UTF8") 

subRDMs = read.csv('/Users/477z/Desktop/EmoDNN/behavior/all/allSubRDMS.csv', header = TRUE, fileEncoding = "UTF8") 

#以下負責折線圖
dataCox15list = list()
for (AI in names(AIRDMs)) {
  dataCo = c()
  for (sub in names(subRDMs)) {
    co = cor(AIRDMs[[AI]], subRDMs[[sub]], method = "spearman")
    co = fisherz(co)
    
    dataCo = c(dataCo, co)
  }
  dataCox15list[[AI]] <- dataCo #list中每一層代表
}

dataTest = data.frame()
for (AI in names(AIRDMs)) {
  confI = t.test(dataCox15list[[AI]])$conf.int
  mean = t.test(dataCox15list[[AI]])$estimate
  temp = c(AI, confI[1], mean, confI[2])
  dataTest = rbind(dataTest, temp)
}
colnames(dataTest) <- c("layers", "lower", "estimate", "upper")

library(ggplot2)

dataTest$nu <- as.numeric(1:15)
dataTest$lower = as.numeric(dataTest$lower)
dataTest$estimate = as.numeric(dataTest$estimate)
dataTest$upper = as.numeric(dataTest$upper)

plot = ggplot(dataTest, aes(x = nu, y = estimate)) +
  geom_line(aes(y = 0),alpha = 0.3, color = "black") +
  geom_line(aes(y = estimate), color = "red") +  # 中心線
  geom_ribbon(aes(ymin = lower, ymax = upper), alpha = 0.3, fill = "orange") +  # 信賴區間區域
  ylim(-0.05, 0.4) +
  xlab("layers") +
  ylab("Spearman's ρ")+
  scale_x_continuous(breaks = dataTest$nu, labels = dataTest$layers)+
  theme(axis.text.x = element_text(angle = 45, hjust = 1))


plot

ggsave("ALLv2_Conf_All_plot.png", plot, width = 5, height = 4, dpi = 300)


