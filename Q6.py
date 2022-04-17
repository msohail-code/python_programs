def computepay(hours,rate):
    return hours*rate

hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))
pay = computepay(hours,rate)

print("Pay: ",pay)
