import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl
import openpyxl

df = pd.read_excel('export_Russia.xlsx')
plt.style.use('TheEconomist.mplstyle')

fig, (ax1, ax2) = plt.subplots(1, 2)

Period = df['Year'].tolist()
TotalExport = df['Total_merchandise'].tolist()
Fuels = df['Fuels_and_mining_products'].tolist()
Agriculture = df['Agricultural_products'].tolist()
Manufacture = df['Manufactures'].tolist()

ax1.set_xlabel('Period')
ax1.set_ylabel('Value')
ax1.set_title('Export Values, $million', fontweight='bold',
              fontsize=14, loc='center')

ax1.plot(Period, TotalExport,
         label='Total Export', color='royalblue')

ax1.plot(Period, Fuels,
         label='Fuels and mining products', color='limegreen')

ax1.plot(Period, Manufacture,
         label='Manufacture', color='darkorange')

ax1.plot(Period, Agriculture,
         label='Agriculture', color='crimson')

labels = ['Fuel prod.', 'Manufacture', 'Agriculture']
Data = [df['Fuels_and_mining_products'].sum(),
        df['Agricultural_products'].sum(),
        df['Manufactures'].sum()]

ax2.pie(Data, labels=labels, autopct='%1.2f%%', startangle=90)

ax2.set_title('Export Structure', fontweight='bold',
              fontsize=14, loc='center')

ax1.legend(loc='best')
ax2.legend(loc='best')

plt.savefig('Export RU')
plt.show()
