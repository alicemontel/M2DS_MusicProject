import pandas as pnd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
matplotlib.rcParams.update({'font.size': 16})

data = pnd.read_csv('../Source/responses.csv')
pnd.set_option('display.max_columns',200)
data.head(2)
#print data
#print data.shape
#(1010,150)
print data.describe()


music = data.iloc[0:,1:19].copy()

fig = plt.figure(figsize=(18,18))
ax = fig.add_subplot(111)
cax = ax.matshow(music.corr())
fig.colorbar(cax)
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.set_xticklabels([' ']+music.columns.tolist()  ,rotation=90 )
ax.set_yticklabels([' ']+music.columns.tolist()   )

plt.show()
