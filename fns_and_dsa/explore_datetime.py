from datetime import datetime, date, timedelta

def display_current_datetime():
    current_date_and_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", current_date_and_time)


def calculate_future_date():
    current_date = date.today()
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=number_of_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

display_current_datetime()
calculate_future_date()