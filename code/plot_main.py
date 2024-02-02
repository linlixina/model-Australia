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

#Fig 1
df = pd.read_csv("model-Australia/data/owid-covid-data.csv")
x = df.iloc[:, 0] 
xx = df.iloc[:, 9]
y1 = df.iloc[:, 1]
y2 = df.iloc[:, 2]
y3 = df.iloc[:, 3]
y4 = df.iloc[:, 5]
y5 = df.iloc[:, 6]
y6 = df.iloc[:, 7]
y7 = df.iloc[:, 8]
import numpy as np
xxx = xx.replace(np.nan, '', regex=True)
fig = plt.figure(figsize=(15,9))
ax1=fig.add_subplot(111)
ax1.bar(x, y4,label="Confirmed cases (without Omicron VOC)",color='#000000')
ax1.bar(x, y7,label="Confirmed cases (with Omicron VOC)",color='red')
plt.xticks(x[[0, 59, 120, 181, 243, 304, 365, 424,485, 546,608,669,730]],
    ['Jan-21', 'Mar-21','May-21', 'Jul-21','Sep-21','Nov-21','Jan-22','Mar-22','May-22', 'Jul-22','Sep-22','Nov-22','Jan-23']
               ,size=12,rotation=35)
plt.yticks(size=12)
plt.ylim(0,120)
plt.legend(frameon=False, prop={'size':12})
ax2=ax1.twinx()
ax2.plot(x, y1,'o-',markersize=0.8,label="1st dose",color='#842A82')
ax2.plot(x, y2,'o-',markersize=0.8,label="2nd dose",color='#B68833')
ax2.plot(x, y3,'o-',markersize=0.8, label="booster doses",color='#FF9483')
ax2.plot(x, y5,'o-',markersize=0.8, label="booster doses (Israel)",color='#1D5F9B')
plt.annotate(r'$i$', xy=(52, 82), xytext=(-41, -3.8), ha='center',textcoords='offset points', fontsize=12,arrowprops = dict(arrowstyle="-|>,head_width=0.2,head_length=0.4",shrinkA=0,shrinkB=0))
plt.annotate(r'$ii$', xy=(132, 67), xytext=(-41, -3.8),ha='center', textcoords='offset points', fontsize=12,arrowprops=dict(arrowstyle="-|>,head_width=0.2,head_length=0.4",shrinkA=0,shrinkB=0))
plt.annotate(r'$iii$', xy=(151, 52), xytext=(-41, -3.8), ha='center',textcoords='offset points', fontsize=12,arrowprops=dict(arrowstyle="-|>,head_width=0.2,head_length=0.4",shrinkA=0,shrinkB=0))
plt.annotate(r'$iv$', xy=(311, 37), xytext=(-41, -3.8),ha='center', textcoords='offset points', fontsize=12,arrowprops=dict(arrowstyle="-|>,head_width=0.2,head_length=0.4",shrinkA=0,shrinkB=0))
plt.annotate("", xy=(224, 10), xytext=(367, 10),arrowprops=dict(arrowstyle="<->"))
plt.text(263,12,r'20 weeks', fontdict={'size':12})
ax2.plot([52, 52], [0, 108], c='grey', linestyle='--')
ax2.plot([132, 132], [0, 108], c='grey', linestyle='--')
ax2.plot([151, 151], [0, 108], c='grey', linestyle='--')
ax2.plot([311, 311], [0, 108], c='grey', linestyle='--')
x11 = x[50:] 
y11 = y1[50:]
mask = np.isfinite(y11)
line, = ax2.plot(x11[mask],y11[mask], ls="--",lw=1,color='#842A82')
x111 = x[52:] 
y22 = y2[52:]
mask = np.isfinite(y22)
line, = ax2.plot(x111[mask],y22[mask], ls="--",lw=1,color='#B68833')
x1111 = x[278:] 
y33 = y3[278:]
mask = np.isfinite(y33)
line, = ax2.plot(x1111[mask],y33[mask], ls="--",lw=1,color='#FF9483')
plt.ylim(0,100)
plt.legend(ncol=2,frameon=False, prop={'size':12})
plt.yticks(size=12)
ax1.set_xlabel("Timepoint in 2021–23 (months)", fontsize=14)
ax1.set_ylabel("Confirmed COVID-19 cases (*$10^{3}$)", fontsize=14)
ax2.set_ylabel("1st/2nd/boosters dose of vaccine per 100 persons", fontsize=14)
plt.savefig("model-Australia/Figures/Fig_1.svg", format="svg", dpi=300, bbox_inches='tight')



#Fig 2
plt.subplots(1, 2, figsize=(13, 5))
plt.subplot(1, 2, 1)
ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

data= pd.read_csv("model-Australia/data/death-data.csv")
data.head()
ax.bar(data['Date'], data['No dose'], width=0.55, label='No dose',color="#fee1d3")
ax.bar(data['Date'], data['One dose'], width=0.55, bottom=data['No dose'],label='One dose',color="#fd9272")
ax.bar(data['Date'], data['Two doses'], width=0.55, bottom=data['No dose']+data['One dose'] ,label='Two doses',color="#cb181c")
ax.bar(data['Date'], data['Three or more doses'], width=0.55, bottom=data['No dose']+data['One dose']+data['Two doses'] ,label='Three or more doses',color="#630000")
ax.set_ylabel('Weekly COVID-19 deaths', fontsize=9.5)
plt.xlabel("Timepoint in 2021–22 (weeks)", fontsize=9.5)
ax.legend(prop={'size':8})
plt.xticks(data['Date'][[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46]],size=8,rotation=50)
plt.yticks(size=8)
plt.ylim(0,400)
plt.legend(frameon=False, prop={'size':10.5},bbox_to_anchor=(0.955,0.965))
plt.text(-2.3, 400, 'a', ha='center', va='bottom', fontsize=11 ,weight = 'bold')
plt.legend(frameon=False, prop={'size':8},bbox_to_anchor=(0.39,0.995))

plt.subplot(1, 2, 2)
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
plt.text(-4/7+1.75+12, 0+0.02, 'NSW, 50+\n($Oct$ $16$, 0)', ha='center', va='bottom', fontsize=8)
plt.scatter([15+4/7+12],[0.5903],s=12,c='black') 
plt.text(15+13/7+4.2+12, 0.5903-0.08, 'NSW, 50+\n($Feb$ $6$, 0.59)', ha='center', va='bottom', fontsize=8)
plt.scatter([7+5/7+12],[0.0701],s=12,c='red') 
plt.scatter([9+5/7+12],[0.1773],s=12,c='red') 
plt.scatter([11+5/7+12],[0.2675],s=12,c='red') 
plt.scatter([13+5/7+12],[0.4966],s=12,c='red') 
plt.scatter([15+5/7+12],[0.5709],s=12,c='red') 
plt.scatter([17+5/7+12],[0.6339],s=12,c='red') 
plt.scatter([44+4/7+12],[0.7376],s=12,c='black') 
plt.text(44+4/7+6, 0.672, 'NSW, 30+\n($Aug$ $28$, 0.74)', ha='center', va='bottom', fontsize=8)
plt.scatter([44+4/7+12],[0.9389],s=12,c='black') 
plt.text(44+4/7+6, 0.874, 'NSW, 65+\n($Aug$ $28$, 0.94)', ha='center', va='bottom', fontsize=8)
plt.yticks(size=8)
plt.ylim(top=1)
y_major_locator=MultipleLocator(0.1)
ax.yaxis.set_major_locator(y_major_locator)
plt.xticks(x[[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56]],size=8,rotation=55)
plt.legend(frameon=False,ncol=1,loc="best", prop={'size':8})
plt.xlabel("Timepoint in 2021–22 (weeks)", fontsize=9.5)
plt.ylabel('Vaccine coverage of 1$st$/2$nd$/3$rd$ dose, 50+', fontsize=9.5) 
plt.text(-0.6, 1, 'b', ha='center', va='bottom', fontsize=11 ,weight = 'bold')
plt.subplots_adjust(wspace=0.15,hspace=0)
plt.savefig("model-Australia/Figures/Fig_2.svg", format="svg", dpi=300, bbox_inches='tight')



#Fig 3
plt.subplots(figsize=(10, 6))
df = pd.read_csv("model-Australia/Results/Proportion_unvaccinated_deaths&population.csv")
x = df.iloc[:, 0] 
y_1 = df.iloc[:, 3]
y_2 = df.iloc[:, 4]
plt.plot(x, y_1,'o-',color='#F14B0d',markersize=5,label='Weekly (unvaccinated,aged 50+, NSW)')
plt.plot(x, y_2,'o-',color='purple',markersize=5,label='Proportion of unvaccinated population (aged 50+, NSW)')
xx = [[0, 17+4/7], [0, 24+4/7],[20, 45+3/7], [43+6/7, 69+6/7]]
x1 = [17/2+4/14, 12+2/7,65/2+3/14, 43/2+6/14+69/2+3/7]
y = [[0.75, 0.75], [0.49, 0.49],[0.37, 0.37], [0.44, 0.44]]

for i in range(0, 1):
    plt.scatter(xx[i], y[i],color='#ADB6B6FF', s=30)
    plt.annotate(str(y[i][0])+' (not fully vaccinated, VIC)', xy=(x1[i], y[i][0]), xytext=(+140, -22), ha='center', textcoords='offset points', fontsize=10.5,arrowprops = dict(arrowstyle="-|>,head_width=0.2,head_length=0.4",shrinkA=0,shrinkB=0,color='#000000'))
    plt.plot(xx[i], y[i],color='#ADB6B6FF')

for i in range(1, 2):
    plt.scatter(xx[i], y[i],color='#ADB6B6FF', s=30)
    plt.annotate(str(y[i][0])+' (unvaccinated, VIC)', xy=(x1[i], y[i][0]), xytext=(+130, 30), ha='center', textcoords='offset points', fontsize=10.5,arrowprops = dict(arrowstyle="-|>,head_width=0.2,head_length=0.4",shrinkA=0,shrinkB=0,color='#000000'))
    plt.plot(xx[i], y[i],color='#ADB6B6FF')

for i in range(2, 3):
    plt.scatter(xx[i], y[i],color='#ADB6B6FF', s=30)
    plt.annotate(str(y[i][0])+' (unvaccinated, VIC)', xy=(x1[i], y[i][0]), xytext=(+25, +40), ha='center', textcoords='offset points', fontsize=10.5,arrowprops = dict(arrowstyle="-|>,head_width=0.2,head_length=0.4",shrinkA=0,shrinkB=0,color='#000000'))
    plt.plot(xx[i], y[i],color='#ADB6B6FF')

for i in range(3, 4):
    plt.scatter(xx[i], y[i],color='#ADB6B6FF', s=30)
    plt.annotate(str(y[i][0])+' (unvaccinated, VIC)', xy=(x1[i], y[i][0]), xytext=(+25, +40), ha='center', textcoords='offset points', fontsize=10.5,arrowprops = dict(arrowstyle="-|>,head_width=0.2,head_length=0.4",shrinkA=0,shrinkB=0,color='#000000'))
    plt.plot(xx[i], y[i],color='#ADB6B6FF')
plt.xticks(x[[0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69]],size=10.5,rotation=45)
plt.ylim(-0.04,1)
plt.legend(frameon=False, prop={'size':10.5},bbox_to_anchor=(0.9785,0.975))
plt.xlabel("Timepoint in 2021–22 (weeks)", fontsize=12)
plt.yticks([0,0.05,0.2,0.4,0.6,0.8,1],size=10.5)
plt.ylabel("Proportion of unvaccinated COVID-19 deaths", fontsize=12)
plt.axhline(y=0.05, color='black', linestyle='dashed')
plt.axhline(y=0, color='black', linestyle='dashed')
plt.savefig("model-Australia/Figures/Fig_3.svg", format="svg", dpi=300, bbox_inches='tight')



#Fig 4
plt.subplots(1, 2, figsize=(13, 5))
plt.subplot(1, 2, 1)
ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
df = pd.read_csv("model-Australia/Results/death-rate-50.csv")
x = df.iloc[:, 0] 
y_1 = df.iloc[:, 1]
y_2 = df.iloc[:, 2]
y_3 = df.iloc[:, 3]
y_4 = df.iloc[:, 4]
plt.plot(x, y_1,'d-',color="#842A82",markersize=3,label='No dose') 
plt.plot(x, y_2,'x-',color="#000000",markersize=3,label='Only one dose') 
plt.plot(x, y_3,'o-',color="#F14B0d",markersize=3,label='Two effective doses') 
plt.plot(x, y_4,'v-',color="#1D5F9B",markersize=3,label='Three or more doses') 
plt.ylabel("VS Death Rates (*$10^{-5}$)", fontsize=9.5)
plt.xlabel("Timepoint in 2021–22 (weeks)", fontsize=9.5)
plt.xticks(x[[0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45]],size=8,rotation=45)
plt.ylim(top=90)
y_major_locator=MultipleLocator(10)
ax.yaxis.set_major_locator(y_major_locator)
plt.yticks(size=8)
plt.text(-2.3, 90, 'a', ha='center', va='bottom', fontsize=11 ,weight = 'bold')
plt.legend(frameon=False, prop={'size':8},bbox_to_anchor=(0.39,0.995))

plt.subplot(1, 2, 2)
ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

df = pd.read_csv("model-Australia/Results/death-rate-70&aged_care.csv")
x = df.iloc[:, 0] 
y_1 = df.iloc[:, 1]
y_2 = df.iloc[:, 2]
y_3 = df.iloc[:, 3]
y_4 = df.iloc[:, 4]
y_5 = df.iloc[:, 5]
plt.plot(x, y_1,'o-',color='#F14B0d',markersize=3,label='70+, No dose in NSW') 
plt.plot(x, y_2,'^-',color='#1D5F9B',markersize=3,label='70+, Only one dose in NSW') 
plt.plot(x, y_3,'s-',color='#B68833',markersize=3,label='70+, Two or more doses in NSW') 
plt.plot(x, y_4,'v-',color='#842A82',markersize=3,label='Aged care residents in NSW') 
plt.plot(x, y_5,'d-',color='#000000',markersize=3,label='Aged care residents in VIC') 
plt.ylabel("Weekly COVID-19 death rates (*$10^{-5}$)", fontsize=9.5)
plt.xlabel("Timepoint in 2021–22 (weeks)", fontsize=9.5)
plt.xticks(size=8,rotation=40)
plt.yticks(size=8)
plt.ylim(-15,400)
plt.legend(frameon=False, prop={'size':8},bbox_to_anchor=(0.52,0.997))
plt.text(-0.6, 400, 'b', ha='center', va='bottom', fontsize=11 ,weight = 'bold')
plt.subplots_adjust(wspace=0.15,hspace=0)
plt.savefig("model-Australia/Figures/Fig_4.svg", format="svg", dpi=300, bbox_inches='tight')



#Fig 5
plt.subplots(3, 1, figsize=(6.6, 10.5))

plt.subplot(3, 1, 1)
ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
df = pd.read_csv("model-Australia/Results/cumulative_deaths.csv")
x = df.iloc[:, 0]
y_1 = df.iloc[:, 1]
y_2 = df.iloc[:, 2]
y_3 = df.iloc[:, 3]
y_4 = df.iloc[:, 4]
plt.plot(x, y_1,'-',color='grey',label='actual') 
plt.plot(x, y_2,'-',color='orange',label='scenario I')
plt.fill_between(x, y_3, y_4, color='orange',alpha=0.5)
plt.ylim(0,3500)
plt.text(-2.3, 3500, 'a', ha='center', va='bottom', fontsize=11 ,weight = 'bold')
plt.yticks(size=9)
plt.legend(frameon=False, prop={'size':9},bbox_to_anchor=(0.28,1))
plt.xticks(x[[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46]],size=9,rotation=45)
plt.subplots_adjust(wspace=0,hspace=0.1)
plt.gca().xaxis.set_ticklabels([])


plt.subplot(3, 1, 2)
ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
x = df.iloc[:, 0]
y_1 = df.iloc[:, 1]
y_2 = df.iloc[:, 5]
y_3 = df.iloc[:, 6]
y_4 = df.iloc[:, 7]
plt.plot(x, y_1,'-',color='grey',label='actual') 
plt.plot(x, y_2,'-',color='red',label='scenario II')
plt.fill_between(x, y_3, y_4, color='red',alpha=0.5)
plt.ylim(0,6000)
plt.text(-2.3, 6000, 'b', ha='center', va='bottom', fontsize=11 ,weight = 'bold')
plt.ylabel("Cumulative COVID-19 Deaths", fontsize=12)
plt.xticks(x[[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46]],size=9,rotation=45)
plt.yticks(size=9)
plt.gca().xaxis.set_ticklabels([])
plt.legend(frameon=False, prop={'size':9},bbox_to_anchor=(0.28,1))


plt.subplot(3, 1, 3)
ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
x = df.iloc[:, 0]
y_1 = df.iloc[:, 1]
y_2 = df.iloc[:, 8]
y_3 = df.iloc[:, 9]
y_4 = df.iloc[:, 10]
plt.plot(x, y_1,'-',color='grey',label='actual') 
plt.plot(x, y_2,'-',color='black',label='scenario III')
plt.fill_between(x, y_3, y_4, color='black',alpha=0.5)
plt.ylim(0,25000)
plt.text(-2.3, 25000, 'c', ha='center', va='bottom', fontsize=11 ,weight = 'bold')
plt.yticks(size=9)
plt.legend(frameon=False, prop={'size':9},bbox_to_anchor=(0.28,1))
plt.xticks(x[[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46]],size=9,rotation=45)
plt.subplots_adjust(wspace=0,hspace=0.1)
plt.xlabel("Timepoint in 2021–22 (weeks)", fontsize=12)

plt.savefig("model-Australia/Figures/Fig_5.svg", format="svg", dpi=300, bbox_inches='tight')