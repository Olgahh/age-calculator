from datetime import date

def check_birthdate(year, month, day):
	x = date.today()
	if int(year) > x.year :
		return False
	elif (x.year == int(year)) and (x.month < int(month)):
		return False
	elif (x.year == int(year)) and (x.month == int(month)) and (x.day < int(day)):
		return False
	else:
		return True

def calculate_age(year, month, day):
    # write code here
	date_today = date.today()
	if date_today.month > int(month):
		age = (date_today.year - int(year))
	elif date_today.month == int(month) and date_today.day > int(day):
		age = (date_today.year - int(year))
	else:
		age = (date_today.year - int(year)) - 1
	print("You are {} years old".format(age))


def main():
	# write main code here
	year = input("Enter year of birth: ")
	month = input("Enter month of birth: ")
	day = input("Enter day of birth: ")

	if check_birthdate(year,month,day) == True:
		calculate_age(year,month,day)
	else:
		print("Birthdate is invalid")


if __name__ == '__main__':
	main()
