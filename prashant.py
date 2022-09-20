from msilib.schema import AdminUISequence
from plyer import notification
import time
name=input("Input your name - ")
title=input("plese input your tittle - ")
message = input("Reminder you want to set for - ")
notification.notify(title=title,
                    message="Hello {} \n {}".format(name,message),
                    toast=False,
                    timeout=10,
                    app_icon = "Paomedia-Small-N-Flat-Bell.ico")
time.sleep(60*60*24)
