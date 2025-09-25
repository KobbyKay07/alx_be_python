from datetime import datetime, date, timedelta
display_current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("Current date and time:", display_current_datetime)

current_date = date.today()

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=number_of_days)
    print(f"Future date: {future_date}")
calculate_future_date()