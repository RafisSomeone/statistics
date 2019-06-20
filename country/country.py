from pandas import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from matplotlib import colors as mcolors
from colour import Color
from matplotlib import cm
from colorspacious import cspace_converter
from collections import OrderedDict

red = Color("red")

df = read_csv('../categories')

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
set_option('display.max_rows', 500)
figure(figsize=(10,10),dpi=200)
categories = df.groupby('country')['country'].count()

red = Color("gold")
colors = list(red.range_to(Color("blue"),len(categories)+10))

colors = [x.get_hex() for x in colors if len(x.get_hex())==7]


ax =categories.plot(kind='bar',title= 'Quantity of projects for country',color=colors,legend=False)
ax.set_xlabel("Country")
ax.set_ylabel("Number of projects")

ax.title.set_size(20)



plt.savefig('country.png')

plt.clf()


figure(figsize=(10,8),dpi=200)
ax2 = categories.plot(kind='box',title= 'Quantity of projects for country' )
ax2.title.set_size(30)
ax2.set_ylabel("Number of projects",fontsize=20)
plt.savefig('country-box.png')

# categories_quantity = DataFrame(categories.groupby("category").agg(['count']))
# print(categories_quantity)


# categories_quantity.plot.bar()


# asd =categories_quantity.boxplot()
# asd.plot()
# plt.show()

# df3 = DataFrame(df['state'])
# print(df3.groupby(['state']).size())
#
# df4 = DataFrame(df['main_category'])
# print(df4.groupby(['main_category']).size())

# df2.boxplot(column='category')