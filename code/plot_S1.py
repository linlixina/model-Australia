import numpy as np
import pandas as pd
import math
import xlrd
import xlwt
import pyecharts.options as opts
from pyecharts.charts import Pie
import seaborn as sns
import sci_palettes
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import matplotlib as mpl
from matplotlib import cm
from matplotlib.pyplot import MultipleLocator

#Fig A
data= pd.read_csv("model-Australia/data/death-data-Australia.csv")
x = data.iloc[:, 0] 
y4 = data.iloc[:, 4]
data.head()
fig, ax = plt.subplots(figsize=(11,6.5))
ax.bar(data['Date'], data['reported deaths (NSW)'], width=0.5, label='reported deaths',color='#fee1d3')
ax.bar(data['Date'], data['under-reported deaths (NSW)'], width=0.5, bottom=data['reported deaths (NSW)'],label='under-reported deaths',color='#fd9272')
ax.bar(data['Date'], data['unreported deaths (NSW)'], width=0.5, bottom=data['reported deaths (NSW)']+data['under-reported deaths (NSW)'] ,label='unreported deaths',color='#cb181c')
ax.set_ylabel('Weekly COVID-19 deaths', fontsize=12)
ax.plot(x, y4, 'o-',color='#630000',markersize=4,label='deaths (AUS)')
plt.xlabel("Timepoint in 2021–22 (weeks)", fontsize=12)
plt.xticks(data['Date'][[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46]],size=10.5,rotation=45)
plt.yticks(size=10.5)
plt.legend(frameon=False, prop={'size':10.5})
plt.savefig("model-Australia/Figures/Fig_A.svg", format="svg", dpi=300, bbox_inches='tight')


#Fig B
labels = ['50$^-$', '50-69', '70$^+$']    
colors = ['#778899', '#334455', '#cb181c']         
sizes = [111+7,468+38,2707+282]                 
explode = [i/sum(sizes)*0.1 for i in sizes]
plt.figure(figsize=(6, 4))
plt.pie(sizes, labels=labels, explode=explode, colors=colors, autopct='%1.1f%%', startangle=-240,textprops = { "fontsize" : 7.5 })
plt.axis('equal')
plt.title('COVID-19 deaths', fontsize=9,weight = 'bold')
plt.legend(frameon=False, prop={'size':7.5})
plt.savefig("model-Australia/Figures/Fig_B.svg", format="svg", dpi=300, bbox_inches='tight')


#Fig C
df = pd.read_csv("model-Australia/data/death-data-70.csv")
x = df.iloc[:, 0] 
y_1 = df.iloc[:, 1]
y_2 = df.iloc[:, 2]
y_3 = df.iloc[:, 3]
y_4 = df.iloc[:, 4]
y_5 = df.iloc[:, 5]
y_6 = df.iloc[:, 6]
fig, ax = plt.subplots(figsize=(11, 6.5))
labels = x
left_bottom_data = y_1
left_middle_data = y_2
left_top_data = y_3
width = 0.3
ax.bar(np.arange(len(left_bottom_data)), left_bottom_data, width=width, tick_label=labels, label="No dose (reported deaths)",color='#9ecbe2')
ax.bar(np.arange(len(left_middle_data)), left_middle_data,bottom=left_bottom_data, width=width, tick_label=labels, label="One dose (reported deaths)",color='#6bafd6')
ax.bar(np.arange(len(left_top_data)), left_top_data, bottom=left_bottom_data+left_middle_data, width=width, tick_label=labels,label="Two or more doses (reported deaths)",color='#2271b6')

right_bottom_data = y_4
right_middle_data = y_5
right_top_data = y_6
ax.bar(np.arange(len(right_bottom_data))+width, right_bottom_data, width=width, tick_label=labels, label="No dose (total deaths)",color='#fd9272')
ax.bar(np.arange(len(right_middle_data))+width, right_middle_data, bottom=right_bottom_data,width=width, tick_label=labels, label="One dose (total deaths)",color='#fb6a4b')
ax.bar(np.arange(len(right_top_data))+width, right_top_data, bottom=right_bottom_data + right_middle_data, width=width, tick_label=labels,label="Two or more doses (total deaths)",color='#cb181c')
ax.set_ylabel('Weekly COVID-19 deaths', fontsize=12)
plt.xlabel("Timepoint in 2021–22 (weeks)", fontsize=12)
plt.legend(frameon=False, prop={'size':10.5})
y=np.arange(len(labels))
plt.yticks(size=10.5)
plt.xticks(size=10.5,rotation=45)
plt.xticks(y+width/2,['Nov 20','Nov 27', 'Dec 4','Dec 11','Dec 18','Dec 25', 'Jan 1','Jan 8', 'Jan 15','Jan 22','Jan 29','Feb 5','Feb 12'],size=10.5,rotation=45)
plt.savefig("model-Australia/Figures/Fig_C.svg", format="svg", dpi=300, bbox_inches='tight')




#Fig E
plt.subplots(figsize=(9, 6))
ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
df = pd.read_csv("model-Australia/data/vaccination-data.csv")
x = df.iloc[:, 0] 
y_1 = df.iloc[:, 1]
y_2 = df.iloc[:, 2]
y_3 = df.iloc[:, 3]
y_4 = df.iloc[:, 4]
plt.plot(x, y_1,'-',color='#842A82',label='1$st$ dose (NSW_50+)')
plt.plot(x, y_2,'-',color='#B68833',label='2$nd$ dose (NSW_50+)')
plt.plot(x, y_3,'--',color='#1D5F9B',label='3$rd$ dose (NSW_50+)')
plt.plot(x, y_4,'-',color='grey',label='3$rd$ dose (VIC_50+)')
plt.ylim((-0.05, 1))
plt.xlim((-2, 46+12))
plt.scatter([-4/7+12],[0],s=12,c='black') 
plt.text(-4/7+1.75+12, 0+0.02, 'NSW, 50+\n($Oct$ $16$, 0)', ha='center', va='bottom', fontsize=7.5)
plt.scatter([15+4/7+12],[0.5903],s=12,c='black') 
plt.text(15+13/7+4.2+12, 0.5903-0.08, 'NSW, 50+\n($Feb$ $6$, 0.5903)', ha='center', va='bottom', fontsize=7.5)
plt.scatter([7+5/7+12],[0.0701],s=12,c='red') 
plt.scatter([9+5/7+12],[0.1773],s=12,c='red') 
plt.scatter([11+5/7+12],[0.2675],s=12,c='red') 
plt.scatter([13+5/7+12],[0.4966],s=12,c='red') 
plt.scatter([15+5/7+12],[0.5709],s=12,c='red') 
plt.scatter([17+5/7+12],[0.6339],s=12,c='red') 
plt.scatter([44+4/7+12],[0.7376],s=12,c='black') 
plt.text(44+4/7+6, 0.672, 'NSW, 30+\n($Aug$ $28$, 0.7376)', ha='center', va='bottom', fontsize=7.5)
plt.scatter([44+4/7+12],[0.9389],s=12,c='black') 
plt.text(44+4/7+6, 0.874, 'NSW, 65+\n($Aug$ $28$, 0.9389)', ha='center', va='bottom', fontsize=7.5)
plt.yticks(size=7.5)
plt.ylim(top=1)
y_major_locator=MultipleLocator(0.1)
ax.yaxis.set_major_locator(y_major_locator)
plt.xticks(x[[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56]],size=9,rotation=45)
plt.legend(frameon=False,ncol=1,loc="best", prop={'size':7.5})
plt.xlabel("Timepoint in 2021–22 (weeks)", fontsize=10)
plt.ylabel('Vaccine coverage of 1$st$/2$nd$/3$rd$ dose, 50+', fontsize=10) 
plt.savefig("model-Australia/Figures/Fig_E.svg", format="svg", dpi=300, bbox_inches='tight')



#Fig F
fig, ax = plt.subplots(figsize=(7.6,5))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
df = pd.read_csv("model-Australia/Results/Reconstructed_two-dose_mortality_rate.csv")
x = df.iloc[:, 0]
y_1 = df.iloc[:, 1]
y_3 = df.iloc[:, 2]
plt.plot(x, y_1,'o-',color='red',markersize=3,label='r$_2$($t$)') 
plt.plot(x, y_3,'o-',color='grey',markersize=3,label='r$_{2a}$($t$)') 
plt.xticks(x[[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46]],size=9.5,rotation=45)
plt.yticks(size=9.5)
plt.ylim(-1,12)
y_major_locator=MultipleLocator(2)
plt.legend(frameon=False, prop={'size':9.5})
plt.xlabel("Timepoint in 2021–22 (weeks)", fontsize=11)
plt.ylabel("Weekly COVID-19 death rates (*$10^{-5}$)", fontsize=11)
plt.savefig("model-Australia/Figures/Fig_F.svg", format="svg", dpi=300, bbox_inches='tight')



#Fig G
plt.subplots(figsize=(9, 6))
df = pd.read_csv("model-Australia/Results/scenario_1.csv")
ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
x = df.iloc[:, 0]
y_1 = df.iloc[:, 1]
y_2 = df.iloc[:, 2]
y_3 = df.iloc[:, 3]
y_4 = df.iloc[:, 4]
y_5 = df.iloc[:, 5]
plt.plot(x, y_1,'o-',color='#000000',markersize=3,label='actual') 
plt.plot(x, y_2,'s-',color='#1D5F9B',markersize=3,label='scenario I (simple)') 
plt.plot(x, y_3,'o-',color='grey',markersize=3,label='scenario I (improved)') 
plt.fill_between(x, y_4, y_5, color='grey',alpha=0.5)
plt.ylim(-10,400)
plt.xticks(x[[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46]],size=9.5,rotation=45)
plt.yticks(size=9.5)
plt.legend(frameon=False, prop={'size':9.5},bbox_to_anchor=(0.955,0.965))
plt.ylabel("Weekly COVID-19 Deaths", fontsize=11)
plt.xlabel("Timepoint in 2021–22 (weeks)", fontsize=11)
plt.savefig("model-Australia/Figures/Fig_G.svg", format="svg", dpi=300, bbox_inches='tight')



#Fig I
df = pd.read_csv("model-Australia/Results/scenario_3.csv") # 打开Excel--.csv文件
x = df.iloc[:, 0] 
y = df.iloc[:, 2]
y_1 = df.iloc[:, 3]
y_2 = df.iloc[:, 4]
plt.subplots(1, 3, figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.plot(x,y,color='purple')
plt.fill_between(x, y_1, y_2, color='purple',alpha=0.2)
plt.yticks(size=9.5)
plt.xticks(x[[0,4,8,12,16,20,24,28,32,36,40,44,48]],size=8.5,rotation=50)
plt.title("$I(t)$", fontsize=12)
plt.ylabel("cases", fontsize=12)


x = df.iloc[:, 0] 
y = df.iloc[:, 5]
y_1 = df.iloc[:, 6]
y_2 = df.iloc[:, 7]
plt.subplot(1, 3, 2)
plt.plot(x,y,color='blue')
plt.fill_between(x, y_1, y_2, color='blue',alpha=0.2)
plt.yticks(size=9.5)
plt.xticks(x[[0,4,8,12,16,20,24,28,32,36,40,44,48]],size=8.5,rotation=50)
plt.title("$S(t)$", fontsize=12)
plt.xlabel("Timepoint in 2021–22 (weeks)", fontsize=12)


x = df.iloc[:, 0] 
y = df.iloc[:, 8]
y_1 = df.iloc[:, 9]
y_2 = df.iloc[:, 10]
plt.subplot(1, 3, 3)
plt.plot(x,y,color='red')
plt.fill_between(x, y_1, y_2, color='red',alpha=0.2)
plt.title("$D(t)$", fontsize=12)
plt.yticks(size=9.5)
plt.xticks(x[[4,10,16,22,28,34,40,46]],size=8.5,rotation=45)
plt.xticks(x[[0,4,8,12,16,20,24,28,32,36,40,44,48]],size=8.5,rotation=50)
plt.savefig("model-Australia/Figures/Fig_I.svg", format="svg", dpi=300, bbox_inches='tight')