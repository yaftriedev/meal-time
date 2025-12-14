import time
from web.util import get_meal_time_array
from datetime import datetime
# from gpiozero import LED

hours = get_meal_time_array()
actual_day = datetime.now().date()

def dispend(h):
    with open("logs/gpio-log.txt", "a") as log_file:
        log_file.write(f"Dispensing meal at {h} on {datetime.now()}\n")

while True:
    now = datetime.now()

    # If day has changed, reload hours
    if now.date() != actual_day:
        hours = get_meal_time_array
        dia_actual = now.date()

    # Schedule meals
    scheduled_hours = [h for h in hours if 
                       (now.hour, now.minute, now.second) >= (h.hour, h.minute, h.second)]

    for h in scheduled_hours:
        dispend(h)
        hours.remove(h)

    time.sleep(1)
