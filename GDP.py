import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl
from cycler import cycler

df = pd.read_csv('gdp_data.csv')

plt.style.use('TheEconomist.mplstyle')

fig, ax = plt.subplots()
USA = df[df['Country Code'] == 'USA']
Russia = df[df['Country Code'] == 'RUS']
China = df[df['Country Code'] == 'CHN']

plt.plot(USA['Year'], USA['Value'] / 1_000_000_000_000,
         label='USA GDP')
plt.plot(Russia['Year'], Russia['Value'] / 1_000_000_000_000,
         label='Russia GDP')
plt.plot(China['Year'], China['Value'] / 1_000_000_000_000,
         label='China GDP')

plt.title('USA, China and Russia GDP, $t',fontsize=20, fontweight='bold')
plt.xlabel("Year")
plt.ylabel("GDP in Trillions of USD")
plt.xticks(range(1960, 2020, 10))
plt.ylim(0)

plt.text(x=.8, y=.72, s="""USA""",
        transform=fig.transFigure, ha='left', fontsize=8, alpha=.9)
plt.text(x=.8, y=.44, s="""China""",
        transform=fig.transFigure, ha='left', fontsize=8, alpha=.9)
plt.text(x=.83, y=.165, s="""Russia""",
        transform=fig.transFigure, ha='left', fontsize=8, alpha=.9)
plt.legend(loc='best')
plt.savefig('GDP.png')

plt.show()
