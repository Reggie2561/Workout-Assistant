import os
import sys


class Notification:
    def __init__(self,):
        self.os = sys.platform

    def send(self, title, content, priority="default", length=5):
        if self.os.startswith("win"):
            from win10toast import ToastNotifier
            try:
                noti = ToastNotifier()
                noti.show_toast(title, content, duration=length, threaded=True)
            except Exception as e:
                print(e)
        else:
            os.system(f"termux-notification -t {title} -c {content} --alert-once --priority {priority}")
            os.system(f"notify-send '{title}', '{content}'")