
import numpy as np
import matplotlib.pyplot as plt
 
barWidth = 0.25
 
bars1 = [25, 13, 10, 5, 5]
bars2 = [15, 5, 13, 10, 5]
bars3 = [10, 5, 10, 10, 5]
 
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
 
plt.bar(r1, bars1, color='#D4AF37', width=barWidth, edgecolor='white', label='Gold Medals')
plt.bar(r2, bars2, color='#CCCCCC', width=barWidth, edgecolor='white', label='Silver Medals')
plt.bar(r3, bars3, color='#A97142', width=barWidth, edgecolor='white', label='Bronze Medals')
 
plt.xlabel('Countries', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['A', 'B', 'C', 'D', 'E'])
 
plt.legend()
plt.show()

plt.savefig('/This PC/Documents/my_StackedBarChart.pdf')
