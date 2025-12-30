import time
from datetime import datetime, timedelta

def countdown(target_time):
    """
    Displays a real-time countdown to a specified target_time.
    target_time should be a datetime object.
    """
    while True:
        # Get the current time
        now = datetime.now()
        # Calculate the remaining time
        time_left = target_time - now

        # Check if the countdown is finished
        if time_left <= timedelta(0):
            print("🎉 Time's up! Happy Event! 🎉")
            break

        # Extract days, hours, minutes, and seconds from the timedelta
        days = time_left.days
        seconds = time_left.seconds
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)

        # Format the output string using carriage return (\r) to overwrite the previous line
        countdown_display = f"Time remaining: {days} days, {hours:02d}:{minutes:02d}:{seconds:02d}"
        print(countdown_display, end="\r")

        # Pause the script for 1 second before the next iteration
        time.sleep(1)

# --- Example Usage ---
# Set the target date and time (e.g., December 31st, 2025 at midnight)
# Replace with your desired year, month, day, hour, minute, second
target_date = datetime(2025, 12, 31, 23, 59, 59)

# Start the countdown
countdown(target_date)