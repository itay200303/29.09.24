# start

# try lets you handle the error and except lets you handle the error

# we need to catch the error in order not to repeat the same mistake several times

x = 88
try:
    x / 0
except ZeroDivisionError:
    print("You cant divide the number by 0")

try:
    raise ValueError("Error mistake.")
except ValueError as e:
    print(f"the Error is caught: {e}")

list_num: list[int] = [0] * 4
try:
    for i in range(4):
        num = int(input("Enter a number: "))
        if num == -999:
            break
        list_num[i] = num
        print(f"{i} in list_num: {list_num[i]}")

except ValueError:
    print("Put in only numbers")
except IndexError:
    print("The index is out of range")
