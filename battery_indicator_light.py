# Battery Notifier
# pip install plyer
from plyer import notification
import psutil
from time import sleep
while True:
    battery = psutil.sensors_battery()
    life = battery.percent
    if life < 50:
        notification.notify(
            title = "Battery Low",
            message = "Please connect to power source",
            timeout = 10
        )
    # sleep(60)
    elif life > 50:
        notification.notify(
            title = "Battery Is Quite Good",
            message = "You can Work Tension Free",
            timeout = 10
        )
    sleep(60)