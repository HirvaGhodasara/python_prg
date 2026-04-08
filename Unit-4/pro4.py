import matplotlib.pyplot as plt

years = ['2021', '2022', '2023', '2024', '2025']
profits = [12000, 15000, 13500, 18000, 21000]

plt.plot(years, profits, marker='o', linestyle='-', color='b')
plt.title('Company Profit Over 5 Years')
plt.xlabel('Year')
plt.ylabel('Profit')
plt.show()