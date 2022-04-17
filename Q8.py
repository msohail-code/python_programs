def computepay(hours,rate):
    return hours*rate

hours =input("Enter hours: ")
try:
    check_hours=float(hours)
    rate = input("Enter rate: ")

    check_rate = float(rate)
    pay = computepay(check_hours,check_rate)

    print("Pay: ",pay)
except:
    print("Error, Please enter numeric value only")
