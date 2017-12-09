wd = setwd("C:/Users/mixal")
library(foreign)
library(ggplot2)

#HTree_1_1 = read.arff('./SlashDot//HTree_ROC_SlashDot1-1.arff')
#J48_1_1 = read.arff('./SlashDot//J48_ROC_SlashDot1-1.arff')

HTree_1_10 = read.arff('./reality_mining///HTree_ROC_reality_mining_Data1-600.arff')
J48_1_10 = read.arff('./reality_mining///J48_ROC_reality_mining_Data1-600.arff')

#HTree_1_1 = HTree_1_1[,c(6,7)]
#colnames(HTree_1_1) = c("FPR","TPR")
#J48_1_1 = J48_1_1[,c(6,7)]
#colnames(J48_1_1) = c("FPR","TPR")

HTree_ROC_1_10 = HTree_1_10[,c(6,7)]
colnames(HTree_ROC_1_10) = c("FPR","TPR")
J48_ROC_1_10 = J48_1_10[,c(6,7)]
colnames(J48_ROC_1_10) = c("FPR","TPR")

HTree_PR_1_10 = HTree_1_10[,c(8,9)]
colnames(HTree_PR_1_10) = c("Precision","Recall")
J48_PR_1_10 = J48_1_10[,c(8,9)]
colnames(J48_PR_1_10) = c("Precision","Recall")

#ggplot(NULL, aes(FPR, TPR)) + 
#    geom_line(data = HTree_1_1, color = 'red') +
#    geom_line(data = J48_1_1, color = 'black') + 
#    labs(x = 'False Positive Rate', y = 'True Positive Rate (Recall)') + 
#    scale_x_continuous(expand = c(0, 0),limits = c(0,1.02)) + scale_y_continuous(expand = c(0, 0), limits = c(0,1.02))

#ggplot(NULL, aes(FPR, TPR)) + 
#    geom_line(data = HTree_1_10, color = 'red') +
#    geom_line(data = J48_1_10, color = 'black') + 
#    labs(x = 'False Positive Rate', y = 'True Positive Rate (Recall)') + 
#    scale_x_continuous(expand = c(0, 0),limits = c(0,1.02)) + scale_y_continuous(expand = c(0, 0), limits = c(0,1.02))

# ggplot(data = HTree_ROC_1_1, aes(FPR,TPR, color = 'red')) + 
#     geom_line() +
#     geom_line(data = J48_ROC_1_1, aes(FPR,TPR, color = 'blue')) +
#     scale_x_continuous(expand = c(0, 0),limits = c(0,1.02)) + scale_y_continuous(expand = c(0, 0), limits = c(0,1.02)) +
#     scale_color_manual(labels = c('C4.5, AUC: 0.9144', 'HTree, AUC: 0.9076'), values = c('red','black')) +
#     labs(x = 'False Positive Rate', y = 'True Positive Rate (Recall)', title = 'SlashDot, Undersampled: 1:1 Ratio') +
#     theme(plot.title = element_text(hjust = 0.5))    

ggplot(data = HTree_ROC_1_10, aes(FPR,TPR, color = 'red')) + 
    geom_line() +
    geom_line(data = J48_ROC_1_10, aes(FPR,TPR, color = 'blue')) +
    scale_x_continuous(expand = c(0, 0),limits = c(0,1.02)) + scale_y_continuous(expand = c(0, 0), limits = c(0,1.02)) +
    scale_color_manual(labels = c('C4.5', 'HTree'), values = c('red','black')) +
    labs(x = 'False Positive Rate', y = 'True Positive Rate (Recall)', colour = 'Models') +
    theme(plot.title = element_text(hjust = 0.5), 
          axis.title = element_text(size = 15),
          legend.text = element_text(size = 13),
          axis.text.x = element_text(size = 13),
          axis.text.y = element_text(size = 13))    

ggplot(data = HTree_PR_1_10, aes(Recall,Precision, color = 'red')) + 
    geom_line() +
    geom_line(data = J48_PR_1_10, aes(Recall,Precision, color = 'blue')) +
    scale_x_continuous(expand = c(0, 0),limits = c(0,1.02)) + scale_y_continuous(expand = c(0, 0), limits = c(0,1.02)) +
    scale_color_manual(labels = c('C4.5', 'HTree'), values = c('red','black')) +
    labs(x = 'Recall', y = 'Precision', colour = 'Models') +
    theme(plot.title = element_text(hjust = 0.5), 
          axis.title = element_text(size = 15),
          legend.text = element_text(size = 13),
          axis.text.x = element_text(size = 13),
          axis.text.y = element_text(size = 13))    

