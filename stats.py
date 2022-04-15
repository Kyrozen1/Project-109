import statistics
import pandas as pd
import plotly.figure_factory as ff
import csv

df=pd.read_csv("StudentsPerformance.csv")
mathScore = df["math score"].tolist()
mean = statistics.mean(mathScore)
median = statistics.median(mathScore)
mode = statistics.mode(mathScore)
standDiviation= statistics.stdev(mathScore)
print("The mean is --> "+str(mean))
print("The median is --> "+str(median))
print("The mode is --> "+str(mode))
print("The standard diviation is --> "+str(standDiviation))

fig=ff.create_distplot([df["math score"].tolist()],["score"], show_hist=False)
fig.show()

fsd_start,fsd_end=mean-standDiviation,mean+standDiviation
ssd_start,ssd_end=mean-(2*standDiviation),mean+(2*standDiviation)
tsd_start,tsd_end=mean-(3*standDiviation),mean+(3*standDiviation)

mathScore_of_data_lies_within_standardDiviation = [result for result in mathScore if result > fsd_start and result < fsd_end]
mathScore_of_data_lies_within_2standardDiviation = [result for result in mathScore if result > ssd_start and result < ssd_end]
mathScore_of_data_lies_within_3standardDiviation = [result for result in mathScore if result > tsd_start and result < tsd_end]

print("{}% of data for height lies within first standardDiviation".format(len(mathScore_of_data_lies_within_standardDiviation)*100.0/len(mathScore)))
print("{}% of data for height lies within second standardDiviation".format(len(mathScore_of_data_lies_within_2standardDiviation)*100.0/len(mathScore)))
print("{}% of data for height lies within third standardDiviation".format(len(mathScore_of_data_lies_within_3standardDiviation)*100.0/len(mathScore)))