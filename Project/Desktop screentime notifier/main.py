import time
from plyer import notification


def notifyMe():
    notification.notify(
        title="Screen Time Reminder",
        message="Every 20 minutes spent using a screen; you should try to look away at something that is 20 feet away from you for a total of 20 seconds.",
        app_icon="/home/vaishnavi/PycharmProjects/pythonProject/warning.ico",
        timeout=10
    )


if __name__ == '__main__':
    while True:
        notifyMe()
        time.sleep(1200)
