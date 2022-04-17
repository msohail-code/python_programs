arr = []
while True:
    num = input("Enter any number:")

    if num == "finish" or num == "Finish":
        break
    try:
        value = int(num)
        arr.append(value)
    except:
        print("Please enter any number.")

total = 0
for i in arr:
    total += i

average = total/len(arr)

print("Total: ",total)
print("Average: ", average)




