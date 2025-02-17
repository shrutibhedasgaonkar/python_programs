import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import numpy as np

# Data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temperatures = [25, 27, 26, 28, 30, 29, 31]
days = [1, 2, 3, 4, 5, 6, 7]

# Plot
plt.plot(days, temperatures, marker='o', linestyle='--', color='green', label="Temperature")

# Labels and title
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Trend Over the Week")
plt.legend()

# Show plot
plt.show()

plt1.arrow(days, temperatures, 0.2, 0.2, head_width=0.01, head_length=0.01, fc='green')
plt1.show()

plt.bar(days, temperatures, 0.5, )
plt.show()
