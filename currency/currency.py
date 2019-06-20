from colour import Color
from pandas import *
from matplotlib import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from matplotlib import colors as mcolors

df = read_csv('../categories')

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
set_option('display.max_rows', 500)
figure(figsize=(24,18),dpi=200)
categories = df.groupby('currency')['currency'].count()
red = Color("gold")
colors = list(red.range_to(Color("blue"),len(categories)+10))

colors = [x.get_hex() for x in colors if len(x.get_hex())==7]


ax =categories.plot(kind='bar', color=colors,title= 'Currencies in use',fontsize=20)
ax.title.set_size(40)
ax.set_xlabel("Currency",fontsize=20)
ax.set_ylabel("Number of projects",fontsize=20)

plt.savefig('currency.png')

plt.clf()


figure(figsize=(10,8),dpi=200)
ax2 = categories.plot(kind='box',title= 'Currencies in use' )
ax2.title.set_size(30)
ax2.set_ylabel("Number of projects",fontsize=20)
plt.savefig('currency-box.png')