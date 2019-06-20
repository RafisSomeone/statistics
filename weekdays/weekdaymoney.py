from colour import Color
from pandas import *
from matplotlib import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from matplotlib import colors as mcolors
from datetime import datetime
import calendar

df = read_csv('../categories')
# df = df[df.state == 'successful']
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
set_option('display.max_rows', 500)
figure(figsize=(30, 27), dpi=200)
start = df.launched
start = [x.split(" ")[0] for x in start]
weekdays = []
date_format = "%Y-%m-%d"
for i in range(len(start)):
    date = datetime.strptime(start[i], date_format)
    weekdays.append(date.weekday())



df3 = DataFrame({"weekdays":weekdays, "state":df.state})

categories = df3.groupby(['weekdays','state']).size()

red = Color("gold")
colors = list(red.range_to(Color("blue"),5))
colors = [x.get_hex() for x in colors if len(x.get_hex())==7]
colors=colors[2:]

z=categories.index.set_levels([[calendar.day_name[i]for i in range(0,7)], ['canceled', 'failed', 'live', 'successful', 'suspended']])
categories.index=z

ax =categories.plot(kind='bar', color=['yellow','red','blue','lime','purple'],title= 'Money collected by projects started in particular years',fontsize=20)
ax.set_xlabel("Years",fontsize=25)
ax.set_ylabel("Collected money [USD]",fontsize=25)
ax.title.set_size(40)


plt.savefig('yearsmoney.png',bbox_inches="tight", pad_inches=0.1)
#
# plt.clf()
#
#
# figure(figsize=(10,8),dpi=200)
# ax2 = categories.plot(kind='box',title= 'Money collected by projects started in particular years' )
# ax2.title.set_size(30)
# ax2.set_ylabel("Collected money [USD]",fontsize=20)
# plt.savefig('yearsmoney-box.png')
