import numpy as np

ages = np.random.randint(5, 100, 50) # Generating random ages
bins = [0, 10, 20, 30, 40, 50, 60, 120]

plt.hist(ages, bins=bins, edgecolor='black', color='lightgreen')
plt.title('Age Distribution of Students')
plt.xlabel('Age Group')
plt.ylabel('No. of Students')
plt.show()