setwd("/Users/477z/Desktop")

negAIRDMs = read.csv('/Users/477z/Desktop/EmoDNN/behavior/negv2/negRDMS.csv', header = TRUE, fileEncoding = "UTF8") 

negsubRDMs = read.csv('/Users/477z/Desktop/EmoDNN/behavior/negv2/negSubRDMS.csv', header = TRUE, fileEncoding = "UTF8") 



dataCox15list = list()
for (AI in names(negAIRDMs)) {
  dataCo = c()
  for (sub in names(negsubRDMs)) {
    co = cor(negAIRDMs[[AI]], negsubRDMs[[sub]], method = "spearman")
    co = fisherz(co)
    
    dataCo = c(dataCo, co)
  }
  dataCox15list[[AI]] <- dataCo #list中每一層代表
}

negdataTest = data.frame()
for (AI in names(negAIRDMs)) {
  confI = t.test(dataCox15list[[AI]])$conf.int
  mean = t.test(dataCox15list[[AI]])$estimate
  temp = c(AI, confI[1], mean, confI[2])
  negdataTest = rbind(negdataTest, temp)
}
colnames(negdataTest) <- c("layers", "neglower", "negestimate", "negupper")

#############################NEU

neuAIRDMs = read.csv('/Users/477z/Desktop/EmoDNN/behavior/neuv2/neuRDMS.csv', header = TRUE, fileEncoding = "UTF8") 

neusubRDMs = read.csv('/Users/477z/Desktop/EmoDNN/behavior/neuv2/neuSubRDMS.csv', header = TRUE, fileEncoding = "UTF8") 

dataCox15list = list()
for (AI in names(neuAIRDMs)) {
  dataCo = c()
  for (sub in names(neusubRDMs)) {
    co = cor(neuAIRDMs[[AI]], neusubRDMs[[sub]], method = "spearman")
    co = fisherz(co)
    
    dataCo = c(dataCo, co)
  }
  dataCox15list[[AI]] <- dataCo #list中每一層代表
}

neudataTest = data.frame()
for (AI in names(neuAIRDMs)) {
  confI = t.test(dataCox15list[[AI]])$conf.int
  mean = t.test(dataCox15list[[AI]])$estimate
  temp = c(confI[1], mean, confI[2])
  neudataTest = rbind(neudataTest, temp)
}
colnames(neudataTest) <- c( "lower", "estimate", "upper")

##############ALL

allAIRDMs = read.csv('/Users/477z/Desktop/EmoDNN/behavior/allv2/AIRDMS.csv', header = TRUE, fileEncoding = "UTF8") 

allsubRDMs = read.csv('/Users/477z/Desktop/EmoDNN/behavior/allv2/allSubRDMS.csv', header = TRUE, fileEncoding = "UTF8") 

dataCox15list = list()
for (AI in names(allAIRDMs)) {
  dataCo = c()
  for (sub in names(allsubRDMs)) {
    co = cor(allAIRDMs[[AI]], allsubRDMs[[sub]], method = "spearman")
    co = fisherz(co)
    
    dataCo = c(dataCo, co)
  }
  dataCox15list[[AI]] <- dataCo #list中每一層代表
}

alldataTest = data.frame()
for (AI in names(allAIRDMs)) {
  confI = t.test(dataCox15list[[AI]])$conf.int
  mean = t.test(dataCox15list[[AI]])$estimate
  temp = c(confI[1], mean, confI[2])
  alldataTest = rbind(alldataTest, temp)
}
colnames(alldataTest) <- c( "alllower", "allestimate", "allupper")
#繪圖

library(ggplot2)
library(patchwork)

negdataTest$nu <- as.numeric(1:15)
negdataTest$neglower = as.numeric(negdataTest$neglower)
negdataTest$negestimate = as.numeric(negdataTest$negestimate)
negdataTest$negupper = as.numeric(negdataTest$negupper)

neudataTest$lower = as.numeric(neudataTest$lower)
neudataTest$estimate = as.numeric(neudataTest$estimate)
neudataTest$upper = as.numeric(neudataTest$upper)

alldataTest$alllower = as.numeric(alldataTest$alllower)
alldataTest$allestimate = as.numeric(alldataTest$allestimate)
alldataTest$allupper = as.numeric(alldataTest$allupper)

merged_df <- cbind(negdataTest, neudataTest, alldataTest)

plot <- ggplot(merged_df, aes(x = nu))+
  geom_line(aes(y = 0),alpha = 0.3, color = "black") +
  geom_line(aes(y = estimate, color = "blue")) +  # 中心线，蓝色
  geom_ribbon(aes(ymin = lower, ymax = upper), alpha = 0.15, fill = "blue")  +  # neu信賴區間區域，蓝色填充
  geom_line(aes(y = negestimate, color = "red")) +  # 中心线，红色
  geom_ribbon(aes(ymin = neglower, ymax = negupper), alpha = 0.15, fill = "red")+  # neg信賴區間區域，红色填充
  geom_line(aes(y = allestimate, color = "purple")) +  # 中心线，紫色
  geom_ribbon(aes(ymin = alllower, ymax = allupper), alpha = 0.15, fill = "purple")+  # all信賴區間區域，紫色填充
  ylim(-0.05, 0.4) +
  xlab("layers") +
  ylab("Spearman's ρ") +
  scale_x_continuous(breaks = merged_df$nu, labels = merged_df$layers) +
  scale_color_manual(name = "Lines", values = c("blue" = "blue", "red" = "red", "purple" = "purple"),labels = c("blue" = "Neural Images", "red" = "Negtive Images", "purple" = "All Images"),limits = c("blue", "red", "purple")) +
  guides(color = guide_legend(title = "Lines"), fill = "none")+
  #scale_color_manual(name = "Lines", values = c("blue" = "blue", "red" = "red"),labels = c("blue" = "Neural Images", "red" = "Negtive Images"),limits = c("blue", "red")) +
  #guides(color = guide_legend(title = "Lines"), fill = "none")+
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
  

plot

ggsave("combine_Conf_All_plot.png", plot, width = 6, height = 4, dpi = 300)


