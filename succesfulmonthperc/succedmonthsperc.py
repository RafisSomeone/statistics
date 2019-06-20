from colour import Color
from pandas import *
from matplotlib import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from matplotlib import colors as mcolors
from datetime import datetime


df = read_csv('../categories')
all_p = len(df)
df2 = df
df5 =df

df5 = df5[df.state != 'successful']
df5 = df5[df.state != 'live']

start5 = df5.launched
start5 = [x.split(" ")[0] for x in start5]
years5 = []
date_format = "%Y-%m-%d"
for i in range(len(start5)):
    date5 = datetime.strptime(start5[i], date_format)
    years5.append(date5.month)

df6 = DataFrame({"month":years5,"state":df5.state})
categories4 = df6.groupby('month')['month'].count()

start2 = df2.launched
start2 = [x.split(" ")[0] for x in start2]
years2 = []
date_format = "%Y-%m-%d"
for i in range(len(start2)):
    date2 = datetime.strptime(start2[i], date_format)
    years2.append(date2.month)

df4 = DataFrame({"month":years2,"state":df.state})
categories2 = df4.groupby('month')['month'].count()



df = df[df.state == 'successful']


mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
set_option('display.max_rows', 500)

start = df.launched
start = [x.split(" ")[0] for x in start]
years = []
date_format = "%Y-%m-%d"
for i in range(len(start)):
    date = datetime.strptime(start[i], date_format)
    years.append(date.month)

df3 = DataFrame({"month":years,"state":df.state})


categories = df3.groupby('month')['month'].count()


val = categories2.values
mon = categories.values

mon2 = categories4.values

result = [int(round((mon[i]/val[i])*100)) for i in range(len(val))]
result2 = [int(round((mon2[i]/val[i])*100)) for i in range(len(val))]

a = [str(i) for i in range(1,13)]

pol = DataFrame({'successful':result,"failed":result2})
pol.index +=1
print(pol)

plt.clf()

ax =pol.plot(kind='bar', color=["gold","green"],title= 'Failed and successful projects per months',fontsize=20,ylim=(0,100))
ax.set_xlabel("Months",fontsize=10)
ax.set_ylabel("Percent of project",fontsize=10)
ax.title.set_size(17)

plt.savefig('successmonthperc.png',bbox_inches="tight", pad_inches=0.1,dpi=200)




