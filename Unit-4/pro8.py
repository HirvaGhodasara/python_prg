courses = ['MCA', 'BCA', 'MSC', 'BSC']
students = [120, 80, 40, 60]

# Find the index of the max value to explode it
explode = [0.1 if x == max(students) else 0 for x in students]

plt.pie(students, labels=courses, explode=explode, autopct='%1.1f%%', shadow=True)
plt.title('Student Distribution per Course')
plt.show()