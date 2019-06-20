from colour import Color
from pandas import *
from matplotlib import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from matplotlib import colors as mcolors

df = read_csv('../categories')
set_option('display.max_columns', 500)
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
set_option('display.max_rows', 2000)
categories = df.groupby('backers')['backers'].count()
df1=categories.to_frame()
df2=df1.iloc[0].values.sum()
df3=df1.iloc[1].values.sum()
df4=df1.iloc[2:10].values.sum()
df5=df1.iloc[10:50].values.sum()
df6=df1.iloc[50:100].values.sum()
df7=df1.iloc[100:1000].values.sum()
df8=df1.iloc[1000:10000].values.sum()

figure(figsize=(7,5),dpi=200)
print(df1)
red = Color("gold")
colors = list(red.range_to(Color("blue"),len(categories)+10))
colors = [x.get_hex() for x in colors if len(x.get_hex())==7]


colors=colors[2:]
ax = plt.bar(["0","1","2-9","10-49","50-99","100-999","1000+"],[df2,df3,df4,df5,df6,df7,df8],color=colors)
plt.xlabel("Number of backers")
plt.ylabel("Number of projects")



plt.figtext(.5,.9,'Quantity of Backers', fontsize=20, ha='center')
plt.savefig('backers.png')



plt.clf()

pol = DataFrame({"backers": ["0","1","2-9","10-49","50-99","100-999","1000+"], "count": [df2,df3,df4,df5,df6,df7,df8]})

ax2 = pol.plot(kind='box',title= 'Quantity of backers' )

ax2.title.set_size(20)
ax2.set_ylabel("Number of projects",fontsize=5)
plt.savefig('backres-box.png')