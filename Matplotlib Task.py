import matplotlib.pyplot as graph

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
temperatures = [22, 24, 19, 23, 25, 27, 26]  # مثال لدرجات الحرارة (تقدر تغيرها)

graph.plot(days, temperatures, marker='o', linestyle='-', color='b')

graph.title("Temperature Variation Over a Week")
graph.xlabel("Days of the Week")
graph.ylabel("Temperature (°C)")

graph.show()
