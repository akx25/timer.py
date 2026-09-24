import time
import winsound


print("\033[1m" + "Timer" + "\033[0m")
print("\033[1m" + "(Made By: akx25)" + "\033[0m")
print("")
print("")
print("")
print("\033[1m" + "You can calculate your time if you want!" + "\033[0m")

def calculator():
	first_number = float(input("Enter a number:"))
	operator = input("Enter an operator (+, -, *, /): ")
	second_number = float(input("Enter a second number:"))

	if operator == "+":
		result = first_number + second_number
	elif operator == "-":
		result = first_number - second_number
	elif operator == "*":
		result = first_number * second_number
	elif operator == "/":
		if second_number == 0:
			print("MATH ERROR (Can't divide 0 by 0!)")
			return
		result = first_number / second_number
	else:
		print("Invalid operator")
		return

	print(f"Result: {result}")

if input("Do you want to calculate your time (y/n)") =="y":
    calculator()
    print("----------------------------------------------------------------------------------------------------")
    
    

print("")
print("")
print("")
print("\033[1m" + "NOTICE THAT DECIMALS OR NUMBERS ARE NOT SUPPORTED! (If you do type decimals or numbers the software will crash...)" + "\033[0m")
print("")
print("")
print("")
print("(Enter your time...)")

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1

    print("Time's up!")

t = input("Enter the time in seconds: ")

countdown(int(t))

winsound.PlaySound(
    ".wav",
    winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC
)

input("Press Enter to stop the timer:")
