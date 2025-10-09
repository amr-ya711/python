# Task: Weather Advisor
Temperature = float(input("Enter the current Temperature in Celsius: "))

if Temperature >= 30:
    print("It's a hot day. Stay hydrated!")
elif Temperature >= 20 and Temperature <= 29:
    print("It's a warm day. Enjoy the weather!")
elif Temperature >= 10 and Temperature <= 19:
    print("It's a cool day. Wear a jacket!")
else:
    print("It's a cold day. Stay warm!")