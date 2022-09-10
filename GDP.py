import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('gdp_data.csv')
fig, ax = plt.subplots()
USA = df[df['Country Code'] == 'USA']
Russia = df[df['Country Code'] == 'RUS']
China = df[df['Country Code'] == 'CHN']
plt.plot(USA['Year'], USA['Value'] / 1_000_000_000_000, label='USA GDP', color='deepskyblue')
plt.plot(Russia['Year'], Russia['Value'] / 1_000_000_000_000, label='Russia GDP', c='red')
plt.plot(China['Year'], China['Value'] / 1_000_000_000_000, label='China GDP', c='darkgreen')
plt.title('USA and Russia GDP', fontsize=20, fontweight='bold')
plt.xticks(range(1960, 2020, 4))
plt.grid(alpha=0.1, color='black')
plt.legend(loc='best')
plt.show()
