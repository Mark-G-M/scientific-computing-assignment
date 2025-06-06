import matplotlib.pyplot as plt

# Temperature readings for 7 days
temperatures = [20, 22, 19, 23, 21, 24, 20]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Plotting the line graph
plt.plot(days, temperatures, marker='o', linestyle='-', color='blue')
plt.title('Weekly Temperature Readings')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()
