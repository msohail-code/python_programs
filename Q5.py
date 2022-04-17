while True:
    num = input("Enter any number:")

    if num == "finish" or num == "Finish":
        break
    try:
        value = float(num)
        if value < 0 or value > 1:
            print("Bad Score.")
        elif value >= 0.95:
            print("A")
        elif value>=0.8:
            print("B")
        elif value>=0.75:
            print("C")
        elif value>=0.5:
            print("D")
        elif value<0.5:
            print("F")
            
    except:
        print("Please enter any number.")
