from colour import Color
from pandas import *
from matplotlib import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from matplotlib import colors as mcolors
from datetime import datetime

df = read_csv('../categories')

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
set_option('display.max_rows', 500)
figure(figsize=(30, 18), dpi=200)
start = df.launched
start = [x.split(" ")[0] for x in start]
month = []
date_format = "%Y-%m-%d"
for i in range(len(start)):
    date = datetime.strptime(start[i], date_format)
    month.append(date.month)

df3 = DataFrame({"month":month, "usd_pledged_real":df.usd_pledged_real})

categories = df3.groupby('month')['month'].sum()

red = Color("gold")
colors = list(red.range_to(Color("blue"),len(categories)+10))
colors = [x.get_hex() for x in colors if len(x.get_hex())==7]
colors=colors[2:]

ax =categories.plot(kind='bar', color=colors,title= 'Money collected by projects started in particular months',fontsize=20)
ax.set_xlabel("Months",fontsize=25)
ax.set_ylabel("Collected money [USD]",fontsize=25)
ax.title.set_size(40)

plt.savefig('monthmoney.png')

plt.clf()


figure(figsize=(10,8),dpi=200)
ax2 = categories.plot(kind='box',title= 'Money collected by projects started in particular months' )
ax2.title.set_size(20)
ax2.set_ylabel("Collected money [USD]",fontsize=20)
plt.savefig('monthmoney-box.png')
