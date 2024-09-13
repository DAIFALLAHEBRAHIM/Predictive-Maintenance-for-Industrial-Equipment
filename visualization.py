import matplotlib.pyplot as plt

# Visualize sensor data
plt.figure(figsize=(10, 6))
plt.plot(data['time'], data['temperature'], label='Temperature')
plt.plot(data['time'], data['vibration'], label='Vibration')
plt.plot(data['time'], data['pressure'], label='Pressure')
plt.xlabel('Time')
plt.ylabel('Sensor Values')
plt.title('Sensor Data Over Time')
plt.legend()
plt.show()
