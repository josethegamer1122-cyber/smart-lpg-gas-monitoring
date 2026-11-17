import random
import time
import matplotlib.pyplot as plt

FULL_LPG = 14.2
EMPTY_CYLINDER = 15.0

lpg_remaining = 14.2

time_data = []
weight_data = []
lpg_data = []

print("====================================")
print("   AI BASED LPG PREDICTION SYSTEM")
print("====================================")

for hour in range(24):

    temperature = random.uniform(25, 35)
    consumption = random.uniform(0.02, 0.06)

    lpg_remaining -= consumption

    if lpg_remaining < 0:
        lpg_remaining = 0

    total_weight = EMPTY_CYLINDER + lpg_remaining
    lpg_percentage = (lpg_remaining / FULL_LPG) * 100

    time_data.append(hour)
    weight_data.append(total_weight)
    lpg_data.append(lpg_percentage)

    print()
    print("Hour:", hour)
    print("Temperature:", round(temperature, 2), "°C")
    print("Cylinder Weight:", round(total_weight, 2), "kg")
    print("LPG Remaining:", round(lpg_percentage, 2), "%")

    time.sleep(0.2)

plt.plot(time_data, weight_data, marker="o")

plt.title("LPG Cylinder Weight")
plt.xlabel("Time (Hours)")
plt.ylabel("Weight (kg)")
plt.grid(True)

plt.show()

print()
print("Simulation completed.")