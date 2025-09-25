import datetime
display_current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("Current date and time:", display_current_datetime)

current_date = datetime.date.today()

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + datetime.timedelta(days=number_of_days)
    print(f"Future date: {future_date}")
calculate_future_date()